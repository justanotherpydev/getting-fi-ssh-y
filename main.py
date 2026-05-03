import random
import os
import json

SAVE_FILE = "player_save.json"


def split():
    print("____________________________")


# ================= SAVE / LOAD =================

def load_game():
    global inventory, money

    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            inventory = data["inventory"]
            money = data["money"]
    except:
        print("No save found, starting new game...")
        inventory = {
            "bass": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "trout": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "bluegill": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "crapie": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "coyfish": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "retrofish": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0}
        }
        money = 0


def save_game(silent=False):
    data = {
        "inventory": inventory,
        "money": money
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    if not silent:
        print("Game saved!")


def wipe_save():
    global inventory, money

    print("\n⚠ WARNING: This will permanently delete your save.")
    split()

    total_fish = sum(sum(f.values()) for f in inventory.values())

    print(f"You have ${money} and {total_fish} fish.")
    confirm = input("Type WIPE to confirm or press ENTER to return >>> ")

    if confirm.upper() == "WIPE":
        inventory = {
            "bass": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "trout": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "bluegill": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "crapie": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "coyfish": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0},
            "retrofish": {"beat up": 0, "standard": 0, "long": 0, "short": 0, "flawless": 0}
        }
        money = 0

        save_game(silent=True)
        print("Save wiped.")
    else:
        print("Wipe canceled.")


# ================= GAME DATA =================

fish = ["bass", "trout", "bluegill", "crapie"]
specialfish = ["retrofish", "coyfish"]

fish_values = {
    "bass": 10,
    "trout": 12,
    "bluegill": 5,
    "crapie": 5,
    "coyfish": 100,
    "retrofish": 100
}

conditions = ["beat up", "standard", "long", "short", "flawless"]

condition_multipliers = {
    "beat up": 0.5,
    "standard": 1,
    "long": 1.2,
    "short": 0.8,
    "flawless": 2
}


# ================= CORE SYSTEMS =================

def calculate_inventory_value():
    total = 0

    for fish_name, conds in inventory.items():
        for condition, amount in conds.items():
            total += amount * fish_values[fish_name] * condition_multipliers[condition]

    return int(total)


def castline():
    print("\nCasting line...\n")

    num = random.randint(1, 10)

    if num == 5:
        fih = random.choice(specialfish)
    else:
        fih = random.choice(fish)

    condition = random.choice(conditions)

    value = int(fish_values[fih] * condition_multipliers[condition])

    print(f"You caught a {condition} {fih} worth ${value}")

    inventory[fih][condition] += 1


def sell_all():
    global money

    total_value = calculate_inventory_value()

    if total_value == 0:
        print("You have nothing to sell.")
        return

    print(f"You sold all fish for ${total_value}!")

    money += total_value

    # reset inventory
    for fish_name in inventory:
        for condition in inventory[fish_name]:
            inventory[fish_name][condition] = 0


def show_stats():
    split()

    print(f"\n Money: ${money}")
    print(f" Inventory value: ${calculate_inventory_value()}")

    split()

    for fish_name in inventory:
        total_count = sum(inventory[fish_name].values())

        total_value = 0
        for condition, amount in inventory[fish_name].items():
            total_value += amount * fish_values[fish_name] * condition_multipliers[condition]

        print(f"{fish_name}: {total_count} → ${int(total_value)}")


def open_shop():
    print("shop coming soon...")
    split()


# ================= COMMANDS =================

commands = {
    "cast": "go fishing",
    "show": "show your stats",
    "sell": "sell all your fish",
    "shop": "open the shop",
    "help": "list all commands",
    "clear": "clear the screen",
    "save": "save your game",
    "wipe": "wipe your save data",
    "exit": "exit the game"
}


# ================= MAIN =================

load_game()

print("welcome to getting fi-ssh-y!")
print('use "help" for help')

while True:
    choice = input("user terminal >>> ").lower()

    if choice == "help":
        for cmd, desc in commands.items():
            print(f"{cmd} - {desc}")

    elif choice == "cast":
        castline()

    elif choice == "show":
        show_stats()

    elif choice == "sell":
        sell_all()

    elif choice == "shop":
        open_shop()

    elif choice in ("cls", "clear"):
        os.system("cls" if os.name == "nt" else "clear")

    elif choice == "save":
        save_game()

    elif choice == "wipe":
        wipe_save()

    elif choice == "exit":
        os.system("cls" if os.name == "nt" else "clear")
        show_stats()
        print("____________________________")
        print("Goodbye!")
        break

    else:
        print("bad command... try again!")
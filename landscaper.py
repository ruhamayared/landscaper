# Game State
game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "scissors", "profit": 5, "cost": 5},
    {"name": "push_lawnmower", "profit": 50, "cost": 25},
    {"name": "battery_lawnmower", "profit": 100, "cost": 250},
    {"name": "team", "profit": 250, "cost": 500},
]

# Game Option Functions


def mow_lawn():
    tool = tools[game["tool"]]
    print(
        f"You mowed the lawn using {tool['name']} and earned ${tool['profit']}!")
    game["money"] += tool["profit"]


def check_stats():
    tool = tools[game["tool"]]
    print(
        f"You currently have ${game['money']} and are using a {tool['name']}.")


def upgrade():
    next_tool = tools[game["tool"] + 1]

    if (next_tool == None):
        print("There are no more tools.")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("Not enough money to buy tool.")
        return 0
    else:
        print(f"You just upgraded to {next_tool['name']}!")
    game["money"] -= next_tool["cost"]
    game["tool"] += 1


def win_check():
    if (game["tool"] == 5 and game["money"] == 1000):
        print("You won the game!")
        return True
    return False


# Loop for user's choices
while (True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [Q] Quit")

    if (user_choice == "Q"):
        print("You quit the game.")
        break
    elif (user_choice == "1"):
        mow_lawn()
    elif (user_choice == "2"):
        check_stats()
    elif (user_choice == "3"):
        upgrade()
    elif (win_check()):
        break

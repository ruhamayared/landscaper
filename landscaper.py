game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "scissors", "profit": 5, "cost": 5},
    {"name": "push_lawnmower", "profit": 50, "cost": 25},
    {"name": "battery_lawnmower", "profit": 100, "cost": 250},
    {"name": "team", "profit": 250, "cost": 500},
]

while (True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [Q] Quit")

    tool = tools[game["tool"]]

    if (user_choice == "Q"):
        break
    elif (user_choice == "1"):

        print(
            f"You mowed the lawn using {tool['name']} and earned ${tool['profit']}!")
    elif (user_choice == "2"):
        print()

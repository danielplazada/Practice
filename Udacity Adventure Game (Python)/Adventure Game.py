import random
import time


def text_delay(text_string):
    print(text_string)
    time.sleep(2)


def start_story(weapon, villain):
    text_delay("You wake up on a hill. On the left of you there is a."
        "On the left of you there is a river"
        "On the right there is a rainforest."
        "Beside you find a wooden spear, but might not last for long."
        "you need to find a better.")


def village(weapon, villain):
    if "magic_wand" in weapon:
        text_delay("You already been here, you already have a"
                   "good weapon, try to explore another area")
    else:
        text_delay("You enter a small shop and you notice"
                   "a magical wand...")
        text_delay("you decide to get the magical wand"
                   "and you start to walk back to the hill")
    weapon.append("magic_wand")
    player_choice(weapon, villain)


def rainforest(weapon, villain):
    text_delay("As you are walking in the forest you walk into the" + villain + ".")
    if "magic_wand" not in weapon:
        text_delay("You are not prepared to fight" + villain + ".")
    while True:
        player_input_2 = input("Do you want to fight (choose 1) or attept to escape (choose 2)")
        if player_input_2 == "1":
            if "magic_wand" in weapon:
                print("You are much stronger then" + villain + ".\n")
                print("You defeted the " + villain + ". \n")
                play_game()
    else:
        text_delay("YOU DIED the" + villain + " was stronger then you.")
        play_again()
        text_delay("\n")
        if player_input_2 == "2":
            text_delay("You escaped and you are safe")
            player_choice(weapon, villain)


def player_choice(weapon, villain):
        text_delay("Choice 1 Go to nearby village")
        text_delay("Choice 2 Go to the nearby forest")
        text_delay("Please choose your adventure!")
        while True:
            player_input = input("(Please enter 1 or 2.)\n")
            if player_input == "1":
                village(weapon, villain)
                break
            elif player_input == "2":
                rainforest(weapon, villain)


def retry_game():
        text_delay("Loading new game...")


def end_game():
        text_delay("Cloasing game please wait...")
        exit()


def play_game():
    again = input("Would you like to play again? (yes/no)").lower()
    if again == "yes":
        retry_game()
    elif again == "no":
        end_game()
    else:
        exit()


def main_game():
    weapon = []
    villain = random.choice(["evil wizard", "witch", "river monster", "troll"])
    start_story(weapon, villain)
    player_choice(weapon, villain)

main_game()

#import proper files
import time
import random

#Created a funtion that will make a 2.5 second pause between text.
def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2.5)
def intro(item, option):# intrudaction to the game
    print_pause("You wake up in a small patch of tall grass "
                "with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    print_pause("On the left of you there is a river.\n")
    print_pause("On the right there is a rainforest.\n")
    print_pause("Beside you find a wooden spear, but might not last for long.\n")
    print_pause("you need to find a better weapon.\n")
def rainforest(item, option):#The player must enter the rainforest to find a
                             #magigal wand in order to win the game
    if "magic_wand" in item:
        print_pause("\nYou begin walking into the rain forest.")
        print_pause("\nYou relize you been here and the moster is not here.1")
        print_pause("\nYou walk back towards the river. \n")
    else:
        print_pause("\nYou begin walking into the rain forest.")
        print_pause("\nYou relize its filled with dangrous animals.")
        print_pause("\nYou notice a shiny red light coming from a nearby tree.")
        print_pause("\nYou decide to quickly run towars the red light")
        print_pause("\nYou found a magical wand, you decide that its a better"
                    " wapon then the wooden spear.")
        print_pause("\nYou quickly turn back and run towards the river.\n")
        item.append("magic_wand")
    field(item, option)
def house(item, option): # House is where the moster lives
    print_pause("\nYou approach the door of the house.")
    print_pause("\nYou enter the old house and inside you find a " + option + ".")
    print_pause("\nEep! This is the " + option + "'s house!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "magic_wand" not in item:
        print_pause("You are not prepared to fight" + option + ".\n")
    while True:
        choice_two = input("Would you like to try (1) fight or (2) "
                        "run away?")
        if choice_two == "1":
            if "magic_wand" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you take out your weapon. \n")
                print_pause("\nThe Magical Wand shines brightly in "
                            "your hand as"+option+"is ready to attack you.")
                print_pause("\nThe " + option + " notices that your weapon"
                            " is more powerful, and runs away!")
                print_pause("\nYou saved the town the the terror of"+option+" !\n")
            else:
                print_pause("\nYou try to fight the"+option+"but your wooden spear broke! ")
                print_pause("\nYou lost!\n")
            play_again()
            break
        if choice_two == "2":
            print_pause("\nYou run back towards the river and cross it using your raft. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            field(item, option)
            break
def field(item, option):
    print_pause("Enter 1 to enter the rain forest.")
    print_pause("Enter 2 to cross the river and go to the old house.")
    print_pause("What would you like to do?")
    while True:
        choice_one = input("(Please enter 1 or 2.)\n")
        if choice_one == "1":
            rainforest(item, option)
            break
        elif choice_one == "2":
            house(item, option)
            break
def play_again():
    again = input("Would you like to play again? (yes/no)").lower()
    if again == "yes":
        print_pause("\n\n\nPlease wait restarting the game ...\n\n\n")
        print_pause("\n\n\n...\n\n\n")
        print_pause("\n\n\n...\n\n\n")
        play_game()
    elif again == "no":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()
def play_game():
    item = []
    option = random.choice(["evil wizard", "witch", "river monster", "troll"])
    intro(item, option)
    field(item, option)
play_game()

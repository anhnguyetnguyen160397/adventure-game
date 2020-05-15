import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(message, option1, option2):
    while True:
        choose = input(message)
        if choose == option1:
            return choose
        elif choose == option2:
            return choose


def intro(monster):
    print_pause('You find yourself standing in an open field,'
                'filled with grass and yellow wildflowers.')
    print_pause(f'Rumor has it that a {monster} is somewhere around here,'
                ' and has been terrifying the nearby village.')
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause("In your hand you  hold your trusty (but not very effective) "
                "dragger.\n")
    


def house_or_cave(item, monster):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    choose_path = valid_input("Please enter 1 or 2.\n", '1', '2')
    if choose_path == '1':
        house(item, monster)
    elif choose_path == '2':
        cave(item, monster)


def house(item, monster):
    print_pause('You approach the door of the house.')
    print_pause('You are about to knock when the door opens '
                f'and out steps a {monster}.')
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f'The {monster} attacks you!')
    if "sword" not in item:
        print_pause('You feel a bit under-prepared for this, '
                    'what with only having a tiny dragger.')
    choose_solution = valid_input('Would you like to (1) fight '
                                  'or (2) run away?\n', '1', '2')
    if choose_solution == '1':
        if 'sword' in item:
            print_pause(f'As the {monster} moves to attack, '
                        'you unsheath your new sword.')
            print_pause('The Sword of Ogoroth shines brightly '
                        'in your hand as you brace yourself for the attack.')
            print_pause(f'But the {monster} takes one look at your shiny new '
                        'toy and runs away!')
            print_pause(f'You have rid the town of the {monster}. '
                        'You are victorious!')
        else:
            print_pause('You do your best. . .')
            print_pause(f'but your dragger is no match for the {monster}')
            print_pause('You have been defeated!')
        play_again(monster)
    elif choose_solution == '2':
        print_pause('You run back into the field. Luckily, '
                    'you don\'t seem to have been followed.\n')
        house_or_cave(item, monster)


def cave(item, monster):
    print_pause('You peer cautiously into the cave.')
    if 'sword' in item:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.\n")
        house_or_cave(item, monster)
    else:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eyes catches a glint of metal Sword'
                    ' of Ogoroth!')
        print_pause('You discard your silly old dragger'
                    'and take the sword with you.')
        item.append('sword')
        print_pause('You walk back out to the field.\n')
        house_or_cave(item, monster)


def play_again(monster):
    play_again = valid_input('Would you like to play again? (y/n)', 'y', 'n')
    if play_again == 'y':
        print_pause('Excellent! Restarting the game . . .')
        play_game(random.choice(list))
    elif play_again == 'n':
        print_pause('Thanks for playing! See you next time.')

list = ['troll', 'gorgon', 'dragon', 'pirate']

def play_game(monster):
    item = []
    intro(monster)
    house_or_cave(item, monster)


play_game((random.choice(list)))

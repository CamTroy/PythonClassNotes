# Monster
from sympy import false
from sympy.strategies.core import switch

monsters = []

class Monster:

    name = ""
    type = ""
    health = 100
    attack_power = 10

    def __init__(self, name, type, health, attack_power):

        self.name = name
        self.type = type
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_monster):

        other_monster.health -= self.attack_power

    def is_alive(self):

        if self.health > 0:
            return True
        return False

def get_num_input(message):

    num_input = ""
    is_valid = False
    while not is_valid:

        num_input = input(message)
        if not (num_input.isnumeric()):

            print("That's not a number, stupid idiot")
        else:

            is_valid = True

    return int(num_input)

def get_num_input_with_range(message, min, max):

    num_input = ""
    is_valid = False
    while not is_valid:

        num_input = input(message)
        if not (num_input.isnumeric() and min <= int(num_input) <= max):

            print(f"Type a number between {min} and {max}")
        else:

            is_valid = True

    return int(num_input)

def create_monsters():

    global monsters
    sub_list = []

    while True:

        monster_name = input(f"Enter a name.\n")
        monster_type = input(f"What element is the monster?\n")
        monster_health = get_num_input(f"What is the monster's health?\n")
        monster_attack = get_num_input(f"What is the monster's attack?")

        sub_list.append(Monster(monster_name, monster_type, monster_health, monster_attack))

        continue_option = input("Do you want to continue? yes/no\n")
        if not (continue_option.lower() == "yes" or continue_option.lower() == "y"):

            break


    monsters += sub_list

def fight():

    index = 0
    for monster in monsters:

        index += 1
        print(f"{index}: {monster.name}, {monster.type}, {monster.health}, {monster.attack_power}\n")

    first_monster = monsters[get_num_input_with_range("Which monster should go first?\n", 1, len(monsters) + 1) - 1]
    second_monster = monsters[get_num_input_with_range("Which monster should go second?\n", 1, len(monsters) + 1) - 1]

    first_og_health = first_monster.health
    second_og_health = second_monster.health

    while first_monster.is_alive() or second_monster.is_alive():

        if not (first_monster.is_alive() and second_monster.is_alive()):
            break

        if first_monster.is_alive() and second_monster.is_alive():

            print(f"{first_monster.name} hit {second_monster.name} for {first_monster.attack_power} damage!\n")
            print(f"{second_monster.name} has {second_monster.health} health left!")
            second_monster.health -= first_monster.attack_power

        if first_monster.is_alive() and second_monster.is_alive():

            print(f"{second_monster.name} hit {first_monster.name} for {second_monster.attack_power} damage!\n")
            print(f"{first_monster.name} has {first_monster.health} health left!")
            first_monster.health -= second_monster.attack_power

    if first_monster.is_alive():
        print(f"{first_monster.name} won!")

    if second_monster.is_alive():
        print(f"{second_monster.name} won!")

    first_monster.health = first_og_health
    second_og_health = second_monster.health

while True:

    option = get_num_input("Pick an option:\n"
                           "1. Create new monsters\n"
                           "2. View all monsters\n"
                           "3. Make two monsters fight\n"
                           "4. Exit\n")

    match option:

        case 1:

            create_monsters()
        case 2:

            print(monsters)
        case 3:

            fight()
        case 4:

            print("Thank you for playing!")
            break
        case _:

            print("Thank you for playing!")
            break
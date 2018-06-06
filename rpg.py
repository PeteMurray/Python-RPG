import re
import random

# Inventory system
class Item(object):
    def __init__(self, name, attack, armor, weight, price):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price

class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Atk', 'Arm', 'Lb', 'Val']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price]]))

    def __str__(self):
        out = '\t'.join(['Name', 'Atk', 'Arm', 'Lb', 'Val'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price]])
        return out

inventory = Inventory()
inventory.add_item(Item('Sword', 5, 1, 15, 2))
inventory.add_item(Item('Armor', 0, 10, 25, 5))

# Character name and stats
user_character = [["Name"," "],
                  ["Level",1],
                  ["Exp",0],
                  ["Health Points",20],
                  ["Energy",10],
                  ["Strength",1],
                  ["Defense",1],
                  ["Status","Normal"]]

def character_creation():

    user_name = input("What is your name?: ")

    while True:
        if not re.match("^[A-Za-z]*$", user_name):
            print("Only letters, please.")
            user_name = input("What is your name?: ")
        elif len(user_name) < 1:
            print("Please input something!")
            user_name = input("What is your name?: ")
        elif len(user_name) > 16:
            print("Sixteen character limit for names.")
            user_name = input("What is your name?: ")
        else:
            # Adds username to user_character
            user_character[0][1] = str(user_name)
            print("\n")
            break

    # Print the characters stats
    for i in user_character:
        print(*i, sep=": ")
    print("You have the following in your inventory:")
    print(inventory)

character_creation()

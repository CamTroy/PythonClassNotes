# Even or Odd Checker
from random import randint
import webbrowser
import re

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

def even_or_odd():

    num = get_num_input("Enter a number.")

    if num % 2 == 0:
        print(f"{num} is odd!")
    else:
        print(f"{num} is even!")

# Calculator
def calc():

    num1 = get_num_input()
    num2 = get_num_input()

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} x {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")

# Number Guessing Game
def guessing_game():

    random_num = randint(0, 10)
    guess = get_num_input("Enter a number.")

    if random_num == guess:
        print("Great job!")
    else:
        print("You guessed wrong!")
        webpage = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open_new_tab(webpage)

# Basic Password Checker
#
# Ask for a password and check if it meets basic rules (length, contains numbers, etc.).
#
# Concepts: Strings, conditions, input, len().
# Password checker
# Requirements: 5 characters, at least 1 number
def password_checker():

    password = input("Gib password")
    passes = 0

    if password.__len__() >= 5:
        passes += 1

    if bool(re.search(r'\d', password)):
        passes += 1

    if passes >= 2:
        print("Your password is awesome!!11")
    else:
        print("Your password sucks!!11!")


# Palindrome Checker
#
# Check if a word or sentence is a palindrome.
#
# Concepts: Strings, slicing, functions.

def palindrome():

    string1 = input("Enter a string")

    if string1 == string1[::-1]:
        print("Is a palindrome fr")
    else:
        print("Is not palindrome bruh")

# Largest number in a list.
def largest_number():

    numbers = []
    num1 = get_num_input("Enter a number.")
    num2 = get_num_input("Enter another number.")
    num3 = get_num_input("Enter one more number.")

    biggest = num1
    for num in numbers:
        if num > biggest:
            biggest = num

    print(f"{biggest} is the greatest number in the list.")

# Word Counter
#
# Take a sentence and count how many times each word appears.
#
# Concepts: Dictionaries, strings, loops.
def word_counter():

    sentence = input("Give sentence.")
    words = sentence.split()
    counted_words = {}

    for word in words:

        if not counted_words.__contains__(word.capitalize()):
            counted_words[word.capitalize()] = 1
        else:
            counted_words[word.capitalize()] += 1

    print(counted_words)

even_or_odd()
print()
calc()
print()
guessing_game()
print()
password_checker()
print()
palindrome()
print()
largest_number()
print()
word_counter()

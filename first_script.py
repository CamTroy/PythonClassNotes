# First script!
print("Hello, world!")

# Defining variables
bruh = "bruh"
print(bruh)

def greeting(name, age):
    print("Hello " + name + ". " + "You are " + str(age) + " years old!")

greeting("Cameron", 21)

def is_cringe(person_name):
    if person_name == "Jaxon":
        print(person_name + " is cringe!!")
    elif person_name == "Jackson":
        print(person_name + " person is awesome!!")
    else:
        print("I'm not sure.")

is_cringe("Jaxon")
is_cringe("Jackson")

# Switch/match statements
user_input = "Start"

match user_input:
    case "Start":
        print("Started!")
    case "Stop":
        print("Stopped!")
    case "Pause":
        print("Paused!")
    case _:
        print("Input not recognized.")

# Format strings
name = "Bruh"
age = 18

message = f"Bro's name is {name}, bro is {age} years old."
print(message)

def rawr(*args):
    print(args)

rawr("First arg", 3, "Bruh", False)

def huzzah(first, second, third, fourth, pizza):
    print(first, second, third, fourth, pizza)

# Call functions with params in any order if you use the names.
huzzah(pizza = "Pepperoni", first = "Second", second = 1, fourth = "Infinity", third = "Shrek")

def yell(**args):
    print(args)

yell(first = "second", second = "first", guts = "GRIFFIIIIIIIIIIITH")

# Returning things from functions
def add(left, right):
    return left + right

result = add(10, 3)
print(f"10 + 3 is {result}")

def math(left, right):
    add = left + right
    sub = left - right
    div = left / right
    return add, sub, div

add_result, sub_result, div_result = math(10, 5)
print(add_result, sub_result, div_result)
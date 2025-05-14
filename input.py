# Getting input and stuff

name_input = input("What is your name?")
age_input = input("How old are you?")

def greet(name, age):
    print("Hello ", name, ". You are ", age, " years old.")
    
greet(name_input, age_input)
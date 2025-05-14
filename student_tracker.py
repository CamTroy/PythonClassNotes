import json
import os.path

path = "stuff.json"

students = []

def prompt_for_students():
    while True:
        print("\nEnter student details:")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")

        student = {
            "name": name,
            "age": age,
            "grade": grade
        }

        students.append(student)

        more = input("Add another student? (yes/no): ").strip().lower()
        if more != 'yes':
            break

    return students

def main_menu():
    user_choice = 0
    menu_options = ["Add Students", "Show Students", "Exit"]
    choices = [1,2,3]

    while user_choice not in choices:
        i = 0
        for option in menu_options:
            i = i + 1
            print(f"{i} - {option}")
        try:
            user_choice = int(input(f"Please choose one {choices}"))
        except:
            print("Invalid input. Please try again.")

    return user_choice

def go():
    global students
    students = load_students()
    keep_going = True
    while keep_going:
        option = main_menu()

        match option:
            case 1:
                if not students:
                    students = prompt_for_students()
                else:
                    students = students + prompt_for_students()
            case 2:
                print(students)
                print("\nStudent Information:")
                i = 0
                for student in students:
                    i = i + 1
                    print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            case 3:
                save_students()
                keep_going = False

def load_students():
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
            return data
    return []

def save_students():
    with open(path, "w") as f:
        json.dump(students, f, indent=4)

go()
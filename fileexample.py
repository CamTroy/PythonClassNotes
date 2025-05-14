# FileIO
import json

default_weapon = {
    "Id": 1,
    "Name": "Basic Dagger",
    "Type": "Dagger",
    "Description": "Kills things well enough."
}

weapons = [default_weapon]

def add_weapon(id, name, type, desc):
    weapons.append({"Id": id, "Name": name, "Type": type, "Description": desc})

def save_weapons():
    with open("weapons.json", "w") as f:
        json.dump(weapons, f, indent=4)

def load_weapons():
    with open("weapons.json", "r") as f:
        data = json.load(f)
        return data

# save_weapons()
weapons = load_weapons()
add_weapon(2, "Buster sword", "Sword", "Big sword")
add_weapon(3, "Gunblade", "Gun & Sword", "Gun sword")
add_weapon(4, "Masamune", "Sword", "Long sword")
add_weapon(5, "Keyblade", "Sword", "Sword?")

print(weapons)
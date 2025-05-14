import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Get something
def get_something():

    resp = requests.get(url)
    if resp.status_code == 200:

        stuff = resp.json()
        # print(json.dumps(stuff, indent=4))
        nothing(stuff)
    else:

        print("Bruh: ", resp.status_code)
    return None

# Print something
def nothing(something):

    if something:
        print(f"{something['name']} is a {something['types'][0]['type']['name']} type pokemon. "
              f"\n{something['name']} has {len(something['moves'])} possible moves.")

    if something['abilities']:

        abilities = something['abilities']
        print(f"{something['name']} has {len(something['abilities'])} abilities which are:")
        for element in abilities:
            print("\n", element['ability']['name'])



get_something()
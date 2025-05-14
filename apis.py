import json
import requests

# API stuff
url = "https://api.magicthegathering.io/v1/cards"

cards = []

# Talking to APIs
# Get data from the API
def get_cards():

    # Get the shit
    resp = requests.get(url)

    # Analyze the shit
    if resp.status_code == 200: # Check response code is 200 which means success

        data = resp.json()
        print(json.dumps(data, indent=4))
    else:

        print("Something went wrong.")

def print_cards():
    pass

# POST, won't work in this example because this endpoint doesn't exist, but this is how is done
def update_card():

    url = "https://api.magicthegathering.io/v1/update_card" # This endpoint does not actually exist
    post_data = {
        "id": 1,
        "name": "Bruh"
    }

    headers = {
        "content-type": "application/json"
    }

    requests.post(url, data = json.dumps(post_data), headers = headers)

get_cards()
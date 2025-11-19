import json, sys, requests
from dotenv import dotenv_values

config = dotenv_values(".env")

chosen_object = sys.argv[1]

try:
    chosen_json = ""
    with open(f"{chosen_object}.json", 'r') as file:
        chosen_json = json.load(file)
except:
    print("could not open file.")
    exit()

r = requests.post(config["SERVER_ADDRESS"], json=chosen_json)
print(r.text)
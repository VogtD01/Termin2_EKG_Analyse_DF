import json

# Opening JSON file
file = open("person_db.json")

# Loading the JSON File in a dictionary
person_data = json.load(file)

person_data
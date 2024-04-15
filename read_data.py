import json


def load_person_data():
    """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list():
    person_list = []
    for person in load_person_data():
        person_list.append(person["firstname"] + " " + person["lastname"] )
      
    return person_list

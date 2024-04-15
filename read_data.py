import json


def load_person_data():
    """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list():
    person_list = []
    person_data = load_person_data()
    for person in person_data:
        person_list.append(person["firstname"] + " " + person["lastname"] )
      
    return person_list

def find_person_data_by_name(name):
    person_data = load_person_data()
    for person in person_data:
        if name == person["firstname"] + " " + person["lastname"]:
            return person
    return None
    
        
if __name__ == "__main__":
    print(load_person_data())
    print(get_person_list())
    print(find_person_data_by_name("Max Mustermann"))




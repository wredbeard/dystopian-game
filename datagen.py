import random, json, functions
from faker import Faker


def party_name_selector():

    with open('partynames.txt') as f:
        rng = random.SystemRandom()
        random.seed(rng)
        lines = f.readlines()
        party_name = random.choice(lines)
        return party_name


def people_name_selector():
    people_name = Faker()
    people_name.seed(random.randint(1, 999))
    return people_name.name()


def event_get(event_id):
    with open('events.json') as json_file:
        data = json.load(json_file)
        print(data[event_id]['description'])
        functions.play_menu()


def event_roll():
    min = 0
    max = 100
    rng = random.SystemRandom()
    x = rng.randint(min, max)
    return x

# overly complicated random event generator
def random_event():
    random.seed(random.SystemRandom())
    with open('events.json') as fp:
        data = json.load(fp)
        questions = data
        random_index = random.choice(list(questions))
        print(questions[random_index]['description'])
        effect = questions[random_index]['effect']
        key = questions[random_index]['key']
        value = questions[random_index]['value']
        to_change = var_dict[key][value]
        changed = to_change + effect
        var_dict[key][value] = changed
        write_game_config()
        functions.play_menu()

def random_conversation():
    with open('streetcon.txt') as f:
        rng = random.SystemRandom()
        random.seed(rng)
        lines = f.readlines()
        randomconvo = random.choice(lines)
        return randomconvo

# go ahead and open config file for writing
with open('config.json', 'r') as infile:
    var_dict = json.load(infile)


# write the state of the game to config file

def write_game_config():
    with open('config.json', 'w') as outfile:
        json.dump(var_dict, outfile)

#class to handle the generation of new aides

class aide:
    def __init__(self):
        self.skills = []
        self.names = []
        self.prices = []
        self.skills_mult = []
import random
import json
import functions
from faker import Faker


# picks random rival party name from list
def party_name_selector():

    with open('partynames.txt') as f:
        rng = random.SystemRandom()
        random.seed(rng)
        lines = f.readlines()
        party_name = random.choice(lines)
        return party_name


# enumerates a population for the game with variables such as mood, party support, etc. Work in progress

"""def build_populace(pop_to_enum):
    d = open('populace.json')
    populace = {}
"""
# displays laws from laws.json
def law_roster():
    with open('laws.json') as json_file:
        data = json.load(json_file)
        laws_to_it = []
        for key in data['laws'].values():
            laws_to_it.append(key['description'])
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(laws_to_it)))

# generates random names to pass to functions
def people_name_selector():
    people_name = Faker()
    people_name.seed(random.randint(1, 999))
    return people_name.name()


# shows description of an event from events.json
def event_get(event_id):
    with open('events.json') as json_file:
        data = json.load(json_file)
        print(data[event_id]['description'])
        functions.play_menu()


# returns a random number in range; will soon be deleted
def event_roll():
    min = 0
    max = 100
    rng = random.SystemRandom()
    x = rng.randint(min, max)
    return x


# returns a random number from min, max passed to it. mostly for probabilities
def prob(min, max):
    random.seed(random.SystemRandom())
    x = random.randint(min, max)
    return x


# generates a number to assign to population; less important than membership_gen
def gen_pop():
    min = 1000000
    max = 10000000
    rng = random.SystemRandom()
    x = rng.randint(min, max)
    return x


# assigns party membership to appropriate json keys; will need adjustments
def membership_gen(world_pop):
    percent_1 = prob(5, 10) * .001
    percent_2 = prob(10, 20) * .001
    num_members_myparty = percent_1 * world_pop
    num_members_rival = percent_2 * world_pop
    functions.my_rival['membership'] = round(num_members_rival)
    functions.my_party['membership'] = round(num_members_myparty)


# random event generator, responsible for changing variables based on event effect
def random_event():
    random.seed(random.SystemRandom())
    with open('events.json') as fp:
        data = json.load(fp)
        questions = data
        random_index = random.choice(list(questions))
        event = questions[random_index]['description']
        effect = questions[random_index]['effect']
        key = questions[random_index]['key']
        value = questions[random_index]['value']
        to_change = var_dict[key][value]
        changed = to_change + effect
        var_dict[key][value] = changed
        write_game_config()
        return event


# testing out random conversations, or overheard conversations; will eventually have game world relevance
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


# class to handle the generation of new aides

class aide:
    def __init__(self):
        self.skills = []
        self.names = []
        self.prices = []
        self.skills_mult = []

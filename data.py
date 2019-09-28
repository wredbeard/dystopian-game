from json import load, dump


# load config file for reading
with open('config.json', 'r') as config_in_file:
    game_config = load(config_in_file)


# loads game events
with open('events.json', 'r') as game_events_file:
    game_event = load(game_events_file)


# load the book of laws
with open('laws.json', 'r') as laws_file:
    game_laws = load(laws_file)


# write changes to the config file
def game_config_write():
    with open('config.json', 'w') as config_out_file:
        dump(game_config, config_out_file)

from data import game_config, game_config_write
import textwrap


# a simple cross platform way of clearing the console screen
def screen_clear():
    print("\n" * 100)


#wraps long text
def wrd_wrp(str_to_wrap):
    print('\n'.join(textwrap.wrap(str_to_wrap, width=79, replace_whitespace=False)))


# resets values for a new game
def game_new_setup(player_name, player_title, player_party):
    game_config['player']['name'] = player_name
    game_config['player']['title'] = player_title
    game_config['player']['party'] = player_party


# persistent player status bar
def player_stats():
    stats_player_money = "\t\tMoney: " + str(game_config['player']['money'])
    stats_player_power = " Power: " + str(game_config['player']['power'])
    stats_player_lev = " Leverage: " + str(game_config['player']['leverage'])
    total_stats = stats_player_money + stats_player_power + stats_player_lev
    return total_stats


# exits and saves the game
def game_save_exit():
    game_config_write()
    return 0


# generates a report on population and their attitudes
def gen_report_populace():
    print("\nCurrent population: " + str(game_config['world']['population']))
    if game_config['world']['anger'] <= 20:
        print("\nThe people are currently: Complacent")
    elif 20 < game_config['world']['anger'] <= 50:
        print("\nThe people are currently: Agitated")
        wrd_wrp("\nIt may be a good idea to give the people limited freedoms or enact more forceful measures to bring"
                " them back in line.")
    elif 51 <= game_config['world']['anger'] <= 99:
        print("\nThe people are currently: Angry")
        wrd_wrp("\nIt is highly advised you take immediate action to pacify the people or bring them back in line.")
    else:
        pass
    print("\nPrisoner count: You currently have " + str(game_config['world']['prisoners']) + " at your disposal.")


# reports numbers of criminals and crimes
def gen_report_crime():
    wrd_wrp("\nOur 'aggregate' data tells us that there are around " + str(game_config['crime']['criminals']) + " active"
            " criminals at large.")
    print("\nWe have determined there were " + str(game_config['crime']['crimes_committed']) + "this year.")
    print("\nMurders: " + str(game_config['crime']['crimes']['murder']))
    print("\nBribes: " + str(game_config['crime']['crimes']['bribery']))
    print("\nThefts: " + str(game_config['crime']['crimes']['theft']))
    print("\nAs well as an estimated " + str(game_config['crime']['crimes']['other']) + " crimes we have not yet "
                                                                                        "made up.")

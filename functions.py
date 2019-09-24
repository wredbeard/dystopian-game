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

def gen_report_economy():
    wrd_wrp("\nWe currently have around " + str(game_config['economy']['businesses']) + " factories and farms"
            " under our thumb.")
    b_tax_percent = game_config['economy']['taxes']['b_tax'] * 100
    p_tax_percent = game_config['economy']['taxes']['p_tax'] * 100
    print("\nCurrent business tax rate: " + str(b_tax_percent))
    print("\nOur industries are currently exporting: ")
    print("\nHuman parts: " + str(game_config['economy']['exports']['human_parts']))
    print("\nMachines: " + str(game_config['economy']['exports']['machines']))
    print("\nAgriculture: " + str(game_config['economy']['exports']['agriculture']))
    print("\nTotal tax revenue from businesses: " + str(game_config['economy']['taxes']['b_rev']))
    print("\n------------------------------------")
    print("\nCurrent personal tax rate: " + str(p_tax_percent))
    print("\nRevenue from personal taxes: " + str(game_config['economy']['taxes']['p_rev']))


def gen_report_bank():
    out_interest = game_config['bank']['p_interest'] * game_config['bank']['total_funds']
    in_interest = game_config['bank']['i_interest'] * game_config['bank']['total_loaned']
    bank_revenue = in_interest - out_interest
    p_interest_rounded = game_config['bank']['p_interest'] * 100
    i_interest_rounded = game_config['bank']['i_interest'] * 100
    print("Current consumer interest rate: " + str(round(p_interest_rounded)))
    print("\nCurrent financing interest rate: " + str(round(i_interest_rounded)))
    print("\nTotal Assets: " + str(game_config['bank']['total_funds']))
    print("\nCurrent outgoing interest: " + str(round(out_interest)))
    print("\nCurrent incoming interest: " + str(round(in_interest)))
    print("\nThe National Bank Income: + " + str(round(bank_revenue)))



def bank_deposit():
    print("How much money would you like to deposit?")
    print("\nYou can deposit up to " + str(game_config['player']['money']))
    try:
        deposit_amount = int(input("\n\nSpecify amount > "))
        if deposit_amount > 0:
            if deposit_amount > game_config['player']['money']:
                print("You can not deposit more money than you have.")
                bank_deposit()
            elif deposit_amount <= game_config['player']['money']:
                game_config['bank']['p_money'] += deposit_amount
                game_config['player']['money'] -= deposit_amount
                game_config_write()
            else:
                print("I'm taking the day off...")
        else:
            print("You deposit nothing.")
    except:
        print("Do you think bankers have a sense of humor?")
        bank_deposit()

def bank_withdraw():
    print("How much would you like to withdraw? ")
    print("\nYou have " + str(game_config['bank']['p_money']) + " stored with us.")

    try:
        withdraw_amount = int(input("\n\nSpecify amount > "))
        if withdraw_amount > 0:
            if withdraw_amount > game_config['bank']['p_money']:
                print("You can not withdraw more money than you have.")
                bank_deposit()
            elif withdraw_amount <= game_config['bank']['p_money']:
                game_config['bank']['p_money'] -= withdraw_amount
                game_config['player']['money'] += withdraw_amount
                game_config_write()
            else:
                print("I'm taking the day off...")
        else:
            print("You withdraw nothing.")
    except:
        print("Do you think bankers have a sense of humor?")
        bank_deposit()


def bank_loan():
    pass


def bank_pay_loan():
    pass
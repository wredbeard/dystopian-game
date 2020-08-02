from data import game_config, game_config_write, game_laws, game_laws_write
import textwrap
import colors
import random
import os

color = colors.GameColors()


# simple seeded rng
def rand_gen(min_num, max_num):
    rand_seed = random.SystemRandom()
    random.seed(rand_seed)
    rand_return = random.randint(min_num, max_num)
    return rand_return


# a simple cross platform way of clearing the console screen
def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# wraps long text
def wrd_wrp(str_to_wrap):
    print('\n'.join(textwrap.wrap(str_to_wrap, width=79, replace_whitespace=False)))


# sets up new game
def game_new():
    game_population = rand_gen(1000000, 10000000)
    game_config['world']['population'] = game_population
    game_config['crime']['criminals'] = rand_gen(0, round(game_population * 0.01))
    game_config['economy']['businesses'] = rand_gen(round(game_population * 0.02), round(game_population * 0.03))
    game_config['bank']['funds'] = rand_gen(1000, 10000)
    game_config['bank']['p_money'] = rand_gen(10000, 100000)
    game_config['bank']['funds'] = rand_gen(1000000, 10000000)
    game_crime_handler()

# makes functions where something needs to be displayed to user prettier
def content_template(title, text):
    print("-" * len(title) * 2)
    print(title)
    print("-" * len(title) * 2)
    wrd_wrp(text)
    print("\n\n\n")


# resets values for a new game
def game_new_setup(player_name, player_title, player_party):
    game_config['player']['name'] = player_name
    game_config['player']['title'] = player_title
    game_config['player']['party'] = player_party
    game_config['player']['money'] = 10000
    game_config['player']['power'] = 10
    game_config['player']['leverage'] = 1
    game_config['player']['is_dead'] = False
    game_config['player']['turn'] = 0
    game_config['world']['growth_mod'] = 0.01
    game_config['world']['anger'] = 10
    game_config['world']['health'] = 50
    game_config['world']['revolting'] = False
    game_config['world']['prisoners'] = rand_gen(1000, 10000)
    game_config['world']['hunger'] = 0
    game_config['world']['religion'] = 10
    game_config['crime']['crimes_committed'] = 0
    game_config['crime']['crime_mod'] = 0.013
    game_config['economy']['prod_mod'] = 1.0
    game_config['economy']['taxes']['b_tax'] = 0.05
    game_config['economy']['taxes']['p_tax'] = 0.05
    game_config['bank']['p_interest'] = 0.05
    game_config['bank']['i_interest'] = 0.07
    game_config['bank']['loan'] = 0
    game_config_write()


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
    game_laws_write()
    game_law_effects()
    return 0

def turn_counter():
    game_config['player']['turn'] += 1

# turn handler
def game_end_turn():
    game_law_effects()
    game_crime_handler()
    turn_counter()

# handles crime on turn end and game start
def game_crime_handler():
    base_crime = game_config['crime']['criminals']
    game_config['crime']['crimes_committed'] = round(base_crime * .9)
    total_crime = round(game_config['crime']['crimes_committed'])
    game_config['crime']['crimes']['murder'] = rand_gen(0, total_crime)
    game_config['crime']['crimes']['bribery'] = rand_gen(0, total_crime)
    game_config['crime']['crimes']['theft'] = rand_gen(0, total_crime)
    game_config['crime']['crimes']['other'] = rand_gen(0, total_crime)


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
    print("\nWe have determined there were " + str(game_config['crime']['crimes_committed']) + " crimes this year.")
    print("\nMurders: " + str(game_config['crime']['crimes']['murder']))
    print("\nBribes: " + str(game_config['crime']['crimes']['bribery']))
    print("\nThefts: " + str(game_config['crime']['crimes']['theft']))
    print("\nAs well as an estimated " + str(game_config['crime']['crimes']['other']) + " crimes we have not yet "
                                                                                        "made up.")


# reports health of economy
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


# reports bank interest interest and income
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


# controls bank deposits
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
                game_config['bank']['total_funds'] += deposit_amount
                game_config_write()
            else:
                print("I'm taking the day off...")
        else:
            print("You deposit nothing.")
    except TypeError:
        print("Do you think bankers have a sense of humor?")
        bank_deposit()


# controls bank withdrawals
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
                game_config['bank']['total_funds'] -= withdraw_amount
                game_config_write()
            else:
                print("I'm taking the day off...")
        else:
            print("You withdraw nothing.")
    except TypeError:
        print("Do you think bankers have a sense of humor?")
        bank_deposit()


# take out loans
def bank_loan():
    loan_max = game_config['player']['money'] * 0.30
    if game_config['bank']['loan_out']:
        print("Please resolve your current loan before taking another.")
    else:
        print("\nMax loan amount: " + str(round(loan_max)))
        try:
            loan_requested = int(input("Please enter your desired loan amount. "))
            if loan_requested > loan_max:
                print("\nYou can not take more than the maximum loan.")
            elif loan_requested <= loan_max:
                print("\nLoan approved: " + str(loan_requested))
                game_config['bank']['loan'] = loan_requested
                game_config['player']['money'] += loan_requested
                game_config['bank']['loan_out'] = True
                game_config['bank']['total_loaned'] += loan_requested
            else:
                print("\nYou take no loan.")
                game_config_write()
        except TypeError:
            print("That's not a number.")
            bank_loan()


# pay back loans
def bank_pay_loan():
    if not game_config['bank']['loan_out']:
        print("You do not have any loans to pay.")
    else:
        print("\nOutstanding balance: " + str(game_config['bank']['loan']))
        try:
            loan_to_pay = int(input("\nHow much would you like to pay back? "))
            if loan_to_pay <= game_config['player']['money']:
                if loan_to_pay > game_config['bank']['loan']:
                    print("\nThat is more than your current balance.")
                    bank_pay_loan()
                elif loan_to_pay < game_config['bank']['loan']:
                    loan_new_balance = game_config['bank']['loan'] - loan_to_pay
                    game_config['player']['money'] -= loan_to_pay
                    game_config['bank']['loan'] -= loan_to_pay
                    game_config['bank']['total_loaned'] -= loan_to_pay
                    print("Your new balance is: " + str(loan_new_balance))
                elif loan_to_pay == game_config['bank']['loan']:
                    game_config['player']['money'] -= loan_to_pay
                    game_config['bank']['loan'] = 0
                    game_config['bank']['loan_out'] = False
                    game_config['bank']['total_loaned'] += loan_to_pay
                    print("\nYou have paid off your loan.")
                else:
                    print("\nYou pay nothing.")
                    game_config_write()
        except TypeError:
            print("\nI have not had enough coffee to deal with your 'ineptitude'.")


# key of category in laws.json is passed to handler to activate/deactivate laws
def law_activation_handler(law_cat):
    content_template(game_laws[law_cat]['title'], game_laws[law_cat]['desc'])
    law = {}
    for x in game_laws[law_cat]['laws']:
        law[x] = game_laws[law_cat]['laws'][x]['name']
        active = game_laws[law_cat]['laws'][x]['active']
        desc = game_laws[law_cat]['laws'][x]['desc']
        if active:
            print(x + "| " + law[x] + " - " + desc + color.GREEN + " - Active\n" + color.RESET, sep='\n')
        else:
            print(x + "| " + law[x] + " - " + desc + color.RED + " - Inactive\n" + color.RESET, sep='\n')
    choice = input(color.YELLOW + "\nWhich law would you like to change? Use 0 to exit >" + color.RESET)
    if choice == '0':
        pass
    elif choice not in game_laws[law_cat]['laws']:
        print("Not a valid law...")
        screen_clear()
        law_activation_handler(law_cat)
    else:
        law_change = game_laws[law_cat]['laws'][choice]['active']
        game_laws[law_cat]['laws'][choice]['active'] = not law_change
        screen_clear()
        law_activation_handler(law_cat)


def game_law_effects():
    pop_laws = game_laws['pop_laws']['laws']
    crime_laws = game_laws['crime_laws']['laws']
    economy_laws = game_laws['economy_laws']['laws']
    health_laws = game_laws['health_laws']['laws']

    # pop laws
    if pop_laws['1']['active']:
        game_config['crime']['criminals'] -= round(game_config['crime']['criminals'] * 0.1)
        if game_config['crime']['criminals'] <= 0:
            game_config['crime']['criminals'] = 0
    else:
        pass
    if pop_laws['2']['active']:
        game_config['crime']['criminals'] -= round(game_config['crime']['criminals'] * 0.05)
        if game_config['crime']['criminals'] <= 0:
            game_config['crime']['criminals'] = 0
    else:
        pass
    if pop_laws['3']['active']:
        game_config['crime']['criminals'] -= round(game_config['crime']['criminals'] * 0.1)
        if game_config['crime']['criminals'] <= 0:
            game_config['crime']['criminals'] = 0
    else:
        pass
    if pop_laws['4']['active']:
        game_config['crime']['criminals'] -= round(game_config['crime']['criminals'] * 0.01)
        if game_config['crime']['criminals'] <= 0:
            game_config['crime']['criminals'] = 0
    else:
        pass

    # crime laws
    if crime_laws['1']['active']:
        game_config['crime']['crimes']['murder'] -= round(game_config['crime']['crimes']['murder'] * 0.75)
        game_config['world']['population'] += round(game_config['world']['population'] * 0.0075)
        game_config['world']['anger'] -= 1
    else:
        pass
    if crime_laws['2']['active']:
        game_config['crime']['crimes']['theft'] -= round(game_config['crime']['crimes']['theft'] * 0.75)
    else:
        pass
    if crime_laws['3']['active']:
        game_config['crime']['crimes']['other'] -= round(game_config['crime']['crimes']['theft'] * 0.05)
    else:
        pass
    if crime_laws['4']['active']:
        game_config['crime']['crimes']['bribery'] -= round(game_config['crime']['crimes']['bribery'] * 0.75)
    else:
        pass
    if crime_laws['5']['active']:
        if game_config['world']['religion'] <= 0:
            pass
        else:
            game_config['world']['religion'] -= 1
    else:
        pass
    if crime_laws['6']['active']:
        game_config['world']['hunger'] -= round(100 * 0.20)
    else:
        pass

    # economy laws
    if economy_laws['1']['active']:
        game_config['economy']['p_tax'] = 0.07
    else:
        game_config['economy']['p_tax'] = 0.05
    if economy_laws['2']['active']:
        game_config['economy']['b_tax'] = 0.07
        game_config['economy']['prod_mod'] = .75
    else:
        game_config['economy']['b_tax'] = 0.05
    if economy_laws['3']['active']:
        game_config['economy']['prod_mod'] = 1.5
    else:
        pass
    if economy_laws['4']['active']:
        game_config['economy']['prod_mod'] = 1.6
        game_config['crime']['crime_mod'] = 0.007
        game_config['world']['anger'] -= 1
    else:
        pass

    # health laws
    if health_laws['1']['active']:
        game_config['world']['growth_mod'] = 0.02
    else:
        pass
    if health_laws['2']['active']:
        game_config['world']['growth_mod'] += 0.01
        if game_config['world']['health'] <= 100:
            game_config['world']['health'] += 1
    else:
        game_config['world']['growth_mod'] -= 0.01
    if health_laws['3']['active']:
        game_config['economy']['exports']['agriculture'] += 10
        game_config['world']['hunger'] -= round(100 * .01)
    else:
        pass
    if health_laws['4']['active']:
        game_config['economy']['prod_mod'] -= .02
        game_config['world']['health'] += round(100 * .01)
    else:
        pass



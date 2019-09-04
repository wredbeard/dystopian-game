import time
import os
import sys
import textwrap
import datagen
import random
from consolemenu import *
from colorama import init, Fore, Style

init()

my_player = datagen.var_dict['player']
my_party = datagen.var_dict['party']
my_rival = datagen.var_dict['rival']
my_aide = datagen.var_dict['aide']
my_world = datagen.var_dict['world']
the_bank = datagen.var_dict['bank']
laws = datagen.var_dict['laws']
aide_calc = datagen.aide()
rand_name = datagen.people_name_selector()
event_get = datagen.event_get


def prompt(selection_list, menu_title, pro_text):
    main_menu = SelectionMenu(selection_list, menu_title, None, None, None, pro_text, p_stats())
    main_menu.show()
    choice = main_menu.current_option
    return choice


# handle player input


# function to clear screen system independent


def scr_clr():
    os.system('cls' if os.name == 'nt' else 'clear')


# persistent status bar


def p_stats():
    ps0 = "\t\tPM:" + str(my_player['money'])
    ps1 = " PP:" + str(my_player['power'])
    ps2 = " PL:" + str(my_player['leverage'])
    ps3 = " PaM:" + str(my_party['funds'])
    ps4 = " PaP:" + str(my_party['power'])
    ps5 = " PaO:" + str(my_party['org'])
    ps6 = " Mems:" + str(my_party['membership'])
    ps7 = Fore.LIGHTBLUE_EX + ps0 + ps1 + ps2 + ps3 + ps4 + ps5 + ps6 + Style.RESET_ALL
    return ps7


# implementation of player suicide. its a dystopia after all.


def suicide():
    scr_clr()
    selection_list = ['1|Back Out', '2|Follow Through']
    choice = prompt(selection_list, "The Last Choice", "If you are feeling particularly weary you may exit the game"
                                                       " via suicide. This will have interesting effects on your next"
                                                       " playthrough.")
    if choice == 0:
        print(Style.RESET_ALL + "Good... The world is better with you around.")
        time.sleep(3)
        play_menu()
    elif choice == 1:
        print("I don't know why you made this choice. I can only assume your back was against the wall.")
        time.sleep(3)
        print("\nI would have understood if you had told me.")
        goodbye = "\n\n\nGoodbye, friend."
        for i in goodbye:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.4)
        time.sleep(5)
        return 0
    else:
        suicide()


# generates 3 aides to choose from


def aide_generator():
    aide_name = datagen.people_name_selector()
    aide_calc.names.append(aide_name)
    aide_calc.prices.append(random.randrange(90, 450))
    for i in aide_calc.prices:
        aide_calc.skills_mult = i * 0.3
    aide_calc.skills.append(round(aide_calc.skills_mult))


# resets config data
def clear_data():
    my_player['power'] = 5
    my_player['leverage'] = 0
    my_player['money'] = 1000
    my_player['is_dead'] = False
    my_party['power'] = 0
    my_party['funds'] = 0
    my_party['might'] = 0
    my_party['org'] = 0
    my_party['membership'] = 0
    my_rival['membership'] = 0
    my_rival['power'] = 100
    my_rival['might'] = 100
    my_rival['funds'] = 10000
    my_rival['is_dead'] = False
    the_bank['loan_out'] = False
    the_bank['funds'] = 0
    the_bank['loan'] = 0
    the_bank['p_money'] = 0
    the_bank['p_interest'] = 0.5
    the_bank['i_interest'] = 0.7
    my_aide['name'] = ''
    my_aide['is_dead'] = False
    my_world['population'] = 0


def new_game():
    scr_clr()
    clear_data()
    pop = datagen.gen_pop()
    my_world['population'] += pop
    datagen.membership_gen(pop)
    wordwrap("Welcome, everyone starts out here. You are the leader of your party. "
             "In order to continue to stay in power you must maintain your party's political power. "
             "You may enforce this whichever way you feel fit. As you progress you will "
             "gain more ways to keep and grow your power.")
    print("\n\nWhat is your title? Chairman, Senator, Leader, Lord\n")
    print("Remember that you will retain your title throughout the game so choose wisely.\n")
    print("Please enter your title:\n")
    choice1 = input(">")
    my_player['title'] = choice1
    os.system('clear')
    print("Okay, " + my_player['title'])
    my_player['name'] = input("\nAnd what is your name?: ")
    scr_clr()
    print(my_player['title'] + " " + my_player['name'] + ", please give a name to your political party")
    my_party['name'] = input("> ")
    os.system('clear')
    print("Your party name is " + my_party['name'])
    my_rival['party'] = datagen.party_name_selector()
    my_rival['name'] = rand_name
    print("Your opponents are The " + my_rival['party'] + " and their leader is " + my_rival['name'])
    print("\n\nYou have " + str(pop) + " hearts and minds to win before you can rule this country.")
    time.sleep(10)
    os.system('clear')
    datagen.write_game_config()
    play_menu()


def play_menu():
    scr_clr()
    selections = ['Manage Party', 'Personal Actions', 'Plan B', 'Law and Order', 'End Turn', 'Save Game']
    if my_party['power'] < 51:
        selections[3] = 'Law and Order - Not Available'
    choice = prompt(selections, 'Main Menu', 'Here are your current action choices')
    if choice == 0:
        manage_party_menu()
    elif choice == 1:
        actions_menu()
    elif choice == 4:
        end_turn()
    elif my_party['power'] == 51 and choice == 3:
        law_and_order()
    elif choice == 5:
        datagen.write_game_config()
    elif choice == 2:
        suicide()
    else:
        play_menu()


def manage_party_menu():
    scr_clr()
    selections = ['Manage Staff', 'Manage Campaign', 'Party Party', 'Main Menu']
    choice = prompt(selections, "Party Management", 'Here is where you manage your party.')
    if choice == 0:
        manage_staff_menu()
    elif choice == 1:
        manage_campaign_menu()
    elif choice == 2:
        manage_party_menu()
    elif choice == 3:
        play_menu()
    else:
        manage_party_menu()


def actions_menu():
    selections = ['Visit Bank', 'Walk the streets', '']
    choice = prompt(selections, 'Player Actions', 'Certain actions are available to you to control your own personal'
                                                  ' power and position.')
    if choice == 0:
        bank()
    if choice == 1:
        scr_clr()
        print("You have a random conversation.")
        print("\nSomeone says: " + datagen.random_conversation())
        time.sleep(5)
        actions_menu()
    if choice == 2:
        print("Not available yet. ")
        time.sleep(3)
        actions_menu()
    else:
        actions_menu()


def military_actions():
    print()


def law_and_order():
    print()


def manage_staff_menu():
    # handle the selection of staff
    scr_clr()
    if my_aide['name'] == '':
        aide_selector()
    else:
        print("Your current top aide is: " + my_aide['name'])
        selection = ['Meet With Aide', 'Fire Aide', 'Go Back']
        choice = prompt(selection, "Manage Aide", "Here you can arrange a meeting with your aide to gain valuable "
                                                  "insight on your party and government.")
        if choice == 0:
            aide_meeting()
        elif choice == 1:
            # dump character from the script
            print("You have fired your aide. It was probably for the best, right?")
            print("Your aide goes home. A loud bang is heard from the inside of the house.")
            time.sleep(5)
            my_aide['is_dead'] = True
            aide_death_routine()
        elif choice == 2:
            manage_party_menu()


def manage_campaign_menu():
    scr_clr()
    selection = ['Growth Options - Grow Party Membership', 'Funding Options - Tactics To Raise Money',
                 'Anti-Opponent - Damage Reputations, etc.']
    if my_aide['name'] == '':
        print("You need to pick an aide before you can access these options")
        time.sleep(3)
        manage_staff_menu()
    else:
        choice = prompt(selection, "Campaign Menu", "Here you can employ certain tactics to improve your party"
                                                    " power, raise money and reduce the popularity of opponents")
        if choice == 0:
            selection1 = ['Posters - Place posters in various locations - 50 PaM', 'Rally - Rally in the capitol square'
                                                                                   '- 500 PaM',
                          'Force Popularity - Have brutes "convince" people to see things your way - '
                          '1000 PaM', 'Go Back']
            choice1 = prompt(selection1, "Growth Actions", "You have several tactics at your disposal to grow"
                                                           " your party membership, these methods may not"
                                                           " always be effective. Their success depends on"
                                                           " several factors such as aide skill and current"
                                                           " membership")
            if choice1 == 0:
                scr_clr()
                prob = datagen.prob(1, 10) * 0.0000001
                prob2 = datagen.prob(1, 10) * 0.0000001
                pop = my_world['population']
                rival_mems_gained = round(prob2 * my_rival['membership'])
                gained = round(prob * pop)
                total_gain = gained + rival_mems_gained
                my_rival['membership'] -= rival_mems_gained
                my_party['membership'] += total_gain
                print("You've gained " + str(gained) + "members from the populace and " + str(rival_mems_gained) +
                      " from The " + my_rival['party'])
                time.sleep(5)
                manage_campaign_menu()
            else:
                manage_campaign_menu()


def aide_selector():
    scr_clr()
    p_stats()
    if my_aide['name'] == '':
        selections = ['Hire Aide', 'Nevermind']
        choice = prompt(selections, "Hire Aide?", "You currently have no Top Aide. Would you like to hire one?")
        if choice == 0:
            scr_clr()
            for _ in range(3):
                aide_generator()
            print("\nPick your Top Aide:\n")
            aide_1 = "1|Name: " + str(aide_calc.names[0]) + " at skill level " + str(aide_calc.skills[0]) + " for " + \
                     str(aide_calc.prices[0])
            aide_2 = "2|Name: " + str(aide_calc.names[1]) + " at skill level " + str(aide_calc.skills[1]) + " for " + \
                     str(aide_calc.prices[1])
            aide_3 = "3|Name: " + str(aide_calc.names[2]) + " at skill level " + str(aide_calc.skills[2]) + " for " + \
                     str(aide_calc.prices[2])
            selections = [aide_1, aide_2, aide_3]
            choice = prompt(selections, "Select Aide", "You may now pick a Top Aide. Remember that your Aide plays a "
                                                       "large role in your interactions."
                                                       "Having a skilled aide is important for"
                                                       " setting up meetings, political attacks, and certain "
                                                       "covert activities. You must have an aide to access staff menus")
            print()
            if choice == 0:
                if aide_calc.prices[0] > my_player['money']:
                    print("You can not afford this aide.")
                    aide_selector()
                my_aide['name'] = aide_calc.names[0]
                my_aide['skill'] = aide_calc.skills[0]
                my_player['money'] -= aide_calc.prices[0]
                manage_staff_menu()
            elif choice == 1:
                if aide_calc.prices[1] > my_player['money']:
                    print("You can not afford this aide.")
                    aide_selector()
                my_aide['name'] = aide_calc.names[1]
                my_aide['skill'] = aide_calc.skills[1]
                my_player['money'] -= aide_calc.prices[1]
                manage_staff_menu()
            elif choice == 2:
                if aide_calc.prices[2] > my_player['money']:
                    print("You can not afford this aide.")
                    aide_selector()
                my_aide['name'] = aide_calc.names[2]
                my_aide['skill'] = aide_calc.skills[2]
                my_player['money'] -= aide_calc.prices[2]
                manage_staff_menu()
            else:
                print("Nevermind, then")
                time.sleep(3)
                manage_party_menu()
        elif choice == 1:
            my_aide['name'] = ''
            manage_party_menu()
        else:
            aide_selector()


def aide_meeting():
    scr_clr()
    message_1 = "Hello, " + my_player['title'] + my_player['name']
    choice = prompt(['Advice', 'Do Some Work [-50 PM]', 'Go Back'], my_aide['name'], message_1)
    if choice == 0:
        if my_player['money'] < 1000:
            message_2 = "You should work on building your money"
        else:
            message_2 = "Things look good on money"
        prompt(['Thanks'], None, message_2)
        aide_meeting()
    if choice == 1:
        if my_player['money'] > 50:
            my_player['money'] -= 50
            e = datagen.random_event()
            print(e)
            time.sleep(3)
            aide_meeting()
        else:
            print("You can not afford this.")
            aide_meeting()
    if choice == 2:
        manage_staff_menu()


def aide_death_routine():
    if my_aide['is_dead'] is True:
        scr_clr()
        print("The Daily Piper is pleased to report the top aide from " + my_party['name'] + ", " + my_aide['name'] +
              "has died.")
        my_aide['name'] = ''
        time.sleep(3)
        play_menu()
    else:
        play_menu()


def rival_death_routine():
    if my_rival['is_dead'] is True:
        print("Your rival" + my_rival['name'] + 'has "mysteriously" died.')
        time.sleep(3)
    else:
        play_menu()
    print()


def wordwrap(s):
    print('\n'.join(textwrap.wrap(s, width=80, replace_whitespace=False)))


def ww(s):
    wrapped = textwrap.wrap(s, width=80, replace_whitespace=False)
    return wrapped


def read_game_config():
    play_menu()


def bank():
    # here we set up the banking feature of the game
    # setup variables
    interest = the_bank['p_interest']
    # variable created to display interest in percentage
    p_interest = interest * 100
    selections = ['Deposit', 'Withdraw', 'Take Loan', 'Pay Loan', 'Main Menu']
    # if player party has complete power or law enacted they can change the bank interest rate
    # lower amounts should create more income
    if my_party['power'] > 99 or laws['001'] is True:
        selections.append('Change Interest Rate')
    choice = prompt(selections, 'Welcome to The National Bank', 'The current customer'
                                                                ' interest rate is: ' + str(p_interest) + ' %')
    scr_clr()
    if choice == 0:
        # handle deposits
        try:
            scr_clr()
            print("How much would you like to deposit? You have " + str(my_player['money']))
            deposit = int(input(''))
            if deposit == 0:
                print("You deposit nothing.")
                time.sleep(3)
                bank()
            elif 0 < deposit <= my_player['money']:
                my_player['money'] = my_player['money'] - deposit
                the_bank['p_money'] = the_bank['p_money'] + deposit
                datagen.write_game_config()
                bank()
            else:
                print("You do not have the funds to do that.")
                bank()
        except ValueError:
            scr_clr()
            print("Funny joke...")
            time.sleep(3)
            bank()

    elif choice == 1:
        # handle withdrawals
        try:
            print("How much would you like to withdraw? You have " + str(the_bank['p_money']))
            withdraw = int(input(''))

            if withdraw == 0:
                print("You withdraw nothing")
                time.sleep(3)
                bank()
            elif 0 < withdraw <= my_player['money']:
                my_player['money'] = my_player['money'] + withdraw
                the_bank['p_money'] = the_bank['p_money'] - withdraw
                datagen.write_game_config()
                bank()
            else:
                print("You do not have the funds to do that.")
                bank()
        except ValueError:
            scr_clr()
            print('Funny joke...')
            time.sleep(3)
            bank()
    elif choice == 2:
        # handle issuing of loans
        if not the_bank['loan_out']:
            # get the bank's current institutional interest
            i_loan_interest = the_bank['i_interest']
            # total of players cash and bank holdings
            total_funds = my_player['money'] + the_bank['p_money']
            # set maximum loan at 30% of player total money
            max_loan = total_funds * 0.3
            # make the institutional interest easily readable
            pc_interest = i_loan_interest * 100
            scr_clr()
            # show player money and possible loan
            print("Your current cash: " + str(my_player['money']))
            print("\nYour current savings: " + str(the_bank['p_money']))
            wordwrap("\nGiven your current financial standing we can offer you a loan of " + str(
                round(max_loan)) + " at a rate"
                                   " of " + str(round(pc_interest)) + "%. Would you like to take out a loan?")
            l_choice = input("1 - Yes, 2 - No\n:")
            if l_choice == '1':
                scr_clr()
                print("We are pleased that you have chosen to take out a loan.")
                loan_amt = int(input("Please enter desired loan amount up to " + str(round(max_loan)) + ": "))
                try:
                    if loan_amt <= max_loan:
                        scr_clr()
                        print("Processing loan...")
                        the_bank['loan'] = loan_amt
                        the_bank['loan_out'] = True
                        datagen.write_game_config()
                        time.sleep(3)
                        scr_clr()
                        print("Thank you for your patronage.")
                        print("\n\nYour funds are immediately available for use!")
                        wordwrap("\n\nWARNING: FAILURE TO REMIT TO A CASH CHECK EQUALING OUTSTANDING LOANS WILL"
                                 " RESULT IN IMMEDIATE LIQUIDATION OF ACCOUNTS AND LIFE.")
                        time.sleep(10)
                        bank()
                    else:
                        print("\nThat's too much. We've already informed you how much you can take out.")
                        time.sleep(3)
                        bank()
                except ValueError:
                    print('That is not a number')
                    time.sleep(3)
                    bank()
            else:
                print("Maybe later then...")
                time.sleep(3)
                bank()
        else:
            print("Please come back when you have paid your current loan.")
            input("Press enter to continue...")
            bank()
    elif choice == 3:
        # handle payback of loans
        selection_list = ['Pay Back Loan', 'Go Back']
        choice1 = prompt(selection_list, "Pay Back Loan", "Your current loan is: " + str(the_bank['loan']))
        if choice1 == 0:
            scr_clr()
            print("Your loan currently stands at: " + str(the_bank['loan']))
            print('\n\nHow much would you like to pay back?')
            pay_loan = int(input("Pay back amt: "))
            try:
                if my_player['money'] >= pay_loan and pay_loan <= the_bank['loan']:
                    the_bank['loan'] -= pay_loan
                    my_player['money'] -= pay_loan
                    if the_bank['loan'] <= 0:
                        scr_clr()
                        the_bank['loan_out'] = False
                        print("Thank you for paying off your loan.")
                        time.sleep(3)
                        bank()
                    else:
                        print("Your remaining loan balance is " + str(the_bank['loan']))
                    bank()
                elif pay_loan > the_bank['loan']:
                    print("Your loan amount is not that much.")
                    time.sleep(3)
                    bank()
                else:
                    print("You do not have the money to do this.")
                    time.sleep(3)
                    bank()
            except TypeError:
                pass

    else:
        bank()


def vote():
    x = datagen.event_roll()
    if x > 50:
        my_party['lvote'] = 'pass'
    else:
        my_party['lvote'] = 'fail'
    return my_party['lvote']


def end_turn():
    loan_interest()
    player_interest()
    print("---------------"
          "\nYou"
          "\n---------------")
    my_player['turn'] = my_player['turn'] + + 1
    if my_player['power'] <= 0:
        wordwrap("Unfortunately, it appears your political apparatus has run out of steam. You have zero power."
                 "Your destiny may be to roam the streets destitute. Or perhaps you'll be sent in for... reconditioning"
                 "What is certain, however, is that you are nothing to this world anymore.")
        time.sleep(3)
        wordwrap("You have lost the game. You may reload your last save or start a new game.")
        prompt(['This was all a dream', 'Death is surely a just end to the powerless.'], "You ran out of power.", None)
    if my_player['power'] >= 100:
        wordwrap("Congratulations, you've reached the point of ultimate power 'within the context of your government'. "
                 "You are in total control of your"
                 " government and can now pursue all political and military actions. A new menu has been opened to you."
                 " This menu contains additional powers at your disposal to create and maintain order. While supreme"
                 " leader is a great position to be in, we would like to warn you that resistance, secret orders, and "
                 " new political parties may seek to unseat you and if left unchecked will certainly do so!")
    if my_player['power'] >= 1000:
        wordwrap("Mysterious forces have been at work propelling you beyond what you thought possible. Only the most "
                 "powerful of opposition could stop you now. Be aware that those forces have gained strength with you. "
                 "You now have the powers of a supreme being. We implore you to consider all actions you take from this"
                 " point on with great care. A world with no one to govern is not a world at all. With no struggle "
                 "comes no satisfaction. Surely the end of times is near. Do what you will, but the judgement of the "
                 "universe comes with strong consequence.")
    if my_player['money'] <= 500:
        wordwrap("\n-Your personal wealth is not looking good. It is believed those who can not maintain their wealth"
                 "quickly lose their power as well.")
    if 500 < my_player['money'] < 10000:
        wordwrap("\n-Personal wealth is looking okay. You should seek to acquire more of it.")
    if my_player['money'] >= 10000:
        wordwrap("\n-You have plenty of money. Why not put it to work for you?")
    if 10 <= my_player['leverage'] <= 20:
        wordwrap("\n-You have enough leverage to 'undermine' those of lower power. Whatever that means to you.")
    if my_player['leverage'] > 20:
        wordwrap("\n-You have enough leverage to unseat a major official.")
    print("---------------"
          "\nYour Party"
          "\n---------------")
    if my_party['power'] <= 10:
        print("\n-Your party is quite weak. You may be crushed by your opponents.")
    if 10 <= my_party['power'] <= 50:
        print("\n-Your party power is okay. But okay is all they are saying about your party.")
    if 50 < my_party['power'] < 100:
        print("Your party is dominating the national congress.")
    if my_party['power'] >= 100:
        print("Your party has reached supreme power within the national congress.")
    datagen.write_game_config()
    input("Press any key to continue...")
    play_menu()


def loan_interest():
    if the_bank['loan_out']:
        interest_gained = the_bank['loan'] * the_bank['i_interest']
        round(interest_gained)
        the_bank['loan'] += interest_gained
    else:
        pass


def player_interest():
    if the_bank['p_money'] > 0:
        interest_gained = the_bank['p_money'] * the_bank['p_interest']
        round(interest_gained)
        the_bank['p_money'] += interest_gained
    else:
        pass


if __name__ == "__main__":
    play_menu()

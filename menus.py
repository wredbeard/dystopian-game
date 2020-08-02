import functions
import colors
import time
from functions import wrd_wrp as ww

color = colors.GameColors()
console_width = 79


def game_new_menu():
    functions.screen_clear()
    functions.game_new()
    print("-" * console_width + color.YELLOW)
    print("Welcome to Dystopia")
    print("-" * console_width)
    print("Due to the unfortunate and untimely demise of the previous Prime Minister, We've been tasked with setting"
          " you up as his replacement.")
    player_name = input("\n\n\nWhat was your name again? ")
    functions.screen_clear()
    ww("Oh yeah. You'd think I would remember the name of all of the new leaders but for some reason "
       "they never seem to stick around after becoming Minister. I'm sure you will though...")
    ww("\n\n As acting Minister, you may select a new title for yourself. It's been Minister for as "
       "long as I can remember but I think that's just because the title conveys power. You can call "
       "yourself a Lord or Chancellor or whatever you think is fitting of your position")
    player_title = input("\n\n\n Tell me, what would you prefer your title to be? ")
    functions.screen_clear()
    print("Okay, " + player_title + " " + player_name + ", The Party has just been called 'The Party' for as long as"
                                                        " I can remember.")
    player_party = input("\n\n\n What would you prefer we call your party? The... what? ")
    functions.screen_clear()
    print("Not the name I would have picked. " + player_party + " it is." + color.RESET)
    time.sleep(5)
    functions.game_new_setup(player_name, player_title, player_party)
    game_play_menu()


def prompt(prompt_selections, prompt_title, prompt_text):
    functions.screen_clear()
    stats_bar_length = functions.player_stats()
    print(functions.player_stats())
    print("-" * len(stats_bar_length))
    print(prompt_title)
    print("-" * len(stats_bar_length))
    ww("\n" + prompt_text)
    print(*prompt_selections, sep='\n')
    prompt_choice = input("> ")
    return prompt_choice


def prompt_simple(prompt_title, prompt_text):
    functions.screen_clear()
    print("-" * len(prompt_title))
    print(prompt_title)
    print("-" * len(prompt_title))
    ww("\n" + prompt_text)


def game_play_menu():
    prompt_selections = ['1|Read Reports', '2|Modify Laws', '3|Secret Police', '4|Personal Stuff', '5|Issue Orders',
                         '6|Ministries', '7|The National Bank', '8|End Turn', '9|Exit Game']
    choice = prompt(prompt_selections, "Main Menu", "This is your desk. You may execute all of the actions within your"
                                                    " power from here.\n")
    if choice == '1':
        menu_reports()
    elif choice == '2':
        menu_laws()
    elif choice == '3':
        menu_police()
    elif choice == '4':
        menu_personal()
    elif choice == '5':
        menu_orders()
    elif choice == '6':
        menu_ministries()
    elif choice == '7':
        menu_bank()
    elif choice == '8':
        functions.game_end_turn()
        game_play_menu()
    elif choice == '9':
        functions.screen_clear()
        print("Your game is automatically saved...")
        time.sleep(5)
        functions.game_save_exit()
    else:
        game_play_menu()


def menu_reports():
    selections = ['1|Populace Report', '2|Crime Report', '3|Economic Report', '4|Bank Report', '5|Exit']
    choice = prompt(selections, "Reports Menu", "Here you can read reports about the status of our nation. Use it "
                                                "to make important decisions.")
    if choice == '1':
        menu_reports_populace()
    elif choice == '2':
        menu_reports_crime()
    elif choice == '3':
        menu_reports_economy()
    elif choice == '4':
        menu_reports_bank()
    else:
        game_play_menu()


def menu_reports_populace():
    functions.screen_clear()
    prompt_simple("Populace Reports", "General information about the populace of our country.")
    functions.gen_report_populace()
    input("\n\nPress ENTER to close report")
    menu_reports()


def menu_reports_crime():
    functions.screen_clear()
    prompt_simple("Crime Report", "Information about criminal activities in our country.")
    functions.gen_report_crime()
    input("\n\nPress ENTER to close report")
    menu_reports()


def menu_reports_economy():
    functions.screen_clear()
    prompt_simple("Economic Report", "Information about the health of our economy.")
    functions.gen_report_economy()
    input("\n\nPress ENTER to close report")
    menu_reports()


def menu_reports_bank():
    functions.screen_clear()
    prompt_simple("Bank Report", "Information about current interest rates and revenues collected by The National Bank")
    functions.gen_report_bank()
    input("\n\nPress ENTER to close report")
    menu_reports()


def menu_laws():
    functions.screen_clear()
    selections = ['1|Public Order', '2|Criminal', '3|Economic', '4|Health And Safety', '5|Go Back']
    choice = prompt(selections, "Laws Menu", "Here you may enact and retract laws with varying "
                                             "effects on your country,"
                                             " industry, and population.")
    if choice == '1':
        menu_laws_public()
    elif choice == '2':
        menu_laws_crime()
    elif choice == '3':
        menu_laws_economy()
    elif choice == '4':
        menu_laws_health()
    elif choice == '5':
        game_play_menu()
    else:
        menu_laws()


def menu_laws_public():
    functions.screen_clear()
    functions.law_activation_handler('pop_laws')
    menu_laws()


def menu_laws_crime():
    functions.screen_clear()
    functions.law_activation_handler('crime_laws')
    menu_laws()


def menu_laws_economy():
    functions.screen_clear()
    functions.law_activation_handler("economy_laws")
    menu_laws()


def menu_laws_health():
    functions.screen_clear()
    functions.law_activation_handler("health_laws")
    menu_laws()


def menu_police():
    print('NOT AVAILABLE')
    game_play_menu()


def menu_personal():
    print('NOT AVAILABLE')
    game_play_menu()


def menu_orders():
    print('NOT AVAILABLE')
    game_play_menu()

def menu_ministries():
    print('NOT AVAILABLE')
    game_play_menu()


def menu_bank():
    selections = ['1|Deposit', '2|Withdraw', '3|Take Loan', '4|Pay Back Loan', '5|Exit']
    choice = prompt(selections, "The National Bank", "This is The National Bank. You may place treasury funds in here"
                                                     " to gain interest. You may also take out loans on behalf of the"
                                                     " government. However, do not step on the toes of The National"
                                                     " Bank. One might say they hold more power than you do.")
    if choice == "1":
        functions.screen_clear()
        functions.bank_deposit()
        time.sleep(3)
        menu_bank()
    elif choice == '2':
        functions.screen_clear()
        functions.bank_withdraw()
        time.sleep(3)
        menu_bank()
    elif choice == '3':
        functions.screen_clear()
        functions.bank_loan()
        time.sleep(3)
        menu_bank()
    elif choice == '4':
        functions.screen_clear()
        functions.bank_pay_loan()
        time.sleep(3)
        menu_bank()
    elif choice == '5':
        game_play_menu()
    else:
        menu_bank()


def game_settings_menu():
    print('')

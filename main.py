from functions import new_game, read_game_config, scr_clr

def main():
    scr_clr()
    print("Welcome to Dystopia")
    print("\n----------------")
    print("Main Menu")
    print("----------------\n")
    print("1 - New Game\n")
    print("2 - Load Game\n")
    print("3 - Exit\n")
    choice = input("Enter desired command number and press ENTER: ")
    if choice == '1':
        new_game()
    elif choice == '2':
        read_game_config()
    elif choice == '3':
        print("settings")
    else:
        main()

main()


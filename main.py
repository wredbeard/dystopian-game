import menus

def main_menu():
    selections = ['1|New Game', '2|Continue Game', '3|Settings', '4|Exit']
    print(*selections, sep='\n')
    choice = input("\n\n\n> ")
    if choice == '1':
        menus.game_new_menu()
    if choice == '2':
        menus.game_play_menu()
    if choice == '3':
        menus.game_settings_menu()
    else:
        return 0

main_menu()
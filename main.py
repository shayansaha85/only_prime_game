import os
import game_function as gf
from score_analysis import winner_declare, name_score_group_creator
import intro_window as iw
import helptext as ht

ans = 'y'

while ans.lower() == 'y':
    os.system('cls')
    k = iw.introWindow()

    if k == '1':
        print('ONLY PRIMES')
        print('------------')
        database = {}
        w = 'y'
        while w.lower() == 'y':

            print('CHOOSE YOUR OPTION:')
            print('1. SINGLE PLAYER MODE')
            print('2. MULTIPLAYER MODE')
            player_number = 'a'
            while not str(player_number).isdecimal():
                try:
                    player_number = int(input('>> '))
                except ValueError:
                    print('INCORRECT VALUE. ENTER AN INTEGER')
            os.system('cls')
            if player_number == 1:
                name_of_player = input('ENTER YOUR NAME : ')
                single_player_score = gf.enterPrime()
                os.system('cls')
                print(f'{name_of_player.upper()}, YOUR SCORE IS : {single_player_score}')
                w = 2
            elif player_number == 2:
                player_qty = 'a'
                while not str(player_qty).isdecimal():
                    try:
                        player_qty = int(input('HOW MANY PLAYERS? : '))
                    except ValueError:
                        print('INCORRECT VALUE. ENTER AN INTEGER')

                os.system('cls')
                i = 0
                player_names = []
                player_score = []
                print('ENTER PLAYER NAMES')
                print('------------------------')
                while i < player_qty:
                    name = input(f'PLAYER {i + 1} : ')
                    player_names.append(name)
                    i = i + 1
                os.system('cls')
                k = 0
                while k < player_qty:
                    print()
                    print(f'{player_names[k].upper()}\'S TURN')
                    score = gf.enterPrime()
                    player_score.append(score)
                    database[player_names[k].upper()] = player_score[k]
                    k = k + 1
                    os.system('cls')
                print('SCORE BOARD')
                print('---------------------------------------')
                print('PLAYER'.ljust(15), '|'.ljust(15), 'SCORE')
                print('---------------------------------------')
                for key, value in database.items():
                    print(key.ljust(15), '|'.ljust(15), value)
                print('---------------------------------------')
                print()
                winner_declare(name_score_group_creator(player_names, player_score))
                print()
                w = input('DO YOU WANT TO GO BACK TO MAIN MENU? (y/n) : ')
                if w.lower() == 'n':
                    break
            else:
                os.system('cls')
                print('INCORRECT INPUT. ENTER YOUR CHOICE AGAIN')
    elif k == '2':
        ht.helpText()
        ans = input('DO YOU WANT TO GO BACK TO MAIN MENU? (y/n) : ')
    elif k == '3':
        os.system('cls')
        print('THANKS FOR VISITING OUR GAME')
        break
    else:
        print('WRONG ENTRY')
        ans = input('DO YOU WANT TO GO BACK TO MAIN MENU? (y/n) : ')

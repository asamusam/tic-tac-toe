from classes.game import *

print()
print('Welcome!')
print()
print('Choose difficulty:')
print('– easy (1)')
print('– medium (2)')
print('– hard (3)')
print()
level = input('> ')

while level not in ['1', '2', '3']:
    print('Please, choose difficulty: 1, 2, or 3?')
    level = input('> ')

if level == '1':
    field = BattleField()
    field.show_battlefield()
    crosses = Player('Crosses', bcolors.FAIL + 'X' + bcolors.ENDC)
    zeroes = Easy('Zeroes', bcolors.OKBLUE + 'O' + bcolors.ENDC)
elif level == '2':
    field = BattleField()
    field.show_battlefield()
    crosses = Player('Crosses', bcolors.FAIL + 'X' + bcolors.ENDC)
    zeroes = Medium('Zeroes', bcolors.OKBLUE + 'O' + bcolors.ENDC)
elif level == '3':
    field = BattleField()
    field.show_battlefield()
    crosses = Player('Crosses', bcolors.FAIL + 'X' + bcolors.ENDC)
    zeroes = Hard('Zeroes', bcolors.OKBLUE + 'O' + bcolors.ENDC)

players = [crosses, zeroes]
turns = [0, 1] * 5
turn = 0
result = ''

print('Choose a cell to put a cross in.')
print('To exit the game, type "stop".')
print()

for cell in field.cells_content:

    while result == '' and field.empty_cells():

        try:
            
            choice = ''
            if turns[turn] == 0:
                choice = players[turns[turn]].choose_cell()
            else:
                print(bcolors.BOLD + f'{players[turns[turn]].name}: ' + bcolors.ENDC)
                choice = players[turns[turn]].choose_cell(
                                                        field.empty_cells(), 
                                                        players[turns[turn+1]].choices, 
                                                        players[turns[turn+1]].win_combs
                                                        )

            if choice == 'stop':
                result = bcolors.OKCYAN + f'{players[turns[turn]].name} have interrupted the game.' + bcolors.ENDC

            elif choice not in players[turns[turn]].choices and choice not in players[turns[turn+1]].choices:

                # put a cross or a zero in the chosen cell
                field.cells_content[int(choice)-1] = players[turns[turn]].symbol
                players[turns[turn]].choices.append(choice)

                # remove affected winning combinations of the rival
                players[turns[turn+1]].take_damage(choice)

                # check if the game is over
                result = players[turns[turn]].check_gameover()

                turn += 1

            else:
                print(bcolors.WARNING + 'Please, choose an empty cell.' + bcolors.ENDC)
                continue

        except:
            empty_cells = field.empty_cells()
            print(bcolors.WARNING + 'Type in one of the digits:', str(empty_cells) + bcolors.ENDC)
            continue

        field.show_battlefield()

if result == '':
    print(bcolors.BOLD + bcolors.OKCYAN + 'Draw.' + bcolors.ENDC)
    print()
else:
    print(bcolors.BOLD + result + bcolors.ENDC)
    print()
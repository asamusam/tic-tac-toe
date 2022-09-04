import itertools
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class BattleField:

    def __init__(self):
        self.cells_content = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def show_battlefield(self):
        print()
        print(f' {self.cells_content[0]} | {self.cells_content[1]} | {self.cells_content[2]} ')
        print('--- --- ---')
        print(f' {self.cells_content[3]} | {self.cells_content[4]} | {self.cells_content[5]} ')
        print('--- --- ---')
        print(f' {self.cells_content[6]} | {self.cells_content[7]} | {self.cells_content[8]} ')
        print()

    def empty_cells(self):
        empty_cells = []
        for cell in self.cells_content:
            if cell != '\033[91mX\033[0m' and cell != '\033[94mO\033[0m':
                empty_cells.append(cell)
        return empty_cells


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.win_combs = [
                    ('1','2','3'),
                    ('3','5','7'), 
                    ('4','5','6'), 
                    ('7','8','9'), 
                    ('1','4','7'), 
                    ('2','5','8'), 
                    ('1','5','9'), 
                    ('3','6','9')
                    ]
        self.choices = []

    def choose_cell(self):
        choice = input(bcolors.BOLD + f'{self.name}: ' + bcolors.ENDC)
        return choice

    def take_damage(self, choice):
        win_combs_to_remove = []
        for combination in self.win_combs:
            if choice in combination:
                win_combs_to_remove.append(combination)
        for x in win_combs_to_remove:
            self.win_combs.remove(x)

    def check_gameover(self):
        combinations = [i for i in itertools.permutations(self.choices, 3)]
        result = ''
        for comb in combinations:
            if comb in self.win_combs:
                result = bcolors.OKGREEN + f'{self.name} win.' + bcolors.ENDC
                break
        return result


class Hard(Player):

    def choose_cell(self, cells, moves, wincombs):

        # check for winning moves
        my_wins = []
        for cell in cells:
            self.choices.append(cell)
            combs = [i for i in itertools.permutations(self.choices, 3)]
            for comb in combs:
                if comb in self.win_combs:
                    my_wins.append(cell)
            self.choices.pop()

        # check for the rival's winning moves
        rival_wins = []
        for cell in cells:
            moves.append(cell)
            combs = [i for i in itertools.permutations(moves, 3)]
            for comb in combs:
                if comb in wincombs:
                    rival_wins.append(cell)
            moves.pop()
       
        # find the best move
        win_combs = ''.join([''.join(x) for x in self.win_combs])
        best_moves = []
        for cell in cells:
            weight = win_combs.count(cell)
            best_moves.append((weight, cell))
        best_move = max(best_moves)[1]

        if my_wins:
            choice = random.choice(my_wins)
        elif rival_wins:
            choice = random.choice(rival_wins)
        else:
            choice = best_move
        
        return choice

        
class Medium(Player):        

    def choose_cell(self, cells, moves, wincombs):

        # check for winning moves
        my_wins = []
        for cell in cells:
            self.choices.append(cell)
            combs = [i for i in itertools.permutations(self.choices, 3)]
            for comb in combs:
                if comb in self.win_combs:
                    my_wins.append(cell)
            self.choices.pop()

        # check for the rival's winning moves
        rival_wins = []
        for cell in cells:
            moves.append(cell)
            combs = [i for i in itertools.permutations(moves, 3)]
            for comb in combs:
                if comb in wincombs:
                    rival_wins.append(cell)
            moves.pop()

        if my_wins:
            choice = random.choice(my_wins)
        elif rival_wins:
            choice = random.choice(rival_wins)
        else:
            choice = random.choice(cells)

        return choice


class Easy(Player):        

    def choose_cell(self, cells, moves, wincombs):

        # check for winning moves
        my_wins = []
        for cell in cells:
            self.choices.append(cell)
            combs = [i for i in itertools.permutations(self.choices, 3)]
            for comb in combs:
                if comb in self.win_combs:
                    my_wins.append(cell)
            self.choices.pop()

        if my_wins:
            choice = random.choice(my_wins)
        else:
            choice = random.choice(cells)

        return choice
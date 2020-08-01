import itertools
from colorama import Fore, Back, Style, init
init()
    
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied ! Choose Another !")
            return False
        print("   "+"  ".join(str(i) for i in range(len(game_map))))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + 'X' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + 'O' + Style.RESET_ALL
            print(count, colored_row)
        return game_map
    except IndexError as e:
        print("Error: please enter row/column value as 0, 1 or 2.", e)
        return False
    except Exception as e:
        print("Someting went very very wrong !!!", e)
        return False


def win(game_map):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        return False

    # Horizontal
    for row in game_map:
        print(row)
        if all_same(row) :
            print(f"Player {row[0]} is the Winner!!! horizontally")
            return True
    
    # Vertical
    for col in range(len(game)):
        check = []
        for row in game_map:
            check.append(row[col])
        if all_same(check) :
            print(f"Player {check[0]} is the Winner!!! vertically")
            return True

    # Diagonal
    diag = []
    for col, row in enumerate(reversed(range(len(game_map)))):
        diag.append(game_map[row][col])
    if all_same(diag) :
            print(f"Player {diag[0]} is the Winner!!! diagonally (/)")
            return True
    
    diag = []
    for ind in range(len(game_map)):
        diag.append(game_map[ind][ind])
    if all_same(diag) :
            print(f"Player {diag[0]} is the Winner!!! diagonally (\\)")
            return True

    return False

play = True
players = [1,2]
while play:
    
    game_size = int(input("What size of tic-tac-toe you wanna play ? : "))

    game = [[0 for i in range(game_size)] for i in range(game_size)]
            
    game_won = False
    player_cycle = itertools.cycle(players)
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Player : {current_player}")
            row_choice = int(input("Enter row move (0,1,2) : "))
            column_choice = int(input("Enter column move (0,1,2) : "))            
            played = game_board(game, current_player, row=row_choice, column=column_choice)
            
        if win(game):
            game_won = True
            again = input("Game Over ! Do you wanna play again ? (y/n) : ")
            if again.lower() == "y":
                print("Restarting Game ..........")
            elif again.lower() == "n":
                print("Byeee!!!")
                play = False
            else:
                print("Not a valid answer ! See you later .....")
                play = False





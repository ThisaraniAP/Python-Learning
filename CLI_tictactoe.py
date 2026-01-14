board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

def print_board(board):
    print('\n')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        print_board(board)

        print("\nIt's " + turn + "'s turn, where would you like to put your " + turn + "? ")
        move = input()

        while move not in board.keys() or board[move] != ' ':
            print("Invalid move. Choose an empty space from 1-9.")
            move = input()

        board[move] = turn
        count += 1

        if count >= 5:
            if (board['7'] == board['8'] == board['9'] != ' ') or \
               (board['4'] == board['5'] == board['6'] != ' ') or \
               (board['1'] == board['2'] == board['3'] != ' ') or \
               (board['7'] == board['4'] == board['1'] != ' ') or \
               (board['8'] == board['5'] == board['2'] != ' ') or \
               (board['9'] == board['6'] == board['3'] != ' ') or \
               (board['7'] == board['5'] == board['3'] != ' ') or \
               (board['9'] == board['5'] == board['1'] != ' '):
                print_board(board)
                print("\nGame Over.")
                print(" ~~~ " + turn + " won. ~~~ ")
                break
        
        if count == 9:
            print_board(board)
            print("\nGame Over.")
            print(" ~~~ It's a Tie! ~~~ ")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

print("Welcome to Tic Tac Toe!")
print("Player 1 is X and Player 2 is O")
print("Enter numbers 1-9 to place your mark as per the grid below:")
print("\t7|8|9")
print("\t4|5|6")
print("\t1|2|3\n")
print("Let's start the game!\n")
game()

while True:
    print("\nDo you want to play again? (y/n)")
    ans = input().lower()
    if ans == 'y':
        for key in board.keys():
            board[key] = ' '
        game()
    elif ans == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
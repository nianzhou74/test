# Author: 叶航, 72510086, nianzhou74
# Reviewer1: 焦子恩 72510234，6791150
def is_win(game):
    # Check rows
     for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != ' ':
            return True
    # Check columns
    for j in range(3):
        if game[0][j] == game[1][j] == game[2][j] != ' ':
            return True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return True
    return False

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = 0  # 0 for player 1's turn, 1 for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        current_player = 'X' if turn == 0 else 'O'
        if not turn:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        if 0 <= i < 3 and 0 <= j < 3 and game[i][j] == ' ':
                return i, j
            else:
                print("Invalid move. Try again.")
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        if is_win(game):
            print(f"Player {turn+1} wins!")
            break  # Terminate the game
        turn = 1 - turn    # switch turn
        if n == 8:  # All cells have been filled
            print("Tie!")
        # Show the game board 
        for row in game:
            print(" ".join(row))

if __name__ == "__main__":
    main()

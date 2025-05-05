# Write code for tic tac toe
# 1. Create a 3x3 board
# 2. Allow two players to take turns
# 3. Check for a win or a draw
# 4. Display the board after each move
# 5. Allow players to choose their symbols (X or O)
# 6. Allow players to choose their starting player
# 7. Allow players to choose the position of their move
# 8. Allow players to choose to play again
# 9. Allow players to choose to quit the game
# 10. Allow players to choose to reset the game
# 11. Allow players to choose to save the game
# 12. Allow players to choose to load the game
# Print the invalid input message if the input is invalid
# 13. Print the game over message
# print the winner

import os
import pickle

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, symbol):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError
            return divmod(move, 3)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def save_game(board, current_player, player_symbols):
    with open("tic_tac_toe_save.pkl", "wb") as f:
        pickle.dump((board, current_player, player_symbols), f)
    print("Game saved!")

def load_game():
    try:
        with open("tic_tac_toe_save.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No saved game found.")
        return None, None, None

def reset_game():
    return create_board(), 0, {"Player 1": "X", "Player 2": "O"}

def main():
    print("Welcome to Tic Tac Toe!")
    board, current_player, player_symbols = reset_game()

    while True:
        if not board:
            board, current_player, player_symbols = reset_game()

        display_board(board)
        print(f"{list(player_symbols.keys())[current_player]}'s turn ({list(player_symbols.values())[current_player]})")

        print("Options: [1] Make a move [2] Save game [3] Load game [4] Reset game [5] Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                row, col = get_move()
                if board[row][col] == " ":
                    board[row][col] = list(player_symbols.values())[current_player]
                    break
                else:
                    print("Invalid move. The cell is already occupied.")
            if check_winner(board, list(player_symbols.values())[current_player]):
                display_board(board)
                print(f"{list(player_symbols.keys())[current_player]} wins!")
                board, current_player, player_symbols = reset_game()
            elif is_draw(board):
                display_board(board)
                print("It's a draw!")
                board, current_player, player_symbols = reset_game()
            else:
                current_player = 1 - current_player
        elif choice == "2":
            save_game(board, current_player, player_symbols)
        elif choice == "3":
            board, current_player, player_symbols = load_game()
            if not board:
                board, current_player, player_symbols = reset_game()
        elif choice == "4":
            board, current_player, player_symbols = reset_game()
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
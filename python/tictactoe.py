# This is a graphical Tic-Tac-Toe game using the tkinter library.

import tkinter as tk
from tkinter import messagebox

class TicTacToeGame(tk.Tk):
    """
    A graphical Tic-Tac-Toe game application.
    """
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        # Increased geometry to accommodate larger buttons and a new button
        self.geometry("450x550")
        self.resizable(False, False)

        # Game state variables
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.score_x = 0
        self.score_o = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        """
        Creates all the GUI elements for the game.
        """
        # Create a frame to hold the buttons with a black background for visible lines
        board_frame = tk.Frame(self, bg="black")
        board_frame.pack(pady=10)

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                # Increased button size for better clickability
                button = tk.Button(board_frame, text=" ", font=('Arial', 32, 'bold'), 
                                   width=3, height=1,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                # Use padx and pady to create the visible black lines
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)
            
        self.status_label = tk.Label(self, text=f"Player {self.current_player}'s turn", 
                                     font=('Arial', 18))
        self.status_label.pack(pady=(10, 5))

        self.score_label = tk.Label(self, text=f"Score: X: {self.score_x} | O: {self.score_o}",
                                    font=('Arial', 18))
        self.score_label.pack(pady=(5, 10))

        # Create a new frame for control buttons
        control_frame = tk.Frame(self)
        control_frame.pack(pady=5)
        
        # New "Play Again" button
        self.play_again_button = tk.Button(control_frame, text="Play Again", command=self.reset_game, 
                                           state=tk.DISABLED, font=('Arial', 14))
        self.play_again_button.pack(side=tk.LEFT, padx=5)

        # New "Reset Score" button
        self.reset_score_button = tk.Button(control_frame, text="Reset Score", command=self.reset_score,
                                            font=('Arial', 14))
        self.reset_score_button.pack(side=tk.RIGHT, padx=5)

    def handle_click(self, row, col):
        """
        Handles a player's move when they click a button.
        """
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED, 
                                          disabledforeground="black")
            
            if self.check_win():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                if self.current_player == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1
                self.score_label.config(text=f"Score: X: {self.score_x} | O: {self.score_o}")
                self.disable_all_buttons()
                self.play_again_button.config(state=tk.NORMAL) # Enable play again button on win
            elif self.is_board_full():
                self.status_label.config(text="It's a tie!")
                # Auto-reset on tie after a small delay
                self.after(1000, self.reset_game)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_win(self):
        """
        Checks all possible win conditions (rows, columns, and diagonals).
        """
        player = self.current_player
        # Check rows
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False
        
    def is_board_full(self):
        """
        Checks if the board is completely filled.
        """
        return all(self.board[row][col] != " " for row in range(3) for col in range(3))
        
    def disable_all_buttons(self):
        """
        Disables all buttons on the board.
        """
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)
                
    def reset_game(self):
        """
        Resets the game to its initial state.
        """
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.status_label.config(text=f"Player {self.current_player}'s turn")
        self.play_again_button.config(state=tk.DISABLED)
        
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", state=tk.NORMAL)

    def reset_score(self):
        """
        Resets the scores for both players to zero.
        """
        self.score_x = 0
        self.score_o = 0
        self.score_label.config(text=f"Score: X: {self.score_x} | O: {self.score_o}")
        self.reset_game()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.mainloop()

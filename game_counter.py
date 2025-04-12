import tkinter as tk
from tkinter import messagebox
import os

class GameCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GameCounter")
        self.root.geometry("400x800")  # Increased resolution to accommodate history

        # Player names
        self.player1_name = tk.StringVar(value="Player 1")
        self.player2_name = tk.StringVar(value="Player 2")

        # Player scores
        self.player1_score = tk.IntVar(value=0)
        self.player2_score = tk.IntVar(value=0)

        # History file
        self.history_file = "game_history.txt"

        # UI Setup
        self.setup_ui()
        self.load_history()

    def setup_ui(self):
        # Title
        tk.Label(self.root, text="GameCounter", font=("Arial", 16, "bold")).pack(pady=10)

        # Name editing
        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(pady=5)
        tk.Label(self.name_frame, text="Edit Player 1 Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10)
        tk.Entry(self.name_frame, textvariable=self.player1_name, font=("Arial", 12)).grid(row=0, column=1, padx=10)
        tk.Label(self.name_frame, text="Edit Player 2 Name:", font=("Arial", 12)).grid(row=1, column=0, padx=10)
        tk.Entry(self.name_frame, textvariable=self.player2_name, font=("Arial", 12)).grid(row=1, column=1, padx=10)
        tk.Button(self.name_frame, text="Confirm", font=("Arial", 12), command=self.confirm_names).grid(row=2, column=0, columnspan=2, pady=10)

        # Match display
        self.match_frame = tk.Frame(self.root)
        self.match_frame.pack(pady=10)
        self.player1_label = tk.Label(self.match_frame, textvariable=self.player1_name, font=("Arial", 14, "bold"), fg="blue")
        self.player1_label.grid(row=0, column=0, padx=20)
        self.score_label = tk.Label(self.match_frame, text="0 - 0", font=("Arial", 14, "bold"))
        self.score_label.grid(row=0, column=1, padx=20)
        self.player2_label = tk.Label(self.match_frame, textvariable=self.player2_name, font=("Arial", 14, "bold"), fg="red")
        self.player2_label.grid(row=0, column=2, padx=20)

        # Buttons to increment scores
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        tk.Button(self.button_frame, text="Add Point to Player 1", font=("Arial", 12), command=self.add_point_player1).grid(row=0, column=0, padx=10)
        tk.Button(self.button_frame, text="Add Point to Player 2", font=("Arial", 12), command=self.add_point_player2).grid(row=0, column=1, padx=10)

        # Finish button
        tk.Button(self.root, text="End Match", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.finish_game).pack(pady=20)

        # History display
        tk.Label(self.root, text="Match History", font=("Arial", 14, "bold")).pack(pady=10)
        self.history_text = tk.Text(self.root, height=10, width=45, state="disabled", font=("Arial", 10))
        self.history_text.pack(pady=5)

    def confirm_names(self):
        # Hide the name editing frame
        self.name_frame.pack_forget()

    def update_score_display(self):
        self.score_label.config(text=f"{self.player1_score.get()} - {self.player2_score.get()}")

    def add_point_player1(self):
        self.player1_score.set(self.player1_score.get() + 1)
        self.update_score_display()

    def add_point_player2(self):
        self.player2_score.set(self.player2_score.get() + 1)
        self.update_score_display()

    def finish_game(self):
        winner = "It's a tie!"
        if self.player1_score.get() > self.player2_score.get():
            winner = f"{self.player1_name.get()} wins!"
        elif self.player2_score.get() > self.player1_score.get():
            winner = f"{self.player2_name.get()} wins!"

        # Save match result to history
        self.save_to_history(f"{self.player1_name.get()} {self.player1_score.get()} - {self.player2_score.get()} {self.player2_name.get()} | {winner}")

        # Show result and reset scores
        messagebox.showinfo("Game Over", f"Final Scores:\n"
                                         f"{self.player1_name.get()}: {self.player1_score.get()}\n"
                                         f"{self.player2_name.get()}: {self.player2_score.get()}\n\n{winner}")
        self.reset_game()

    def reset_game(self):
        # Reset scores and update display
        self.player1_score.set(0)
        self.player2_score.set(0)
        self.update_score_display()

    def save_to_history(self, result):
        with open(self.history_file, "a") as file:
            file.write(result + "\n")
        self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                history = file.read()
            self.history_text.config(state="normal")
            self.history_text.delete(1.0, "end")
            self.history_text.insert("end", history)
            self.history_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameCounterApp(root)
    root.mainloop()

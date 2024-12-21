import tkinter as tk
from tkinter import messagebox
from math import inf as infinity

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Global variables
player = "X"
COMP = "O"
HUMAN = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]


def empty_cells(state):
    return [[i, j] for i in range(3) for j in range(3) if state[i][j]["text"] == " "]


def alphabeta(state, depth, alpha, beta, player):
    if check_winner(state):
        return [-1, -1, 1] if player == HUMAN else [-1, -1, -1]
    elif is_draw():
        return [-1, -1, 0]

    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, infinity]

    for i in range(3):
        for j in range(3):
            if state[i][j]["text"] == " ":
                state[i][j]["text"] = player
                score = alphabeta(state, depth - 1, alpha, beta, HUMAN if player == COMP else COMP)
                state[i][j]["text"] = " "
                score[0], score[1] = i, j

                if player == COMP:
                    if score[2] > best[2]:
                        best = score
                    alpha = max(alpha, best[2])
                else:
                    if score[2] < best[2]:
                        best = score
                    beta = min(beta, best[2])

                if beta <= alpha:
                    break
    return best


def ai_turn():
    global player
    depth = len(empty_cells(buttons))
    if depth == 0 or check_winner(buttons):
        return

    move = alphabeta(buttons, depth, -infinity, infinity, COMP)
    buttons[move[0]][move[1]]["text"] = COMP

    if check_winner(buttons):
        messagebox.showinfo("Game Over", "Computer wins!")
        reset_game()
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
    else:
        player = HUMAN


def check_winner(state):
    for row in state:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != " ":
            return True

    for col in range(3):
        if state[0][col]["text"] == state[1][col]["text"] == state[2][col]["text"] != " ":
            return True

    if state[0][0]["text"] == state[1][1]["text"] == state[2][2]["text"] != " ":
        return True

    if state[0][2]["text"] == state[1][1]["text"] == state[2][0]["text"] != " ":
        return True

    return False

def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == " ":
                return False
    return True


def reset_game():
    global player
    player = HUMAN
    for row in buttons:
        for btn in row:
            btn["text"] = " "


def btn_click(btn):
    global player

    if btn["text"] == " " and player == HUMAN:
        btn["text"] = player
        if check_winner(buttons):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            player = COMP
            ai_turn()

# Create buttons and add them to the grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3,
                                  command=lambda i=i, j=j: btn_click(buttons[i][j]))
        buttons[i][j].grid(row=i, column=j)

# Start the main loop
root.mainloop()

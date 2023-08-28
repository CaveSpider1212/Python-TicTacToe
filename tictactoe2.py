from tkinter import Tk, Button, messagebox

# Root window
root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("350x360")

# Turn system
turn = 1
gameturn = 0

# Dictionary of buttons
buttons = {}

# Creating the buttons grid
for x in range (3): # Columns for the grid
    for y in range (3): # Rows for the grid
        button = Button(root, width = 12, height = 6, font = "15", command = lambda x=x, y=y: chooseBox(x, y))
        button.grid(row = y, column = x)
        buttons[x, y] = button

# Used to determine if a player won
def winCases(x1, y1, x2, y2, x3, y3, symbol, player):
    if (buttons[x1, y1] == symbol and buttons[x2, y2] == symbol and buttons[x3, y3] == symbol):
        root.destroy()
        messagebox.showinfo("Game over", f"Player {player} wins!")

# Used to determine if a player won or if a draw occured
def checkWin(): # might change later
    global gameturn

    winCases(0, 0, 1, 0, 2, 0, "X", 1)
    winCases(0, 1, 1, 1, 2, 1, "X", 1)
    winCases(0, 2, 1, 2, 2, 2, "X", 1)
    winCases(0, 0, 0, 1, 0, 2, "X", 1)
    winCases(1, 0, 1, 1, 1, 2, "X", 1)
    winCases(2, 0, 2, 1, 2, 2, "X", 1)
    winCases(0, 0, 1, 1, 2, 2, "X", 1)
    winCases(0, 2, 1, 1, 2, 0, "X", 1)

    winCases(0, 0, 1, 0, 2, 0, "O", 2)
    winCases(0, 1, 1, 1, 2, 1, "O", 2)
    winCases(0, 2, 1, 2, 2, 2, "O", 2)
    winCases(0, 0, 0, 1, 0, 2, "O", 2)
    winCases(1, 0, 1, 1, 1, 2, "O", 2)
    winCases(2, 0, 2, 1, 2, 2, "O", 2)
    winCases(0, 0, 1, 1, 2, 2, "O", 2)
    winCases(0, 2, 1, 1, 2, 0, "O", 2)
    
    if gameturn == 9:
        root.destroy()
        messagebox.showinfo("Game over", "Draw")

# Main game
def chooseBox(x, y):
    global turn
    global gameturn
    if buttons[x, y] != "X" and buttons[x, y] != "O": # Alternative to the "DISABLED" keyword
        if turn == 1:
            buttons[x, y].config(text = "X")
            buttons[x, y] = "X"
            turn = 2
        else:
            buttons[x, y].config(text = "O")
            buttons[x, y] = "O"
            turn = 1
        gameturn += 1
    checkWin()

root.mainloop()

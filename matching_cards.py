import random
from tkinter import Tk, Button

# Main window
root = Tk()
root.title("Memory Game")
root["bg"]="#FFCC82"
root.geometry("420x400")

# Cards replaced with emojis
cards = ['🍎','🍎','🍌','🍌','🍇','🍇','🍓','🍓',
         '🍒','🍒','🍉','🍉','🥝','🥝','🍍','🍍']
random.shuffle(cards)

buttons = {}
card_values = {}
first_click = None  # To remember the first clicked card

def on_click(row, col):
    global first_click
    btn = buttons[(row, col)]
    btn.config(text=card_values[(row, col)])  # Reveal card

    if first_click is None:
        # This is the first card clicked
        first_click = (row, col)
    else:
        # This is the second card clicked
        r1, c1 = first_click
        r2, c2 = row, col

        if card_values[(r1, c1)] == card_values[(r2, c2)]:
            # Match found: disable buttons
            buttons[(r1, c1)].config(state='disabled')
            buttons[(r2, c2)].config(state='disabled')
        else:
            # Not a match: hide again after short delay
            root.after(1000, lambda: hide_cards(r1, c1, r2, c2))

        first_click = None  # Reset first click

def hide_cards(r1, c1, r2, c2):
    buttons[(r1, c1)].config(text='')
    buttons[(r2, c2)].config(text='')

def create_grid():
    index = 0
    for row in range(4):
        for col in range(4):
            card_values[(row, col)] = cards[index]
            index += 1
            
            # Button with click event
            btn = Button(
                root,
                text="",            # Hidden card placeholder
                width=5,                     # width in characters
                height=2,                    # height in text lines
                bg='white',
                fg='black',
                font=('Arial', 20),
                command=lambda r=row, c=col: on_click(r, c)
            )
            btn.grid(row=row, column=col, padx=6, pady=6)
            buttons[(row, col)] = btn

create_grid()
root.mainloop()
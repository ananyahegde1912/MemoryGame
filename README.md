
# **Memory Game**

## **Description**
I created a Memory Game where users try to match pairs of cards. It’s a fun way to test memory skills and keep the player engaged with simple gameplay.

## **Features**
- Users click on cards to reveal their icons.
- If the two selected cards match, they stay revealed and turn grey.
- If the cards do not match, they flip back after a short delay so the user can try again.
- Tracks each attempt and gives immediate visual feedback on whether the selection was correct or not.
  
<img width="346" height="351" alt="Screenshot 2026-03-08 083323" src="https://github.com/user-attachments/assets/1ea32107-890f-4f60-aab5-9219cead51e8" />


## **How It Works**

- I used Tkinter to create a 4x4 grid of Button widgets for the cards.
- Each card has a hidden value (like a fruit emoji) stored in a dictionary.
- When a user clicks a card, the on_click function reveals the card’s icon.
- If the two clicked cards match, their state is set to 'disabled' and they turn grey.
- If the two cards do not match, the hide_cards function flips them back by setting their text to an empty string ("") after a short delay using root.after.
- This provides instant feedback and helps users remember which cards have already been revealed.

## **Installation**

1. Download or clone this repository.
2. Make sure Python is installed on your system.
3. Run the `memory_game.py` file using Python.

## **Future Improvements**

- Add more card themes and levels of difficulty.

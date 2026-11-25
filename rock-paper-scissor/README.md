# Rock Paper Scissors Game – Python GUI

## 1. Project Overview

This is a Rock Paper Scissors game developed using Python and Tkinter.

The game allows the player to select one of three options:
- Rock
- Paper
- Scissor

The computer randomly selects its option. The program compares both choices, determines the winner, and updates the scores.

The game also displays images for the player's and computer's choices.

## 2. Libraries Used

### 1. Tkinter

```python
from tkinter import *
```

**What is Tkinter?**

Tkinter is Python's standard library for creating Graphical User Interfaces (GUI).

It allows us to create desktop applications with windows, buttons, labels, text fields, menus, etc.

**Tkinter components used in this project:**

| Component | Purpose |
|---|---|
| `Tk()` | Creates the main application window |
| `Label()` | Displays text, scores and images |
| `Button()` | Creates clickable buttons |
| `configure()` | Changes widget properties |
| `grid()` | Arranges widgets in rows and columns |
| `mainloop()` | Keeps the GUI running and waits for user actions |

### 2. Pillow (PIL)

```python
from PIL import Image, ImageTk
```

**What is Pillow?**

Pillow is a Python imaging library used to open, edit, resize and manipulate images.

It is the modern fork of the original Python Imaging Library (PIL).

**Classes used:**

- `Image`: Opens and resizes image files.
- `ImageTk`: Converts images into a format that Tkinter can display.

Example:

```python
image_rockR = ImageTk.PhotoImage(
    Image.open("./src/rock_paper_scissor/rockR.png").resize((200, 200))
)
```

Explanation:

1. `Image.open()` opens the image.
2. `.resize((200, 200))` changes its dimensions to 200 × 200 pixels.
3. `ImageTk.PhotoImage()` converts it into a Tkinter-compatible image.

### 3. Random Library

```python
from random import randint
```

**What is Random?**

The random module is a built-in Python library used to generate random values.

In this project, `randint()` randomly selects the computer's choice.

Example:

```python
choice_computer = to_select[randint(0, 2)]
```

Explanation:

- `randint(0, 2)` generates a random integer between 0 and 2 (inclusive).
- The generated number is used as an index to select an item from the list.

```python
to_select = ["rock", "paper", "scissor"]
```

Possible results:
- 0 → rock
- 1 → paper
- 2 → scissor

---

## 3. GUI Window Creation

```python
window = Tk()
window.title("Rock Paper Scissors")
window.configure(bg="#9b59b6")
```

Explanation:

- `Tk()` creates the main application window.
- `title()` sets the window title.
- `configure(bg=...)` sets the background colour.

## 4. Loading and Displaying Images

```python
image_rockR = ImageTk.PhotoImage(
    Image.open("./src/rock_paper_scissor/rockR.png").resize((200, 200))
)
```

We load four images:
- Rock for the player.
- Rock for the computer.
- Paper.
- Scissor.

The images are resized to 200 × 200 pixels.

```python
label_player = Label(window, image=image_rockR)
label_computer = Label(window, image=image_rockL)
```

The Label widget displays the images inside the application window.

**Why use ImageTk.PhotoImage?**

Tkinter cannot directly display Pillow's `Image` objects. `ImageTk.PhotoImage()` converts them into a format that Tkinter supports.

## 5. Scoreboard

```python
computer_score = Label(
    window, text=0, font=("arial", 60, "bold"), fg="red"
)

player_score = Label(
    window, text=0, font=("arial", 60, "bold"), fg="red"
)
```

These labels display the computer's and player's scores.

The initial score is 0.

### Updating Computer Score

```python
def computer_score_upadte():
    final = int(computer_score["text"])
    final += 1
    computer_score["text"] = str(final)
```

Explanation:

1. Reads the current computer score.
2. Converts it into an integer using `int()`.
3. Increases the score by 1.
4. Updates the label with the new score.

### Updating Player Score

```python
def player_score_upadte():
    final = int(player_score["text"])
    final += 1
    player_score["text"] = str(final)
```

This function performs the same operation for the player's score.

## 6. Displaying the Game Result

```python
def msg_updation(a):
    final_message["text"] = a
```

This function updates the result message displayed on the screen.

For example:
- Player Wins!!
- Computer Wins!!
- It's a tie

## 7. Winner Checking Logic

```python
def winner_check(p, c):
```

This function compares the player's choice (`p`) with the computer's choice (`c`).

## 8. Computer's Random Choice

```python
to_select = ["rock", "paper", "scissor"]
```

This list stores all three possible choices.

```python
def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
```

Every time the player clicks a button, the computer randomly selects one option.

## 9. Updating Player and Computer Images

```python
if choice_computer == "rock":
    label_computer.configure(image=image_rockL)
elif choice_computer == "paper":
    label_computer.configure(image=image_paper)
else:
    label_computer.configure(image=image_scissor)
```

This changes the computer's image based on its randomly selected choice.

Similarly:

```python
if a == "rock":
    label_player.configure(image=image_rockR)
elif a == "paper":
    label_player.configure(image=image_paper)
else:
    label_player.configure(image=image_scissor)
```

This changes the player's image based on the button clicked.

Finally:

```python
winner_check(a, choice_computer)
```

The function compares both choices and updates the result and scoreboard.

## 10. Creating Buttons

```python
button_rock = Button(
    window,
    width=16,
    height=3,
    text="ROCK",
    font=("arial", 20, "bold"),
    bg="yellow",
    fg="red",
    command=lambda: choice_update("rock")
).grid(row=2, column=1)
```

Three buttons are created:
- ROCK
- PAPER
- SCISSOR

**Important concepts:**

- `text`: Displays the button name.
- `bg`: Sets the background colour.
- `fg`: Sets the text colour.
- `width` and `height`: Set button dimensions.
- `command`: Defines the function executed when the button is clicked.

### Why use lambda?

```python
command=lambda: choice_update("rock")
```

Lambda creates a small anonymous function.

It allows us to pass an argument to `choice_update()` when the user clicks the button.

Without lambda:

```python
command=choice_update("rock")
```

The function would execute immediately when the button is created rather than waiting for a click.

## 11. Grid Layout Manager

```python
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)
```

The `grid()` geometry manager arranges widgets in a table-like structure using rows and columns.

For example:

```python
.grid(row=2, column=1)
```

Places the widget in row 2 and column 1.

## 12. Main Event Loop

```python
window.mainloop()
```

This is the main event loop of the Tkinter application.

It:
- Keeps the application window open.
- Waits for user interactions.
- Detects button clicks.
- Executes the associated functions.
- Updates the GUI when required.

Without `mainloop()`, the application window would close immediately.

---

## 13. Complete Game Flow

1. The application window opens.
2. Player and computer images are displayed.
3. Both scores start at 0.
4. The player clicks Rock, Paper or Scissor.
5. The computer randomly selects its choice.
6. Both images are updated.
7. The winner-checking function compares the choices.
8. The result message is displayed.
9. The winner's score increases by 1.
10. The player can play again.

## 14. Python Concepts Practised

| Concept | Where Used |
|---|---|
| Functions | `winner_check()`, `choice_update()` |
| Conditional statements | `if`, `elif`, `else` |
| Lists | `to_select` |
| Random numbers | `randint()` |
| Type conversion | `int()`, `str()` |
| GUI programming | Tkinter |
| Image processing | Pillow |
| Lambda functions | Button commands |
| Event handling | Button clicks |
| Object interaction | Updating Label properties |

## 15. Project Summary

This project helped me understand how to build a desktop GUI application using Python.

I learned how to:
- Create GUI windows using Tkinter.
- Display and resize images using Pillow.
- Generate random computer choices.
- Use conditional statements to determine the winner.
- Create interactive buttons.
- Update labels dynamically.
- Maintain and display scores.
- Handle user events through Tkinter.

**Libraries used:**
- Tkinter – GUI development.
- Pillow – Image loading and resizing.
- Random – Random computer selection.
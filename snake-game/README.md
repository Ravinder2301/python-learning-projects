# 🐍 Snake Game – Python Project

## 1. Libraries Used

| Library | Purpose |
|---|---|
| `pygame` | Creates the game window, draws the snake and food, handles keyboard events, displays text and updates the screen. |
| `random` | Generates random positions for the food. |
| `time` | Provides time-related functions (imported but not directly used in this code). |

## 2. Main Logic Used

1. **Initialize Pygame:** `pygame.init()` initializes all Pygame modules.
2. **Create Game Window:** `pygame.display.set_mode()` creates a 900 × 600 game window.
3. **Set Game Speed:** `pygame.time.Clock()` controls the snake's movement speed.
4. **Generate Food:** `random.randrange()` generates random X and Y coordinates for food.
5. **Keyboard Controls:** `pygame.event.get()` detects arrow-key presses to move the snake up, down, left and right.
6. **Snake Movement:** The snake's X and Y coordinates are updated based on the direction.
7. **Track Snake Body:** A list (`list_snake`) stores the coordinates of each snake block.
8. **Food Collision:** When the snake touches the food, its length increases and new food is generated.
9. **Collision Detection:** The game ends when the snake hits the screen boundaries or its own body.
10. **Score Calculation:** The score increases whenever the snake eats food.
11. **Game Over:** The player can press `C` to restart or `Q` to quit.

## 3. Important Pygame Functions

| Function | Usage |
|---|---|
| `pygame.init()` | Initializes Pygame |
| `pygame.display.set_mode()` | Creates game window |
| `pygame.display.set_caption()` | Sets window title |
| `pygame.draw.rect()` | Draws snake and food |
| `pygame.font.SysFont()` | Creates fonts |
| `pygame.event.get()` | Handles keyboard and window events |
| `pygame.display.update()` | Refreshes the screen |
| `pygame.time.Clock()` | Controls game FPS |

## 4. Concepts Practiced

- Python functions
- While loops and for loops
- Lists and list manipulation
- Conditional statements (`if-else`)
- Random number generation
- Keyboard event handling
- Collision detection
- Basic game development using Pygame

## 5. How to Run

Install Pygame:

```bash
uv add pygame
```

Run the game:

```bash
uv run snake_game.py
```

**Controls:**
- ⬆️ Up Arrow – Move Up
- ⬇️ Down Arrow – Move Down
- ⬅️ Left Arrow – Move Left
- ➡️ Right Arrow – Move Right
- C – Restart
- Q – Quit
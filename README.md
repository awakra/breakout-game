# Breakout Game

A classic Breakout/Arkanoid-style game built with Python and Pygame.

## Features

- Paddle and ball mechanics
- Multiple rows of colored bricks
- Score tracking
- Life system with Game Over and retry functionality
- FPS counter
- Modular code structure for easy maintenance and extension

## How to Play

- Move the paddle left and right using the arrow keys.
- The ball starts attached to the paddle. Press the UP arrow to launch the ball.
- Break all the bricks to score points.
- You lose a life if the ball falls below the paddle.
- The game ends when you run out of lives. Press `R` to retry or close the window to exit.

## Project Structure

.
├── main.py
├── metrics.py
├── collision_manager.py
├── constants.py
├── utils.py
├── sprites/
│   ├── paddle.py
│   ├── brick.py
│   └── ball.py
├── README.md


- `main.py`: Main game loop and initialization
- `metrics.py`: HUD elements (FrameRate, Scoreboard, Lives)
- `collision_manager.py`: Handles all collision logic
- `constants.py`: Game constants (colors, sizes, etc.)
- `utils.py`: Utility functions for game loop and reset logic
- `sprites/`: Contains Paddle, Brick, and Ball classes

## Requirements

- Python 3.8+
- Pygame 2.x

## Installation

1. Clone this repository:
    ```
    git clone <repo_url>
    cd breakout-game
    ```
2. Install dependencies:
    ```
    pip install pygame
    ```
3. Run the game:
    ```
    python main.py
    ```

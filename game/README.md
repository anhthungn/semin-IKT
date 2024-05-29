# Space War

## Overview
**Space War** is an exciting space shooter game where players control a spaceship, navigate through an asteroid field, collect bonuses, and try to survive as long as possible. The goal is to achieve the highest score while avoiding collisions with asteroids and managing health.

## Features
- Control a spaceship with rotation and movement.
- Dodge asteroids of varying sizes.
- Collect bonuses such as coins, hearts, and diamonds to increase your score and restore health.
- Pixel-perfect collision detection for an immersive experience.
- Game over screen with an option to play again.

## Setup Instructions
### Prerequisites
- Python 3.x
- Pygame library

### Installation
1. Clone this repository to your local machine:
    ```sh
    git clone 'https://github.com/anhthungn/semin-IKT/tree/main/game'
    ```

2. Install the required libraries:
    ```sh
    'pip install pygame'
    ```

3. Run the game:
    ```sh
    'python main.py'
    ```

## Gameplay Instructions
1. **Start Screen**: 
   - Upon launching the game, you will see the game title and a "Press to Start" message. Click anywhere on the screen to start the game.

2. **Controls**:
   - Use the `W` key to move forward.
   - Use the `A` key to rotate left.
   - Use the `D` key to rotate right.

3. **Game Mechanics**:
   - **Asteroids**: Avoid collisions with asteroids. Each collision will decrease your health.
   - **Coins**: Collect coins to increase your score by 50 points.
   - **Hearts**: Collect hearts to restore one health point (up to a maximum of 3).
   - **Diamonds**: Collect diamonds to increase your score by 100 points.

4. **Scoring**:
   - The score is displayed at the top right corner of the screen.
   - The remaining lives are displayed at the top left corner of the screen.

5. **Game Over**:
   - If you lose all your health points, the game will display a game over screen.
   - A "Game Over" message will appear, followed by a "Play Again?" prompt with two buttons: "Yes" and "No".
     - Clicking "Yes" restarts the game.
     - Clicking "No" exits the game.

## Assets
- Images and sounds used in the game are stored in the `resouces/images` and `resouces/sound effects` directories, respectively.

## Credits
- Game Developer: [Nguyen Anh Thu ]

## Contributing
If you wish to contribute to this project, feel free to fork the repository and submit pull requests.

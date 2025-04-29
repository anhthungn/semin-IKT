void initGame() {
  snakeLength = 3;
  // Initial snake position (horizontal line; head at (3,4), tail leftwards)
  snake[0].x = 3; snake[0].y = 4;
  snake[1].x = 2; snake[1].y = 4;
  snake[2].x = 1; snake[2].y = 4;
  direction = 1; // start moving to the right

  generateFood();
}

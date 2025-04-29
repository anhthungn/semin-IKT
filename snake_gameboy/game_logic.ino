void updateGame() {
  // Calculate new head position based on direction
  Coord newHead = snake[0];
  if (direction == 0) { // up
    newHead.y = (newHead.y == 0) ? 7 : newHead.y - 1;
  } else if (direction == 1) { // right
    newHead.x = (newHead.x == 7) ? 0 : newHead.x + 1;
  } else if (direction == 2) { // down
    newHead.y = (newHead.y == 7) ? 0 : newHead.y + 1;
  } else if (direction == 3) { // left
    newHead.x = (newHead.x == 0) ? 7 : newHead.x - 1;
  }

  // Check collision with self
  for (int i = 0; i < snakeLength; i++) {
    if (snake[i].x == newHead.x && snake[i].y == newHead.y) {
      gameOver();
      return;
    }
  }
  
  noTone(BUZZER);
  
  // Check if food is eaten
  bool ateFood = (newHead.x == food.x && newHead.y == food.y);
  if (ateFood) {
    if (snakeLength < 64) {
      for (int i = snakeLength; i > 0; i--) {
        snake[i] = snake[i - 1];
      }
      snake[0] = newHead;
      snakeLength++;
      generateFood();
      tone(BUZZER, 400);
      score++;
    }
  } else {
    // Move snake: shift segments, update head
    for (int i = snakeLength - 1; i > 0; i--) {
      snake[i] = snake[i - 1];
    }
    snake[0] = newHead;
  }
  
  displayScore();
  drawGame();
}

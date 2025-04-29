void generateFood() {
  bool valid = false;
  while (!valid) {
    food.x = random(0, 8);
    food.y = random(0, 8);
    valid = true;
    for (int i = 0; i < snakeLength; i++) {
      if (snake[i].x == food.x && snake[i].y == food.y) {
        valid = false;
        break;
      }
    }
  }
}

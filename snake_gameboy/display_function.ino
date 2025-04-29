void drawGame() {
  ledMat.clearDisplay(DEVICE);
  // Draw snake with rotation:
  // Transformation: new row = original x, new column = (7 - original y)
  for (int i = 0; i < snakeLength; i++) {
    int newRow = snake[i].x;
    int newCol = 7 - snake[i].y;
    ledMat.setLed(DEVICE, newRow, newCol, true);
  }
  // Draw food with the same rotation
  int foodRow = food.x;
  int foodCol = 7 - food.y;
  ledMat.setLed(DEVICE, foodRow, foodCol, true);
}

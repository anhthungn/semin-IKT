void gameOver() {
  for (int i = 0; i < 3; i++) {
    ledMat.clearDisplay(DEVICE);
    delay(200);
    for (int row = 0; row < 8; row++) {
      ledMat.setRow(DEVICE, row, B11111111);
    }
    delay(200);
  }
  score = 0;
  initGame();
}

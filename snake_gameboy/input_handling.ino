void readButtons() {
  // Buttons use INPUT_PULLUP (pressed = LOW)
  if (digitalRead(BTN_UP) == LOW && direction != 2) {
    direction = 0; // up
  }
  else if (digitalRead(BTN_RIGHT) == LOW && direction != 3) {
    direction = 1; // right
  }
  else if (digitalRead(BTN_DOWN) == LOW && direction != 0) {
    direction = 2; // down
  }
  else if (digitalRead(BTN_LEFT) == LOW && direction != 1) {
    direction = 3; // left
  }
}

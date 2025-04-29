void loop() {
  readButtons();

  if (millis() - lastUpdateTime >= updateInterval) {
    lastUpdateTime = millis();
    updateGame();
  }
}

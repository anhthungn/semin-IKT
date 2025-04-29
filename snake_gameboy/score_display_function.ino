void displayScore(){
  int digitOne = score/10;
  int digitTwo = score%10;
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, digits[digitTwo]); // digitTwo
  shiftOut(dataPin, clockPin, MSBFIRST, digits[digitOne]); // digitOne
  digitalWrite(latchPin, HIGH);
}

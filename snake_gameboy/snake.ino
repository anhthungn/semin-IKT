#include "LedControl.h"

// Připojovací piny pro LED matici (MAX7219)
#define DIN 10
#define CS  11
#define CLK 12
#define DEVICE 0

#define latchPin 3
#define clockPin 2
#define dataPin 1

#define BUZZER 4
// Piny pro tlačítka – využíváme interní pull-up rezistory
#define BTN_UP    6
#define BTN_DOWN  9
#define BTN_LEFT  7
#define BTN_RIGHT 8

// Initialize LED matrix
LedControl ledMat = LedControl(DIN, CLK, CS, DEVICE);

// Structure for storing coordinates
struct Coord {
  byte x;
  byte y;
};

// Maximum snake length (8x8 grid)
Coord snake[64];
int snakeLength;
int direction; // 0 = up, 1 = right, 2 = down, 3 = left
Coord food;

unsigned long lastUpdateTime = 0;
const unsigned long updateInterval = 300; // Game speed (ms)

byte digits[10]={0x7E,0x0C,0xB6,0x9E,0xCC,0xDA,0xFA,0x0E,0xFE,0xDE};
int score = 0;

void setup() {
  // Initialize the LED matrix
  ledMat.shutdown(DEVICE, false);
  ledMat.setIntensity(DEVICE, 7);
  ledMat.clearDisplay(DEVICE);

  pinMode(latchPin, OUTPUT);

  pinMode(clockPin, OUTPUT);

  pinMode(dataPin, OUTPUT);
 
  pinMode(BUZZER, OUTPUT);
  // Initialize buttons (internal pull-ups)
  pinMode(BTN_UP, INPUT_PULLUP);
  pinMode(BTN_DOWN, INPUT_PULLUP);
  pinMode(BTN_LEFT, INPUT_PULLUP);
  pinMode(BTN_RIGHT, INPUT_PULLUP);

  // Seed random generator
  randomSeed(analogRead(0));

  // Initialize the game
  initGame();
}

void loop() {


  // Read buttons and update the direction
  readButtons();

  // Update game state based on the update interval
  if (millis() - lastUpdateTime >= updateInterval) {
    lastUpdateTime = millis();
    updateGame();
  }
}

// Initialize the game state
void initGame() {
  snakeLength = 3;
  // Initial snake position (horizontal line; head at (3,4), tail leftwards)
  snake[0].x = 3; snake[0].y = 4;
  snake[1].x = 2; snake[1].y = 4;
  snake[2].x = 1; snake[2].y = 4;
  direction = 1; // start moving to the right

  generateFood();
}

// Read buttons and update direction (ensuring no 180° turn)
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

// Update the game state (move snake, check food and collisions)
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

void displayScore(){
  int digitOne = score/10;
  int digitTwo = score%10;
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, digits[digitTwo]); // digitTwo
  shiftOut(dataPin, clockPin, MSBFIRST, digits[digitOne]); // digitOne
  digitalWrite(latchPin, HIGH);
}

// Generate food at a random free position
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

// Draw the game (snake and food) on the LED matrix with 90° clockwise rotation
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

// Show game over effect and restart game
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

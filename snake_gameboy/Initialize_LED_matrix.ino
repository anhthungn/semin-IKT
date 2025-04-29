LedControl ledMat = LedControl(DIN, CLK, CS, DEVICE);

// Structure for storing coordinates
struct Coord {
  byte x;
  byte y;
};

// Snake variables
Coord snake[64];       // Maximum snake length (8x8 grid)
int snakeLength;       // Current snake length
int direction;         // 0 = up, 1 = right, 2 = down, 3 = left
Coord food;            // Food position

// Game timing
unsigned long lastUpdateTime = 0;
const unsigned long updateInterval = 300; // Game speed (ms)

// 7-segment display digit patterns (0-9)
byte digits[10] = {0x7E,0x0C,0xB6,0x9E,0xCC,0xDA,0xFA,0x0E,0xFE,0xDE};
int score = 0;         // Player score

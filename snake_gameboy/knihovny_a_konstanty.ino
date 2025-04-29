#include "LedControl.h"

// Připojovací piny pro LED matici (MAX7219)
#define DIN 10
#define CS  11
#define CLK 12
#define DEVICE 0

// Piny pro 7segmentový displej
#define latchPin 3
#define clockPin 2
#define dataPin 1

// Bzučák
#define BUZZER 4

// Tlačítka
#define BTN_UP    6
#define BTN_DOWN  9
#define BTN_LEFT  7
#define BTN_RIGHT 8

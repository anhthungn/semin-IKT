#darina
import random

distance = 14 
path = ["." for x in range(distance)]

current_pos = distance // 2

steps = 0
MAX_STEPS = 30

def printPath(path):
    print(f"home {' '.join(path)} pub")

def game(steps, max_steps, path, current_pos):
    
    path[current_pos] = "*" 
    printPath(path)

    while distance > current_pos >= 0 and steps < max_steps:
        steps += 1
        path[current_pos] = "." 
        
        random_number = random.choice([-1, 1])
        current_pos += random_number

        if distance > current_pos >= 0:
            path[current_pos] = "*" 
        else:
            break

        printPath(path)

    if current_pos < 0:
        print("Arrived home")
    elif current_pos >= distance:
        print("Ended in the pub again")
    elif steps == max_steps:
        print("Fallen asleep.")


game(steps, MAX_STEPS, path, current_pos)

pocitadlo = 0
for i in range(100):
    vysledek = game(steps, MAX_STEPS, path, current_pos)
    if vysledek:
        pocitadlo += 1

print(pocitadlo/100 * 100)
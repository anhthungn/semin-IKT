#darina
import random

distance = 14
path = ["." for x in range(distance)]

current_pos = distance // 2

steps = 0
MAX_STEPS = 86

def printPath(path):
    print(f"home {' '.join(path)} pub")

def game(steps, MAX_STEPS, path, current_pos):
    
    path[current_pos] = "*" 
    printPath(path)

    while distance > current_pos >= 0 and steps < MAX_STEPS:
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
        # print("Arrived home")
        return "home"
    elif current_pos >= distance:
        # print("Ended in the pub again")
        return "pub"
    elif steps == MAX_STEPS:
        # print("Falled asleep.")
        return "asleep"


game(steps, MAX_STEPS, path, current_pos)


total_simulations = 100
success_count = 0

for i in range(total_simulations):
    results = game(steps, MAX_STEPS, path, current_pos)
    if results in ["home", "pub"]:
        success_count += 1

percentage = success_count/total_simulations * 100
print(f"Success rate after {total_simulations} simulations: {percentage}%")

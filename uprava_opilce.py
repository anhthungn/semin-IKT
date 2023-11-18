#darina
import random

distance = 14
path = ["." for x in range(distance)]

drunkyard = distance // 2

steps = 0
MAX_STEPS = 88

def printPath(path):
    print(f"home {' '.join(path)} pub")

def game(steps, MAX_STEPS, path, drunkyard):
    
    path[drunkyard] = "*" 
    printPath(path)

    while distance > drunkyard >= 0 and steps < MAX_STEPS:
        steps += 1
        path[drunkyard] = "."
        
        random_number = random.choice([-1, 1])
        drunkyard += random_number

        if distance > drunkyard >= 0:
            path[drunkyard] = "*" 
        else:
            break

        printPath(path)

    if drunkyard < 0:
        # print("Arrived home")
        return "home"
    elif drunkyard >= distance:
        # print("Ended in the pub again")
        return "pub"
    elif steps == MAX_STEPS:
        # print("Falled asleep.")
        return "asleep"


game(steps, MAX_STEPS, path, drunkyard)


total_simulations = 100
success_count = 0

for i in range(total_simulations):
    results = game(steps, MAX_STEPS, path, drunkyard)
    if results in ["home", "pub"]:
        success_count += 1

percentage = success_count/total_simulations * 100
print(f"Success rate after {total_simulations} simulations: {percentage}%")

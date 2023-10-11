import random

def drunkard(distance, step_count):
    position = distance / 2 #position of the drunkyard starts in the middle of the distance
    home = 0 #home is at the 0 distance
    pub = distance #pub = the distance from home to pub

    for step in range (step_count): #the number of steps he can do - since the step count is 20 -> he cant do 22 then
        step = [-1, 1] #step left (-1) step right (+1)
        drunkard_steps = random.choice(step) #drunkyard will make random steps either to the right or left
        position += drunkard_steps #his position + his steps (example: position = 5 -> postion = 5+1/5-1)

        print("home", "." * int(position) + "*" + "." * int(distance - position), "pub") 

        if position == home:
            return "Ended up at home!"
        elif position == pub:
            return "Ended up in the pub again!"
        
result = drunkard(9, 8)
print(result)

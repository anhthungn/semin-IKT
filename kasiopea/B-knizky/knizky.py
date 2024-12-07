import sys

def minimal_steps(N, shelf):
    # find all the positions of 'K' on the shelf
    positions = [i for i, char in enumerate(shelf) if char == 'K']
    
    # find the median
    median_index = len(positions) // 2
    median_position = positions[median_index]
    
    # calculate the minimal number of steps to move the books together
    steps = 0
    for i, pos in enumerate(positions):
        steps += abs(pos - (median_position - median_index + i))
    
    return steps

def read_input(input, output):
    num_of_problems = int(input.readline())
    
    for _ in range(num_of_problems):
        N = int(input.readline())  # shelf length
        shelf = input.readline().strip()
        
        results = minimal_steps(N, shelf)
        output.write(f"{results}\n")

file_names = [
    ("úkoly/kasiopea/B-knizky/B-lehky.txt", "úkoly/kasiopea/B-knizky/B-lehky-vystup.txt"),
]

file_found = False

for input_file, output_file in file_names:
    try:
        with open(input_file, "r", 1, "utf-8") as input:
            with open(output_file, "w", 1, "utf-8") as output:
                read_input(input, output)

        file_found = True

    except FileNotFoundError:
        pass

if not file_found:
    read_input(sys.stdin, sys.stdout)

#!/usr/bin/env python3
import sys

def minimal_time(num_of_cards, cutting_time, scissors_time, scissors_num): # N X Y K
    # time using only the cutter
    cutter_time = num_of_cards * cutting_time # N * X

    # time using scissors for as much paper as possible, and a cutter for the rest
    scissors_batches = num_of_cards // scissors_num
    remaining_cards = num_of_cards % scissors_num  # remaining papers to cut individually
    scissors_time_total = scissors_batches * scissors_time + remaining_cards * cutting_time

    # return the minimal time
    return min(cutter_time, scissors_time_total)

def read_input(input, output):
    num_of_problems = int(input.readline())

    for _ in range(num_of_problems):
        num_of_cards, cutting_time, scissors_time, scissors_num = map(int, input.readline().split())

        results = minimal_time(num_of_cards, cutting_time, scissors_time, scissors_num)

        output.write(f"{results}\n")
        
file_names = [
    ("úkoly/kasiopea/A-karticky/A-lehky.txt", "úkoly/kasiopea/A-karticky/A-lehky-vystup.txt"),
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

import random
import linecache

file_path = "response.txt"
num_lines = sum(1 for line in open(file_path))  


random_line_numbers = random.sample(range(1, num_lines + 1), 5)

for line_number in random_line_numbers:
    line = linecache.getline(file_path, line_number).strip()
    print(f"Line {line_number}: {line}")
    print("\n\n")

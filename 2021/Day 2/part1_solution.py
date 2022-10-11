horizontal = 0
depth = 0

with open("2021/Day 2/input_data.txt",'r') as input_data:
    for line in input_data:
        elements = line.split(" ")
        command = elements[0]
        number = elements[1]
        if command == 'forward':
            horizontal += int(number)
        elif command == 'down':
            depth += int(number)
        elif command == 'up':
            depth -= int(number)

print(horizontal * depth)
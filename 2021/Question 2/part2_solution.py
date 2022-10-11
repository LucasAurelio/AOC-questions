horizontal = 0
depth = 0
aim = 0

with open("2021/Question 2/input_data.txt",'r') as input_data:
    for line in input_data:
        elements = line.split(" ")
        command = elements[0]
        number = elements[1]
        if command == 'forward':
            horizontal += int(number)
            depth += aim * int(number)
        elif command == 'down':
            aim += int(number)
        elif command == 'up':
            aim -= int(number)

print(horizontal * depth)
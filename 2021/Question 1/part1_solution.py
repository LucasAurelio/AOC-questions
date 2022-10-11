

number_increases = 0
measurement = None

with open("2021/Question 1/input.txt",'r') as input_data:
    for line in input_data:
        if measurement is not None:
            if int(line) > measurement:
                number_increases += 1
        measurement = int(line)

print(number_increases)
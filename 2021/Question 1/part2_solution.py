number_increases = 0
latest_sum = None
measurements = []

with open("2021/Question 1/input_data.txt",'r') as input_data:
    for line in input_data:
            measurements.append(int(line))
            if len(measurements)==3:
                new_sum = sum(measurements)
                if latest_sum is not None:
                    if new_sum > latest_sum:
                        number_increases += 1
                latest_sum = new_sum
                measurements.pop(0)

print(number_increases)
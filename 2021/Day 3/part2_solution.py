oxygen_generator = []
co2_scrubber = []


def find_most(currentList,currentIndex):
    count_ones = 0
    count_zeros = 0

    for element in currentList:
        if element[currentIndex]=='0': 
            count_zeros += 1
        elif element[currentIndex]=='1':
            count_ones += 1
    
    if count_ones>count_zeros:
        return '1'
    elif count_zeros>count_ones:
        return '0'
    elif count_ones==count_zeros:
        return '1'

def find_least(currentList,currentIndex):
    count_ones = 0
    count_zeros = 0

    for element in currentList:
        if element[currentIndex]=='0': 
            count_zeros += 1
        elif element[currentIndex]=='1':
            count_ones += 1
    
    if count_ones<count_zeros:
        return '1'
    elif count_zeros<count_ones:
        return '0'
    elif count_ones==count_zeros:
        return '0'


with open("2021/Day 3/input_data.txt",'r') as input_data:
    for line in input_data:
        oxygen_generator.append(line)
        co2_scrubber.append(line)

ind_co2 = 0
ind_oxygen = 0
while len(oxygen_generator)>1 or len(co2_scrubber)>1:
    if len(oxygen_generator)>1:
        temp_list_one = []
        mostTimes = find_most(oxygen_generator,ind_oxygen)
        for element in oxygen_generator:
            if element[ind_oxygen] == mostTimes:
                temp_list_one.append(element)
        if len(temp_list_one)>0:
            oxygen_generator = temp_list_one
        
    ind_oxygen += 1

    if len(co2_scrubber)>1:
        temp_list = []
        mostTimes = find_least(co2_scrubber,ind_co2)
        for element in co2_scrubber:
            if element[ind_co2] == mostTimes:
                temp_list.append(element)
        if len(temp_list)>0:
            co2_scrubber = temp_list
        
    ind_co2 += 1


print(int(oxygen_generator[0],2))
print(int(co2_scrubber[0],2))
print(int(oxygen_generator[0],2) * int(co2_scrubber[0],2))
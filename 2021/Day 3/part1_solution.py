bin_ones = None
bin_zeros = None

gamma = ''
epsilon = ''

with open("2021/Day 3/input_data.txt",'r') as input_data:
    for line in input_data:
        if bin_ones is None:
            bin_ones = [0] * len(line)
            bin_zeros = [0] * len(line)
        for ind in range(len(line)-1):
            if line[ind]=='0': 
                bin_zeros[ind]=bin_zeros[ind]+1
            else:
                bin_ones[ind]=bin_ones[ind]+1

for counts in range(len(bin_ones)-1):
    if bin_ones[counts] > bin_zeros[counts]:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

print(int(gamma,2) * int(epsilon,2))
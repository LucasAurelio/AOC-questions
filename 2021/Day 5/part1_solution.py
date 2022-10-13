from calendar import c


starts = []
ends = []

marked_points = {}

def marks_point(current_point):
    if current_point in marked_points:
        marked_points[current_point] = marked_points[current_point] + 1
    else:
        marked_points[current_point] = 1

with open("2021/Day 5/input_data.txt",'r') as input_data:

    for line in input_data:
        start_end = line.strip().split('->')
        start_line = start_end[0].split(',')
        end_line = start_end[1].split(',')
        starts.append(start_line)
        ends.append(end_line)


for double_index in range(len(starts)):
    x1 = int(starts[double_index][0])
    y1 = int(starts[double_index][1])

    x2 = int(ends[double_index][0])
    y2 = int(ends[double_index][1])

    start_loop = None
    end_loop = None

    if x1 == x2:
        if y1<=y2:
            start_loop = y1
            end_loop = y2
        else:
            start_loop = y2
            end_loop = y1

        for y in range(start_loop,end_loop+1):
            current_position = f"{x1},{y}"
            marks_point(current_position)
    elif y1 == y2:
        if x1<=x2:
            start_loop = x1
            end_loop = x2
        else:
            start_loop = x2
            end_loop = x1

        for x in range(start_loop,end_loop+1):
            current_position = f"{x},{y1}"
            marks_point(current_position)

total_count = 0
for element in marked_points:
    if marked_points[element] >= 2:
        total_count += 1

print(total_count)
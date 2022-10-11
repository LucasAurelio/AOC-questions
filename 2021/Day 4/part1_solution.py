bingo_numbers = []

cards = []

def update_cards(drawnnumber):
    for card in range(len(cards)):
        for row in range(len(cards[card])):
            for number in range(len(cards[card][row])):
                if int(cards[card][row][number]) == drawnnumber:
                    cards[card][row][number] = 1000

def find_winner():
    card_in = 0
    column_in = 0
    columns = [0,0,0,0,0]
    row_count = 0
    for card in cards:
        for row in card:
            for number in row:
                if number == 1000:
                    row_count += 1
                    columns[column_in] += 1
                column_in += 1
            column_in = 0
            if row_count == 5:
                return True, card_in
            row_count = 0

        for count in columns:
            if count == 5:
                return True, card_in
        columns = [0,0,0,0,0]

        card_in += 1
    
    return False, None


with open("2021/Day 4/input_data.txt",'r') as input_data:
    bingo_numbers = input_data.readline().strip().split(',')

    current_card = []
    rows_control = 0
    for line in input_data:
        
        if line.strip() != '':
            current_card.append(line.replace('  ',' ').strip().split(' '))
            rows_control += 1

        if rows_control == 5:
            cards.append(current_card)
            current_card = []
            rows_control = 0


count_drawns = 0
last_drawn = None
winner_card = None
has_winner = False
for number in bingo_numbers:
    update_cards(int(number))
    if count_drawns >= 5:
        has_winner, winner_card = find_winner()
    
    last_drawn = int(number)

    if has_winner:
        break
    
    count_drawns += 1

total_sum = 0

if has_winner:
    for row in cards[winner_card]:
        for number in row:
            if number != 1000:
                total_sum += int(number)

print(last_drawn*total_sum)
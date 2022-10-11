bingo_numbers = []
cards = []
has_won = []

def update_cards(drawnnumber):
    card_in = 0
    for card in range(len(cards)):
        if card_in not in has_won:
            for row in range(len(cards[card])):
                for number in range(len(cards[card][row])):
                    if int(cards[card][row][number]) == drawnnumber:
                        cards[card][row][number] = 1000
        card_in += 1

def find_winner():
    card_in = 0
    column_in = 0
    columns = [0,0,0,0,0]
    row_count = 0

    won = False

    for card in cards:
        if card_in not in has_won:
            for row in card:
                for number in row:
                    if number == 1000:
                        row_count += 1
                        columns[column_in] += 1
                    column_in += 1
                column_in = 0
                if row_count == 5:
                    has_won.append(card_in)
                    won = True
                row_count = 0

            for count in columns:
                if count == 5:
                    has_won.append(card_in)
                    won = True
            columns = [0,0,0,0,0]
        card_in += 1
    
    return won


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
has_winner = None
total_sum = 0

for number in bingo_numbers:
    has_winner = False
    update_cards(int(number))

    if count_drawns >= 5:
        has_winner = find_winner()

        if has_winner == True:
            total_sum = 0
            winner_card = has_won[-1]
            last_drawn = int(number)
            for row in cards[winner_card]:
                for number in row:
                    if number != 1000:
                        total_sum += int(number)
    
    count_drawns += 1

print(last_drawn*total_sum)
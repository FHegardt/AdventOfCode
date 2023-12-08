import regex as re
file = open('input7.txt', 'r')
from functools import cmp_to_key

five_oac = []
four_oac = []
full_house = []
three_oac = []
two_pair = []
pair = []
high_card = []
card_strength = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, 
                 '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
sorted_card_list = [five_oac,four_oac,full_house,three_oac,two_pair,pair,high_card]

def compare_hands(hand1, hand2):

    strength_hand1 = [card_strength[c] for c in hand1]
    strength_hand2 = [card_strength[c] for c in hand2]


    for c1, c2 in zip(strength_hand1, strength_hand2):
        if c1 > c2:
            return 1  
        elif c1 < c2:
            return -1  
    return 0 

cards_with_value_list = []

while True:
    line = file.readline()
    if not line:
        break
    
    cards = line[0:5]
    cards_with_value_list.append([cards, re.findall("\d+",line[6:10])])
    counter = [cards.count(cards[i]) for i in range(len(cards))]

    if 5 in counter:
        five_oac.append(cards)
    elif 4 in counter:
        four_oac.append(cards)
    elif 3 in counter:
        if 2 in counter:
            full_house.append(cards)
        else:
            three_oac.append(cards)
    elif 2 in counter:
        if counter.count(2) == 4:
            two_pair.append(cards) 
        else:
            pair.append(cards)
    else:
        high_card.append(cards)

for i in range(len(sorted_card_list)):
    if len(sorted_card_list[i]) > 1:
        sorted_card_list[i] = sorted(sorted_card_list[i], key=cmp_to_key(compare_hands), reverse=True)
 



counter_adder = len(cards_with_value_list)
answer = 0

for sorted_card in sorted_card_list:
    if len(sorted_card) > 0:
        for current_card in sorted_card:
            for values in cards_with_value_list:
                if values[0] == current_card:
                    answer += (int(values[1][0])*counter_adder)
                    counter_adder -= 1
                    print(counter_adder)
                    break

print(answer)

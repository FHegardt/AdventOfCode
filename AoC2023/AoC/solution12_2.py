import regex as re
file = open('input12_2.txt', 'r')
answer = 0
import itertools

combinations_counter = 0
line_co = 0


while True:
    #print(line_co)
    line_co+=1
    line = file.readline()
    if not line:
        break

    values_to_match = []
    unfixed_values = list(map(int, re.findall("-?\d+",line)))
    


    #damaged_springs = [spring for spring in re.findall("[?.#]+", line)[0]]
    damaged_springs = []
    
    springs = re.findall("[?.#]+", line)

    
    for a in range(5):
        for values in unfixed_values:
            values_to_match.append(values)
        for b in range(len(springs[0])):
            damaged_springs.append(springs[0][b])
        if a <4:
            damaged_springs.append("?")

    questionmark_positions = [index for index, char in enumerate(damaged_springs) if char == '?']
    square_sum = len([dama for dama in damaged_springs if dama == '#'])
    pos_sum = sum(values_to_match) - square_sum
    
    positions = range(len(questionmark_positions))
    hash_positions = itertools.combinations(positions, pos_sum)

    for pos in hash_positions:
        combos = ['.' if i not in pos else '#' for i in range(len(questionmark_positions))]
        print(combos)
        counter = 0
        added_value = 0
        actual_values = []
        for damage in damaged_springs:
            if damage == '?':
                damage = combos[0]
                combos.pop(0)
            if damage == '#':
                counter +=1
            elif counter > 0:
                if len(actual_values) == len(values_to_match):
                    break
                if counter != values_to_match[added_value]:
                    break
                actual_values.append(counter)
                counter = 0
                added_value+=1

        if counter > 0:
            actual_values.append(counter)
            counter = 0
        if actual_values == values_to_match:
            answer+=1

    print(answer)
        



print(answer)
    
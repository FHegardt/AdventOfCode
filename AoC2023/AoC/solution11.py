import regex as re
file = open('input11.txt', 'r')
answer = 0

expanded_galaxy_positions = []
line_counter = 0
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

while True:
    line = file.readline()
    if not line:
        break
    if '#' not in line:
        line_counter +=2
    else:
        hash_positions = [index for index, char in enumerate(line) if char == '#']
        for hash in hash_positions:
            expanded_galaxy_positions.append([line_counter,hash])
        line_counter+=1


position_one_list = []
empty_row_list = []
for galaxy_positions in expanded_galaxy_positions:
    position_one_list.append(galaxy_positions[1])

for i in range(len(expanded_galaxy_positions)+1):
    if i not in position_one_list:
        empty_row_list.append(i)

for new_galaxy_positions in expanded_galaxy_positions:
    curr_count = 0
    for row in empty_row_list:
        if new_galaxy_positions[1] > row:
            curr_count +=1
    new_galaxy_positions[1] +=curr_count
    




for a in range(len(expanded_galaxy_positions)):
    for b in range(a+1,len(expanded_galaxy_positions)):
        answer += manhattan(expanded_galaxy_positions[a], expanded_galaxy_positions[b])



print(answer)
        



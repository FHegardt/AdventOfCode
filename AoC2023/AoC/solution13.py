import regex as re
from collections import Counter
import math

def find_duplicates_indices(lst):
    seen = {}
    duplicate_indices = set()

    for i, sublist in enumerate(lst):
        tuple_sublist = tuple(sublist)

        if tuple_sublist in seen:
            
            duplicate_indices.add(i)
            duplicate_indices.add(seen[tuple_sublist])
        else:
            seen[tuple_sublist] = i

    
    return sorted(list(duplicate_indices))
answer = 0

file = open('input13.txt', 'r')
ash_rock = []


while True:
    line = file.readline()
    if not line:
        break
    if len([index for index, char in enumerate(line) if char == '#']) > 0:
        ash_rock.append([index for index, char in enumerate(line) if char == '#'])
    else:
        transposed_dict = {}
        for row_index, sublist in enumerate(ash_rock):
            for col_index in sublist:
                transposed_dict.setdefault(col_index, []).append(row_index)
                transposed_list = [transposed_dict[i] for i in sorted(transposed_dict.keys())]
        if len(find_duplicates_indices(transposed_list)) > len(find_duplicates_indices(ash_rock)):
            answer +=(find_duplicates_indices(transposed_list)[int(len(find_duplicates_indices(transposed_list))/2)])
        elif len(find_duplicates_indices(transposed_list)) < len(find_duplicates_indices(ash_rock)):
            answer +=(find_duplicates_indices(ash_rock)[int(math.ceil(len(find_duplicates_indices(ash_rock))/2))])*100
            print((find_duplicates_indices(ash_rock)), (find_duplicates_indices(ash_rock)[int(math.ceil(len(find_duplicates_indices(ash_rock))/2))]))
        ash_rock = []

transposed_dict = {}
for row_index, sublist in enumerate(ash_rock):
    for col_index in sublist:
        transposed_dict.setdefault(col_index, []).append(row_index)
        transposed_list = [transposed_dict[i] for i in sorted(transposed_dict.keys())]
if len(find_duplicates_indices(transposed_list)) > len(find_duplicates_indices(ash_rock)):
    answer += (find_duplicates_indices(transposed_list)[int(len(find_duplicates_indices(transposed_list))/2)])
elif len(find_duplicates_indices(transposed_list)) < len(find_duplicates_indices(ash_rock)):
    answer +=(find_duplicates_indices(ash_rock)[int(len(find_duplicates_indices(ash_rock))/2)])*100
    print(len(find_duplicates_indices(ash_rock)))
    

print(answer)
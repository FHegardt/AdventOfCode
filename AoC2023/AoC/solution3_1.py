import regex as re

def is_hitting_character(schematic, row, col):

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue  

            adj_row, adj_col = row + dr, col + dc
            if 0 <= adj_row < len(schematic) and 0 <= adj_col < len(schematic[adj_row]):
                if re.search('[^.\d]', schematic[adj_row][adj_col]):
                    return True
    return False

def calc_sum(schematic):
    total_sum = 0
    for row in range(len(schematic)):
        for match in re.finditer(r'\d+', schematic[row]):
            start, end = match.span()

            if any(is_hitting_character(schematic, row, col) for col in range(start, end)):
                total_sum += int(match.group())
    return total_sum


with open('input3.txt', 'r') as file:
    schematic = [line.strip() for line in file]


total_sum = calc_sum(schematic)
print(total_sum)


import regex as re
file = open('input4.txt', 'r')
answer1 = 0
answer2 = 0
moving_list = []


while True:
    line = file.readline()
    if not line:
        break

    if len(moving_list) == 0:
        moving_list.append(0)
    curr_copies = moving_list[0]+1
    moving_list.pop(0)

    first_split = line.split("|")
    second_split = first_split[0].split(":")
    my_numbers, winning_numbers = re.findall(r'\d+', first_split[1]), re.findall(r'\d+', second_split[1])
    hits = sum(winners in my_numbers for winners in winning_numbers)

    if hits > 0:
        answer1 += (2**(hits-1))
    answer2 +=curr_copies
    
    for i in range(hits):
        try:
            moving_list[i] +=curr_copies
        except:
            moving_list.append(curr_copies)

print(f"First answer: {answer1}. Second answer: {answer2}")

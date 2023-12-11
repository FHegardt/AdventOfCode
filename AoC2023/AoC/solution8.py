import regex as re
file = open('input8.txt', 'r')


first_line = True
letter_dict = {}

while True:
    line = file.readline()
    if not line:
        break
    if first_line:
        instructions = str(line)
        first_line = False
        print(instructions)
    else:
        letter_dict.update({line[0:3]:[line[7:10],line[12:15]]})

current_letters = "MQF"
counter = 0
zzz_not_found = True
while zzz_not_found:
    for i in range(len(instructions)):
        if instructions[i] == "L":
            current_letters = letter_dict[current_letters][0]
            counter +=1
        elif instructions[i] == "R":
            current_letters = letter_dict[current_letters][1]
            counter +=1
        if current_letters == "ZZZ":
            print(counter)
            zzz_not_found = False
            break
        


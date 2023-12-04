import regex as re

choice = input("Player 456, make your choice! Press '1' for first part or '2' for second part:")

file = open('input1.txt', 'r')
answer = 0

number_dict = {"one": 1, "1": 1, "two": 2, "2": 2, "three": 3, "3": 3, "four": 4, "4": 4, "five": 5, "5": 5,
                "six": 6,"6": 6, "seven": 7, "7": 7, "eight": 8,"8": 8, "nine": 9, "9": 9}


while True:
    line = file.readline()
    if not line:
        break
    if choice == '1':
        new_line = ''.join(filter(str.isdigit, line))
    elif choice == '2':
        new_line = re.findall('|'.join(number_dict), line, overlapped=True)
    else:
        print("Player 456, you fucked this up. You fucked this up so bad.")
        break
    answer+= int(str(number_dict[new_line[0]]) + str(number_dict[new_line[-1]]))
   
print(f"Answer: {answer}")
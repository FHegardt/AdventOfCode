import regex as re
answer = 0

for a in range(100):
    with open('input14.txt', 'r') as file:
        rows = [line[a] for line in file]
        circle_index = ([index for index, char in enumerate(rows) if char == 'O'])
        square_index = ([index for index, char in enumerate(rows) if char == '#'])
        for i in range(len(circle_index)):
            circle_stop = True
            down_counter = 1
            while circle_stop:
                if (circle_index[i] - down_counter) in square_index or (circle_index[i] - down_counter) in circle_index or (circle_index[i]-down_counter) <0:
                    circle_index[i] = (circle_index[i]-down_counter)+1
                    answer += (len(rows) - circle_index[i])
                    break
                down_counter +=1

print(answer)
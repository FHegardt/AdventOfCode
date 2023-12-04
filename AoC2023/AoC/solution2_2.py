import regex as re

file = open('input2.txt', 'r')
counter = 0
colours = ["blue","green","red"]
answer =1 

while True:
    line = file.readline()
    power_sets = 1

    if not line:
        break
    for i in range(3):
        finder =[int(line[(m.start(0)-3):(m.start(0)-1)]) for m in re.finditer(colours[i], line)]
        power_sets *= max(finder)
        if max(finder) < 2:
            print(max(finder))


    answer += power_sets

print(answer-1)

    


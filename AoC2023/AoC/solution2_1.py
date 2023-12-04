import regex as re

file = open('input2.txt', 'r')
counter = 0
colours = ["blue","green","red"]
values = [14,13,12]
answer = 0

while True:
    counter +=1
    line = file.readline()
    correct = True
    if not line:
        break

    for i in range(3):
        finder =[int(line[(m.start(0)-3):(m.start(0)-1)]) for m in re.finditer(colours[i], line)]
        for f in finder:
            if f > values[i]:
                correct = False
    if correct:
        answer += counter

print(answer)

    


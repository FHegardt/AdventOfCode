import regex as re
file = open('input6.txt', 'r')

counter = 0
time_and_record = []
answer = 1
while True:
    line = file.readline()
    if not line:
        break
    time_and_record.append(list(map(int, re.findall("\d+",line))))

for a in range(len(time_and_record[0])):
    counter = 0
    for b in range(time_and_record[0][a]):
        if (time_and_record[0][a]-b)*b > time_and_record[1][a]:
            counter +=1
    answer *= counter
print(answer)

import regex as re
moving_list = []
file = open('input5.txt', 'r')

soil_list = []
fertilizer_list = []
water_list = []
light_list = []
temp_list = []
humid_list = []
location_list = []
list_holder = [soil_list,fertilizer_list,water_list,light_list,temp_list,humid_list,location_list]
counter = -2
seed_list_null = True

while True:
    counter += 0
    line = file.readline()
    if not line:
        break
    if seed_list_null:
        seed_list = list(map(int, re.findall("\d+",line)))
        seed_list_null = False

    if len(re.findall("[a-zA-Z]", line))>0:
        counter +=1
    
    numbers = re.findall("\d+",line)
    if len(numbers) ==3:
        numbers = list(map(int, numbers))
        list_holder[counter].append(numbers)


for i in range(len(seed_list)):
    for lists in list_holder:
        for list_numbers in lists:
            if seed_list[i] in range(list_numbers[1], (list_numbers[1]+list_numbers[2])):
                seed_list[i] =seed_list[i]+(list_numbers[0]-list_numbers[1])
                break

print(min(seed_list))


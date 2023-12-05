
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
seed_list=[]

while True:
    line = file.readline()
    if not line:
        break
    if seed_list_null:
        old_seed_list = list(map(int, re.findall("\d+",line)))
        for a in range(int(len(old_seed_list)/2)):
            seed_list.append([old_seed_list[a*2], old_seed_list[a*2]+old_seed_list[a*2+1]-1]) 
        seed_list_null = False

    if len(re.findall("[a-zA-Z]", line))>0:
        counter +=1
    
    numbers = re.findall("\d+",line)
    if len(numbers) ==3:
        numbers = list(map(int, numbers))
        list_holder[counter].append(numbers)


for i in range(len(seed_list)):
    curr_seed_list = [[seed_list[i][0], seed_list[i][1]]]
    for lists in list_holder:
        new_list = []
        for list_numbers in lists:
            curr_low, curr_high = list_numbers[1], (list_numbers[1]+list_numbers[2])

            for count_seed, curr_seed in enumerate(curr_seed_list):
                if curr_seed[0] in range(curr_low, curr_high+1) and curr_seed[1] in range(curr_low, curr_high):
                    new_list.append([curr_seed[0]+(list_numbers[0]-list_numbers[1]),curr_seed[1]+(list_numbers[0]-list_numbers[1])])
                    curr_seed_list.pop(count_seed)
                    
                elif curr_seed[0] in range(curr_low, curr_high+1):
                    new_list.append([curr_seed[0]+(list_numbers[0]-list_numbers[1]),curr_high+(list_numbers[0]-list_numbers[1])])
                    curr_seed[0] = curr_high
                    
                elif curr_seed[1] in range(curr_low, curr_high+1):
                    new_list.append([curr_low+(list_numbers[0]-list_numbers[1]),curr_seed[1]+(list_numbers[0]-list_numbers[1])])
                    curr_seed[1] = curr_low
                    
                elif curr_seed[0] < curr_low and curr_seed[1] > curr_high:
                    new_list.append([curr_low+(list_numbers[0]-list_numbers[1]),curr_high+(list_numbers[0]-list_numbers[1])])
                    curr_seed_list.append([curr_seed[0], curr_low])
                    curr_seed_list.append([curr_high, curr_seed[1]])
                    curr_seed_list.pop(count_seed)
                    break

        for news in new_list:
            curr_seed_list.append(news)
    print(min(curr_seed_list))




import regex as re
file = open('input8.txt', 'r')
answer = 0

def get_distance(p1,p2):
     return abs((p1) - (p2))

while True:
    line = file.readline()
    if not line:
        break
    
    initial_list = [(list(map(int, re.findall("-?\d+",line))))]
    continiue_to_run = True
    counter = 0
    
    while continiue_to_run:
        temp_list = []
        for i in range(len(initial_list[counter])-1):
            temp_list.append(initial_list[counter][i+1]-initial_list[counter][i])
        
   

        initial_list.append(temp_list)
        counter +=1
        if all(v == 0 for v in temp_list):
            continiue_to_run = False
  
    
    last_value = 0
    initial_list.reverse()
    print(initial_list)
    for ini_list in initial_list:
 
        next_value = ini_list[0]-last_value
        print(ini_list[0])
        ini_list.insert(0, next_value)
        last_value = ini_list[0]
    
    answer += next_value
        
print(answer)




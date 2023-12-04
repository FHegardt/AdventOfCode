import regex as re

file = open('input3.txt', 'r')
new_file = [f for f in file]
answer = 0


for a in range(len(new_file)):
        cha_pos = [m.start() for m in re.finditer('\*', new_file[a])]
        if a>0:
            last_nombas = [[m.start(),m.end()-1] for m in re.finditer(r'\d+',new_file[a-1])]
        else:
            last_nombas = [[]]
        curr_nombas = [[m.start(),m.end()-1] for m in re.finditer(r'\d+',new_file[a])]
        if a<len(new_file)-1:
            next_nombas = [[m.start(),m.end()-1] for m in re.finditer(r'\d+',new_file[a+1])]
        else:
            next_nombas =[[]]
        row_list = [last_nombas,curr_nombas,next_nombas]
        for pos in cha_pos:
            curr_value = 0
            counter = 0
            row_counter = -2
            for rows in row_list:
                row_counter +=1
                for nomb in rows:
                    if pos in nomb or pos+1 in nomb or pos-1 in nomb:
                        if counter > 0:
                            if int(nomb[1])-(nomb[0]) == 0:
                                value2=int(new_file[a+row_counter][nomb[0]])
                            else:
                                value2=int(new_file[a+row_counter][nomb[0]:nomb[1]+1])
                        else:
                            if int(nomb[1])-(nomb[0]) == 0:
                                value1=int(new_file[a+row_counter][nomb[0]])
                            else:
                                value1=int(new_file[a+row_counter][nomb[0]:nomb[1]+1])
                        counter+=1
            if counter ==2:
                print(value1, value2)
                curr_value = value1*value2
                answer += curr_value

print(answer)          
        


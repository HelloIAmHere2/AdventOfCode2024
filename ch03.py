#ch03

file_path = 'ch3input.txt'

with open(file_path, 'r') as file:
    file_content = file.read()
    
list = file_content.split('\n')

#print(list)

lst1 = []
lst2 = []

for i in range(len(list)):
    temparr = []
    temparr2 = []
    temparr.append(list[i].split(' '))
    #print(temparr)
    for j in range(len(temparr[0])):
        temparr2.append(int(temparr[0][j]))
    #print(temparr2)
    lst1.append(temparr2)

#print(lst1)


safecount = 0

for i in lst1:
    increase = 1
    decrease = 1
    gradual = 1
    
    #check for increase
    jj = i[0]
    for j in range(1, len(i)):
        if jj>i[j]:
            increase = 0
        jj = i[j]
            
    #check for decrease
    jj = i[0]
    for j in range(1, len(i)):
        if jj<i[j]:
            decrease = 0
        jj = i[j]    
            
    #check for gradual
    jj = i[0]
    for j in range(1, len(i)):
        if abs(jj-i[j])>3 or abs(jj-i[j])<1:
            gradual = 0
        jj = i[j]
            
    if bool(gradual) & ( bool(increase) ^ bool(decrease)):
        safecount += 1
        print(gradual, increase, decrease)
        print(i)
    
    

print(safecount)
            
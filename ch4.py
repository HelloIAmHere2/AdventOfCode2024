#ch4

#open file and read to file_content
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

#track how many reports are safe
safecount = 0


#iterate through list of reports
for z in lst1:
    #safe is set to 1 if any arrangement of a report is safe
    safe = 0
    
    #iterate through different configurations of a report
    for i in range(len(z)):
        tmplist = []
        
        for k in range(len(z)):
            if k != i:
                tmplist.append(z[k])
        
        print(tmplist)
        
        increase = 1
        decrease = 1
        gradual = 1
    
        #check for increase
        jj = tmplist[0]
        for j in range(1, len(tmplist)):
            if jj>tmplist[j]:
                increase = 0
            jj = tmplist[j]
    
        #check for decrease
        jj = tmplist[0]
        for j in range(1, len(tmplist)):
            if jj<tmplist[j]:
                decrease = 0
            jj = tmplist[j]    
                
        #check for gradual
        jj = tmplist[0]
        for j in range(1, len(tmplist)):
            if abs(jj-tmplist[j])>3 or abs(jj-tmplist[j])<1:
                gradual = 0
            jj = tmplist[j]
                
        if bool(gradual) & ( bool(increase) ^ bool(decrease)):
            safe = 1
            #print(gradual, increase, decrease)
            #print(i)
            
    if safe == 1:
        safecount +=1
    
    

print(safecount)
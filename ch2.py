#ch01

file_path = 'ch1input.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

#print(file_content)
list = file_content.split()

#print(list)

#declare lists for holding coordinates
lst1 = []
lst2 = []
ans = 0


#format data
for i in range(len(list)):
    if i%2  == 0:
        lst1.append(int(list[i]))
    else:
        lst2.append(int(list[i]))
#print(lst1)

for i in lst1:
    count = 0
    for j in lst2:
        if i == j:
            count+=1
    ans+=i*count
print(ans)
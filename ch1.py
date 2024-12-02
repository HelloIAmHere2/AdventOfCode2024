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
lst3 = []

for i in range(len(list)):
    if i%2  == 0:
        lst1.append(int(list[i]))
    else:
        lst2.append(int(list[i]))
#print(lst1)

#rearrange lists to correct order

lst1.sort()
lst2.sort()

for i in range(len(lst1)):
    lst3.append(abs(lst1[i]-lst2[i]))
    
print(lst3)

print(sum(lst3))
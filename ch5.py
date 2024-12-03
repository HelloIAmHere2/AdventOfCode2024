#ch5
import re

#open file and read to file_content
file_path = 'ch5input.txt'

with open(file_path, 'r') as file:
    file_content = file.read()
 
#find all mul functions   
x = re.findall("mul\(\d+\,\d+\)", file_content)

#calculate mul functions
sum = 0
for i in x:
    z = re.findall("\d+", i)
    a = int(z[0])
    b = int(z[1])
    sum += a*b
    #print(a)
    #print(b)
    #print(a*b)
    
print(sum)
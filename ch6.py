#ch6
import re

# function takes a string and appends a substring of that split on "dont'" and calls dontsplit()
def dosplit(n):
    y = re.split("don\'t\(\)", n, 1)
    lst.append(y[0])
    try:
        dontsplit(y[1])
    except IndexError:
        return

#function takes a string and splits overything before "do()" and recalls dosplit() 
def dontsplit(n):
    y = re.split("do\(\)", n, 1)
    try:
        dosplit(y[1])
    except IndexError:
        return

#open file and read to file_content
file_path = 'ch5input.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

lst = []
dosplit(file_content)
 
#find all mul functions   
x = re.findall("mul\(\d+\,\d+\)", "".join(lst))

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
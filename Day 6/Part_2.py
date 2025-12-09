from math import prod
f = open("input.txt")
line=[]
for l in f:
    l = l.rstrip("\n")
    line.append(l)
pre_process = []
for index in range(len(line[0])-1, -1 ,-1):
    temp=[]
    for row in line:
        temp.append(row[index])
    if (all(x == " " for x in temp) == False) : pre_process.append(temp)

temp=[]
process = []
temp = []
sum_prod = 0
for row in pre_process:
    if ( row[-1] == "+"):
        temp.append(int("".join(row[: len(row) - 1]).rstrip("\n")))
        sum_prod = sum_prod + sum(temp)
        temp=[]
    elif (row[-1] == "*"):
        temp.append(int("".join(row[: len(row) - 1]).rstrip("\n")))
        sum_prod = sum_prod + prod(temp)
        temp = []
    else:
        temp.append(int("".join(row[: len(row) - 1]).rstrip("\n")))
print("Final : ",sum_prod)
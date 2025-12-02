pos = 50
count = 0
f = open("my_input.txt")
for line in f:
    command = line.rstrip()
    if command[0] == "R":
        pos = (pos + int(command[1:])) % 100
        if(pos == 0): count = count+1
    else:
        pos = (pos - int(command[1:]))%100
        if(pos == 0): count = count+1
print(pos,",",count)

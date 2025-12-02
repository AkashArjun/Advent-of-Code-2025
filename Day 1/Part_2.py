pos = 50
past_pos = pos
rotation = 0
count = 0
f = open("input.txt")
for line in f:
    command = line.rstrip()
    if command[0] == "R":

        rotation = rotation + (int(command[1:])) // 100
        pos = pos + int(command[1:])%100
        if(pos < 0 or pos > 100): 
            if(past_pos != 0 ):
                count = count+1
        pos = pos % 100
        if(pos == 0 ): count = count+1
    else:

        rotation = rotation + (int(command[1:])) // 100
        pos = pos - int(command[1:])%100
        if(pos < 0 or pos > 100): 
            if past_pos != 0 :
                count = count+1
        pos = pos % 100
        if(pos == 0 ): count = count+1
    past_pos = pos
    #print(command," past pos = ",past_pos, " count = ", count, " rotation = ", rotation)
count = count + rotation
print(count)
# print(rotation)

f = open("input.txt")
sum = 0
def largest_jolt(line):
    stack = []
    delete = len(line)-12
    for i in range(0,len(line)):
        element = int(line[i])
        if delete >0 :
            for j in  list(reversed(stack)): # reversing the stack
                if element > j :
                    stack.pop()
                    delete = delete -1
                    if delete <= 0 : break
        stack.append(element)
    return int("".join(str(n) for n in stack[:12])) # skips irrelevant digits at end in case of repitition
    


for line in f:
    line = line.strip()
    sum = sum + largest_jolt(line)

print(sum)
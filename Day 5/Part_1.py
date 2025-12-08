f = open("input.txt")
i = 0
blank = 0
lines = []
fresh = set()
for line in f:
    line = line.rstrip("\n")
    lines.append(line)
    if line == "":
        blank = i
    i += 1

for idx in range(blank+1, i):
    for j in range(0,blank):
        l,u =lines[j].split("-")
        l = int(l)
        u = int(u)
        if (int(lines[idx]) >= l and int(lines[idx]) <= u ):
            fresh.add(int(lines[idx]))
print(len(fresh))

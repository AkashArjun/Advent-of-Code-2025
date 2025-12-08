f = open("input.txt")
i = 0
blank = 0
lines = []
fresh = []
for line in f:
    line = line.rstrip("\n")
    lines.append(line)
    if line == "":
        blank = i
    i += 1

for j in range(0,blank):
    l,u =lines[j].split("-")
    l,u = int(l),int(u)
    fresh.append([l,u])

fresh = sorted(fresh, key=lambda x: x[0])

curr = fresh[0]
union = [curr]
for interval in fresh:
    l,u = interval[0],interval[1]
    if (l <= curr[1]):
        curr[1] = max(curr[1],u)
    else:
        curr = interval
    union.append(curr)
union = set(map(tuple, union))
num_igred = 0
for i in union:
    num_igred += i[1]-i[0]+1

print(num_igred)

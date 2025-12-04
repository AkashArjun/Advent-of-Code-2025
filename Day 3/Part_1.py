f = open("input.txt")
sum = 0


def largest_jolt(line):
    max = 0
    for i in range(len(line)):
        f = int(line[i])
        for j in range(i, len(line)):
            if (max < (f*10 +int(line[j])) and i!= j):
                max = f * 10 + int(line[j])

    return max


for line in f:
    line = line.strip()
    sum = sum + largest_jolt(line)

print(sum)

with open("input.txt", "r") as f:
    contents = f.read()
sum = 0
range_num = contents.split(",")


def sum_of_invalid_in_range(r):
    u, l = int(r.split("-")[0]), int(r.split("-")[1])
    s = 0
    for i in range(u, l + 1):
        if digit_repeat(i) == True:
            s = s + i
    return s


def digit_repeat(num):
    for k in range(1, len(str(num))):
        counter = 0
        copy = num
        equal_block = copy % (10**k)
        while copy > 0:
            if equal_block != copy % (10**k):
                copy = 0
            else:
                counter = counter + 1
            copy = (int)((copy - equal_block) / (10**k))
        if counter * k == len(str(num)):
            return True

    return False


for i in range_num:
    sum = sum + sum_of_invalid_in_range(i)
print(sum)

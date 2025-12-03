with open("input.txt", "r") as f:
    contents = f.read()
sum = 0
range_num = contents.split(",")


def sum_of_invalid_in_range(r):
    u, l = int(r.split("-")[0]), int(r.split("-")[1])
    s = 0
    for i in range(u, l + 1):
        if (digit_repeat(i) == True):
            s = s+ i
    return s

def digit_repeat(num):
    if(len(str(num)) % 2 == 1): return False
    second_half =int(num % (10 ** (len(str(num))/2)))
    first_half = int((num - second_half) / (10 ** (len(str(num)) / 2)))
    if first_half == second_half : 
        return True
    else : 
        return False

for i in range_num:
    sum = sum + sum_of_invalid_in_range(i)
    


print(sum)




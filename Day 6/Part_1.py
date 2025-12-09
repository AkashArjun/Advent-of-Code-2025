f = open("sample_input.txt")
matrix = []
result = []
for line in f:
    line = line.split()
    try:
        line = list(map(int, line))
        matrix.append(line)
    except ValueError:
        matrix.append(line)
print((matrix))
print("row : ",len(matrix))
print("col : ",len(matrix[0]))
for i in matrix:
    print(i)
first = matrix[0][0]
for col in range(len(matrix[0])):
    first = matrix[0][col]
    for row in range(1,len(matrix)-1):
        if(matrix[-1][col] == "+"):
            first = first + matrix[row][col]
        else:
            first = first * matrix[row][col]
    result.append(first)
print(sum(result))

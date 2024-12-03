# 1
file = open('Сучкова Дарья Владиммровна_У244_vvod.txt', 'r')

matrix = []
for line in file:
    row = list(map(int, line.split()))
    matrix.append(row)

file.close()

size = len(matrix)
max_rows = str([max(row) for row in matrix])
min_columns = str([min(matrix[i][j] for i in range(size)) for j in range(size)])

file2 = open('Сучкова Дарья Владиммровна_У244_vivod.txt', 'w')

file2.write("Наибольшие элементы в каждой строке: ")
file2.write(max_rows)
file2.write("\nНаименьшие элементы в каждом столбце: ")
file2.write(min_columns)
file2.write('\n')



#2
from random import shuffle, randint
N = int(input())
b = [[randint(10,99) for i in range(N)] for j in range(N)]
shuffle(b)

for i in b:
    print(i)
print()
 
a = sum(b, [])
max1 = max(a[::N+1])
max2 = max(a[N-1::N-1][:N])

if max1 > max2:
    i1 = j1 = a[::N+1].index(max1)
else:
    i1 = a[N-1::N-1][:N].index(max2)
    j1 = N - 1 - i1
b[N//2][N//2], b[i1][j1] = b[i1][j1], b[N//2][N//2]

for i in b:
    file2.write(' '.join(map(str, row)) + '\n')

file2.close()

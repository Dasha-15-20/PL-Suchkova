# 1
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# size = len(matrix)
# max_rows = [max(row) for row in matrix]
# min_columns = [min(matrix[i][j] for i in range(size)) for j in range(size)]

# print("Наибольшие элементы в каждой строке:", max_rows)
# print("Наименьшие элементы в каждом столбце:", min_columns)


#2
# from random import shuffle, randint
# N = int(input())
# b = [[randint(10,99) for i in range(N)] for j in range(N)]
# shuffle(b)

# for i in b:
#     print(i)
# print()
 
# a = sum(b, [])
# max1 = max(a[::N+1])
# max2 = max(a[N-1::N-1][:N])

# if max1 > max2:
#     i1 = j1 = a[::N+1].index(max1)
# else:
#     i1 = a[N-1::N-1][:N].index(max2)
#     j1 = N - 1 - i1
# b[N//2][N//2], b[i1][j1] = b[i1][j1], b[N//2][N//2]
 
# for i in b:
#     print(i)
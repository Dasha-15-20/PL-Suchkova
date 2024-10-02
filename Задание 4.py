# #7
# n = int(input())
# sum = 0
# factorial = 1

# for i in range(1,n + 1):
#     factorial *= i
#     sum += factorial

# print(sum)

#8
# n = int(input())

# for i in range(1, n+1):
#     for k in range(1, i+1):
#         print(k, sep='', end='')
#     print()

#9
# N = int(input())
# feb1 = 0
# feb2 = 1
# sum = 0

# for i in range(N):
#     sum += feb1
#     feb1, feb2 = feb2, feb2 + feb1

# print(sum)    
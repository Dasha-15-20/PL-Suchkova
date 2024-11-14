# #1
# def gcd(A, B):
#     while B != 0:
#         A, B = B, A % B
#     return A
    
# def lcm(A, B):
#     return (a * b)//gcd(A, B)

# a = int(input('Введите натуральное число:'))
# b = int(input('Введите натуральное число:'))
# nod = gcd(a, b)
# nok = lcm(a, b)

# print('НОД:', nod)
# print('НОК:', nok)


# #2
# a = int(input("Введите сторону а:"))
# b = int(input("Введите сторону b:"))
# c = int(input("Введите сторону c:"))
# f = int(input("Введите сторону f:"))
# d = int(input("Введите диагональ:"))

# if a < (b+c+f) and b < (a+c+f) and c < (a+b+f) and f < (a+b+c):
#     p1 = (a+b+d) / 2
#     p2 = (d+c+f) / 2
#     abd = ((p1 - a)*(p1 - b)*(p1 - d))**(1/2)
#     cfd = ((p2 - c)*(p2 - f)*(p2 - d))**(1/2)
#     S = abd + cfd
#     print(S)
# else:
#     print("Такого четырёхугольника не существует!")
    

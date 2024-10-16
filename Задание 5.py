numbers = []

while True:
    a = int(input('Введите число:'))
    if a == 0:
        break
    numbers.append(a)
    
print(sum(numbers)/len(numbers))
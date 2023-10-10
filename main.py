# Задача «Ряд - 1»
'''
a = int(input('Это значение должно быть меньше второго: '))
b = int(input('Введите второе значение: '))

for i in range(a,b+1):
    print(i)
'''

# Задача «Ряд - 2»
'''
a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))

if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
'''

# Задача «Сумма N чисел»

'''
n = int(input('Введите количество чисел: '))

sum = 0

for i in range(n):
    sum += int(input('Введите значение для переменной: '))
    print(sum)
'''

# Задача «Факториал»
'''
a = 1
n = int(input('Введите число: '))
for i in range(1, n + 1):
    a *= i
print(a)
'''

# Задача «Лесенка»
'''
n = int(input('Введите значение: '))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep = '', end='')
    print()
'''

# Задача «Список квадратов»
'''
n = int(input())
i = 0

while i ** 2 < n:
    print(i ** 2)
    i += 1
'''

# Задача «Степень двойки»
'''
n = int(input('Введите число: '))
st = 2
p = 1
while st <= n:
    st *= 2
    p += 1
print(p - 1, st // 2)
'''

# Задача «Утренняя пробежка»
'''
x = int(input())
y = int(input())
l = x
d = 0

while l <= y:
    l += 0.1*l
    d += 1

print(d)
'''

# Задача «Длина последовательности»
'''
len = 0
while int(input('Введите число: ')) != 0:
    len += 1
print(len)
'''

# Задача «Количество элементов, которые больше предыдущего»
'''
pr = int(input('Введите число: '))
x = 0
while pr != 0:
    last = int(input('Введите число: '))
    if last != 0 and pr < last:
        x += 1
    pr = last
print(x)
'''

# Задача «Второй максимум»
'''
a = int(input())
b = int()
c = int()

while a != 0:
    if b < a:
        b = a
    if c < b:
        b, c = c, b
    a = int(input())
print(b)
'''

# Задача «Числа Фибоначчи»
'''
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
'''

# Задача «Максимальное число идущих подряд равных элементов»
'''
a = int(input())
x2 = x1 = 0

while a != 0:
    b = int(input())
    if a == b:
        x1 += 1
        if x1 > x2:
            x2 = x1
    else:
        x1 = 0
    a = b
print(x2 + 1)
'''

# Задача «Четные индексы»
'''
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
'''

# Задача «Больше предыдущего»
'''
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
'''

# Задача «Наибольший элемент»
'''
max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[max]:
        max = i
print(a[max], max)
'''

# Задача «Шеренга»
'''
a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)
'''

# Задача «Переставить соседние»
'''
a = [int(i) for i in input().split()]

for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]

print(' '.join([str(i) for i in a]))
'''

# Задача «Переставить min и max»
'''
a = [int(i) for i in input().split()]

min = a.index(min(a))
max = a.index(max(a))

[a[max], a[min]] = [a[min], a[max]]

print(' '.join([str(i) for i in a]))
'''

# Задача «Удалить элемент»
'''
a = [int(s) for s in input().split()]

k = int(input())

for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()

print(' '.join([str(i) for i in a]))
'''

# Задача «Вставить элемент»
'''
a = [int(s) for s in input().split()]

k, c = [int(s) for s in input().split()]

a.append(0)

for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]

a[k] = c
print(' '.join([str(i) for i in a]))
'''

# Задача «Ферзи»

# не получилось
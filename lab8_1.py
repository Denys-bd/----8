from array import *
import random

N = int(input("Введіть N: "))
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

masiv1 = array('i', [])

for i in range(N):
    masiv1.append(random.randint(a, b))

masiv2 = array('i', [])

for i in range(N):
    masiv2.append(3 ** i)

print("Перший масив:")
print(masiv1)

print("Другий масив:")
print(masiv2)

masiv1.extend(masiv2)

masiv1 = array('i', sorted(masiv1))

print("Об'єднаний масив після сортування:")
print(masiv1)
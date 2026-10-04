import numpy as np
import math

N = int(input("Введіть N: "))

k = math.ceil(math.sqrt(N))

N = k ** 2

print("Розмір матриці:", k, "x", k)
print("Нове значення N:", N)

masiv = np.arange(1, N + 1).reshape(k, k)

print("Матриця:")
print(masiv)
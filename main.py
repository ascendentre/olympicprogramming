import math
import matplotlib.pyplot as plt

E = 10 ** (-6)


def Q(x, n):
    return -((x ** 2) * (2 * n + 1)) / (((2 * n + 3) ** 2) * (2 * n + 2))


def S(x):
    a = x
    summa = a
    n = 0
    while abs(a) > E:
        a = a * Q(x, n)
        summa += a
    return summa



def Lagrange(x, x_arr, y_arr, n):
    res = 0
    for i in range(n + 1):
        t = 1
        for j in range(n + 1):
            if j != i:
                t *= (x - x_arr[j]) / (x_arr[i] - x_arr[j])
        res += t * y_arr[i]
    return res

maxp = []
for n in range(6, 50):
    x = [0 for i in range(n + 1)]
    y = [0 for i in range(n + 1)]
    a = 0
    b = 4
    h = (b - a) / n
    for i in range(n + 1):
        #x[i] = i * h
        x[i] = ((b - a) / 2) * math.cos((2 * i + 1.0) / (2.0 * n + 2) * math.pi) + ((b + a) / 2.0)
        y[i] = S(x[i])
    x_1 = [0 for i in range(21)]
    y_1 = [0 for i in range(21)]
    pogr = [0 for i in range(21)]
    h1 = (b - a) / 20
    max = -1
    for i in range(21):
        x_1[i] = i * h1
        y_1[i] = S(x_1[i])
        lang = Lagrange(x_1[i], x, y, n)
        e = abs(lang - y_1[i])
        pogr[i] = e
        if e > max:
            max = e
    print(n, max)
    maxp.append(max)

plt.plot(range(6,50), maxp)
plt.scatter(range(6, 50), maxp)
plt.show()
plt.grid(True)
import matplotlib.pyplot as plt
import math


def func():
    x = [i / 10 for i in range(-50, 50, 1)]
    y1 = [math.cos(i) for i in x]
    y2 = [math.sin(i) for i in x]
    y3 = [i ** 2 for i in x]
    y4 = [2 / i if i != 0 else None for i in x]
    plt.figure("4 поля", figsize=(10, 10))
    plt.subplot(2, 2, 1)
    plt.title("y1 = cos(x)")
    plt.ylabel("y1")
    plt.plot(x, y1)
    plt.grid(True)
    plt.subplot(2, 2, 2)
    plt.title("y1 = sin(x)")
    plt.ylabel("y2")
    plt.plot(x, y2)
    plt.grid(True)
    plt.subplot(2, 2, 3)
    plt.title("y1 = x^2")
    plt.ylabel("y3")
    plt.xlabel("x")
    plt.plot(x, y3)
    plt.grid(True)
    plt.subplot(2, 2, 4)
    plt.title("y1 = 2 / x")
    plt.ylabel("y4")
    plt.xlabel("x")
    plt.plot(x, y4)
    plt.grid(True)
    plt.show()


func()

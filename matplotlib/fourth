import random
import matplotlib.pyplot as plt


def pie(n):
    plt.title("Круговая диаграмма")
    names = [str(i) for i in range(1, n + 1)]
    values = random.choices(range(100), k=n)
    plt.pie(values, labels=names, autopct='%.1f%%')
    plt.show()


pie(10)

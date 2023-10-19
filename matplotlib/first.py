import matplotlib.pyplot as plt


def intersection(y1, y2):
    plt.title("Графики y1(x) и y2(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    x = 0
    y1_res_1 = eval(y1)
    y2_res_1 = eval(y2)
    for x in range(-10, 10):
        if eval(y1) == eval(y2):
            break
    y1_res_2 = eval(y1)
    y2_res_2 = eval(y2)
    plt.plot([0, x], [y1_res_1, y1_res_2], [0, x], [y2_res_1, y2_res_2])
    plt.legend([f"y1 = {y1}", f"y1 = {y2}"], loc=2)
    plt.show()


exec("y1 = '2 * x - 3'")
exec("y2 = '0.5 * x + 0.5'")
intersection(y1, y2)

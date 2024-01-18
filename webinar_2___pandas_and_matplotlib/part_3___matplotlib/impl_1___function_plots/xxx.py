import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()  # NOSONAR


def main():
    x = np.linspace(-3, 3, 30 + 1)
    print(x)
    print()

    fig, ax = plt.subplots()
    # print(type(fig))
    # print(fig)
    # print(type(ax))
    # print(ax)

    y1 = x + 2
    print(y1)
    # ax.plot(x, y1)
    # ax.plot(x, y1, color='red', linestyle='-',  marker='o', label='y = x+2')
    ax.plot(x, y1, color='red', linestyle='-',  marker='o', label='$y = x+2$')  # LaTeX

    y2 = x ** 2
    ax.plot(x, y2, color='orange', linestyle='--',  label='$y = x^2$')

    y3 = np.sin(x)
    ax.plot(x, y3, color='green', linestyle=':',  label='$y = \\sin x$')

    y4 = 2 ** x
    ax.plot(x, y4, color='blue', linestyle='-.',  label='$y = 2^x$')

    ax.grid()
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['bottom', 'left']].set_position(('data', 0))
    ax.set_xlim((-3.5, 3.5))
    ax.set_ylim((-1.5, 3.5))
    ax.set_title('Four Function Plots in One Figure')
    ax.legend()  # fügt (u.a.) die Labels hinzu; wird automatisch dort eingefügt, wo es am besten passt/ Platz ist

    fig.tight_layout()



    fig.show()


if __name__ == '__main__':
    main()

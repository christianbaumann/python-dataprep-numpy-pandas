import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid', palette='colorblind')


def main():
    fig = plt.figure(figsize=(12, 9), dpi=100, layout='constrained')
    gs = fig.add_gridspec(2, 2)
    ax_top = fig.add_subplot(gs[0, :])
    ax_bottom_left = fig.add_subplot(gs[1, 0])
    ax_bottom_right = fig.add_subplot(gs[1, 1])

    # TODO 1

    print('-' * 100)

    # TODO 2

    print('-' * 100)

    # TODO 3

    print('-' * 100)

    # TODO 4

    print('-' * 100)

    # TODO 5

    plt.show()


if __name__ == '__main__':
    main()

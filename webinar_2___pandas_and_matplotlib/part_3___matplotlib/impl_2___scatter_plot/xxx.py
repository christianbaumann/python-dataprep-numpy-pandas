import numpy as np
import matplotlib.pyplot as plt

POINT_COUNT = 100
rng = np.random.default_rng()  # NOSONAR


def main():
    x = rng.normal(size=POINT_COUNT)
    y = rng.normal(size=POINT_COUNT)
    # sizes = 1000 * rng.normal(size=POINT_COUNT)
    sizes = 750 * abs(rng.normal(size=POINT_COUNT))
    colors = rng.normal(size=POINT_COUNT)

    fig, ax = plt.subplots()
    # ax.scatter(x, y, s=sizes, c=colors, alpha=0.5)
    ax.scatter(x, y, s=sizes, c=colors, cmap='plasma', alpha=0.5)
    ax.set_title('Scatter Plot')

    fig.colorbar(mappable=ax.collections[0])
    fig.tight_layout()
    fig.show()


if __name__ == '__main__':
    main()

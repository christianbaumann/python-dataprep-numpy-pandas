import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()  # NOSONAR


def main():
    # TODO
    pass


def f(x, y):
    return np.sin(x) ** 10 + np.cos(x * y + 10) * np.cos(x)


if __name__ == '__main__':
    main()

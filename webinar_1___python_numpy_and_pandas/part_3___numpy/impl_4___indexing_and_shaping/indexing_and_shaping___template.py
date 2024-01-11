import numpy as np

rng = np.random.default_rng()  # NOSONAR


def main():
    vector = rng.integers(100, 999 + 1, 10)
    # TODO

    print('-' * 100)

    matrix = rng.integers(100, 999 + 1, (10, 3))
    # TODO


if __name__ == '__main__':
    main()

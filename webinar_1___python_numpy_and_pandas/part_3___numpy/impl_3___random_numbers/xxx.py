import numpy as np

rng = np.random.default_rng();
# rng = np.random.default_rng(seed=1130);


def main():
    # discrete uniform integers
    # print(rng.integers(10))
    # print()
    # print(rng.integers(5, 10))
    # print()
    # print(rng.integers(5, 10, 4))
    # print(type(rng.integers(5, 10, 4)))
    # print()
    # print(rng.integers(5, 10, (4, 5)))
    #
    # print('-' * 100)

    # normal/Gaussian distribution
    # print(rng.normal(7.3, 1.4, 30))

    print('-' * 100)

    # continuous uniform floats in [0.0, 1.0)
    print(rng.random(30))


if __name__ == '__main__':
    main()

import numpy as np

rng = np.random.default_rng(seed=42)  # NOSONAR


def main():
    vector = rng.integers(100, 999 + 1, 10)
    # print(vector)
    # print(vector[4])
    # print(vector[1:5])
    # vector[1:5] = 621
    # print(vector)
    # print()
    # vector_slice = vector[5:9]
    # print(vector_slice)
    # vector_slice[:] = 770
    # print(vector_slice)
    # print(vector)

    print('-' * 100)

    matrix = rng.integers(100, 999 + 1, (10, 3))
    print(matrix)
    print()
    print(matrix[1][2])
    print()
    print(matrix[1, 2])
    print()
    print(matrix[:5])
    print()
    print(matrix[:5, 2:])
    print()
    matrix = matrix.reshape(6,5)
    print(matrix)


if __name__ == '__main__':
    main()

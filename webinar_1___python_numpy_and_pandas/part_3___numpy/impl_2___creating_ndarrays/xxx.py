import numpy as np


def main():
    matrix = np.array([[-1.4, 2.2, 4.2], [4.3, 2.4, 1]])  # klassische Python Liste
    # print(matrix)
    # print(type(matrix))
    # print(matrix.ndim)
    # print(matrix.shape)
    # print(matrix.dtype)
    # print()
    # print(matrix * -9)
    # print()
    # print(matrix + matrix)

    print('-' * 100)

    # print(np.zeros((1, 4)))
    # print(np.zeros((1, 4), dtype='int32'))
    # print()
    # print(np.ones((3, 3)))
    # print()
    # print(np.identity(5))  # Einheitsmatrix (neutrales Element bei Multiplikation)

    print('-' * 100)

    # print(np.arange(2, 6))  # Analog zu Python's 'range'
    # print()
    # print(np.linspace(2, 6, 10+1))


if __name__ == '__main__':
    main()

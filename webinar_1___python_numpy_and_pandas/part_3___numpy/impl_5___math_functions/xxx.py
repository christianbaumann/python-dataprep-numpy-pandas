import numpy as np

rng = np.random.default_rng()  # NOSONAR


def main():
    matrix = rng.normal(loc=0.0, scale=1.0, size=(5, 5))
    print(matrix)

    print(f'Mean: {np.mean(matrix)}')
    print(f'Mean: {matrix.mean()}')
    print(f'Standard Deviation: {matrix.std()}')
    print(f'Sum: {matrix.sum()}')
    print(f'Column Sums (= sums down the rows): {matrix.sum(axis=0)}')
    print(f'Row Sums (= sums across the columns): {matrix.sum(axis=1)}')
    print(f'Cumulative Column Sums:\n{matrix.cumsum(axis=0)}')


if __name__ == '__main__':
    main()

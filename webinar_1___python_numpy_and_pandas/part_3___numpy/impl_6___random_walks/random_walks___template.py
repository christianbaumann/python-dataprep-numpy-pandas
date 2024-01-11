import random
import numpy as np
import matplotlib.pyplot as plt

STEP_COUNT = 100


def main():
    walk = python_walk()
    # walk = numpy_walk()
    print(walk)
    _, ax = plt.subplots()
    ax.plot(walk)
    plt.show()


def python_walk():
    position = 0
    walk = [position]
    for _ in range(STEP_COUNT):
        step = 1 if random.randint(0, 1) else -1
        position += step
        walk.append(position)
    return walk


def numpy_walk():
    # TODO

    print(f'Walk: ')
    print(f'Minimum: ')
    print(f'Maximum: ')
    print(f'Step Number at Maximum: ')
    print(f'First Time Being 10 Steps Away from the Center: ')

    # TODO


if __name__ == '__main__':
    main()

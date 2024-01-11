import math

I_SQUARED_MAX = 1_000_000


def main():
    pass  # TODO

for i in range(1, I_SQUARED_MAX):

    square = i ** 2

    if square > I_SQUARED_MAX:
        break

    print(square)

    number_of_sixes = str(square).count('6')
    if number_of_sixes >= 3:
        break



if __name__ == '__main__':
    main()

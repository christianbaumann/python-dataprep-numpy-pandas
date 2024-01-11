def main():
    f = 10 / 5
    print(f, type(f))  # float

    a = 10 // 5
    print(a, type(a))  # integer

    n = 6 / 8
    h = 6 // 8
    print(n, h)

    print('-' * 100)

    c = 7 ** 5000  # Integer in Python können beliebig groß sein
    print(c)
    print(type(c))
    print(len(str(c)))


if __name__ == '__main__':
    main()

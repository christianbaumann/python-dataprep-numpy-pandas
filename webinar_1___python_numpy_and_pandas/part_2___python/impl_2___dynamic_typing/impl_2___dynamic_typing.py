def main():
    g = 'Hello!'
    print('ID of g:', id(g))
    print('Type of g:', type(g))
    print('Value of g:', g)

    print('-' * 100)

    g = 9904
    print('ID of g:', id(g))
    print('Type of g:', type(g))
    print('Value of g:', g)

    # Typ der Variablen hängt in Python immer an der Instanz, und nicht an der Referenz


if __name__ == '__main__':
    main()
def gaseste_cea_mai_lunga_subsecventa_domino(lista):
    cea_mai_lunga_subsecventa = []
    subsecventa_curenta = [lista[0]]

    for i in range(1, len(lista)):
        x1, y1 = lista[i - 1]
        x2, y2 = lista[i]

        if y1 == x2:
            subsecventa_curenta.append(lista[i])
        else:
            if len(subsecventa_curenta) > len(cea_mai_lunga_subsecventa):
                cea_mai_lunga_subsecventa = subsecventa_curenta
            subsecventa_curenta = [lista[i]]

    if len(subsecventa_curenta) > len(cea_mai_lunga_subsecventa):
        cea_mai_lunga_subsecventa = subsecventa_curenta

    return cea_mai_lunga_subsecventa


lista_numerelor = [(8, 9), (9, 5), (5, 4), (4, 7), (7, 2), (2, 8), (3, 3), (1, 1)]

subsecventa_domino = gaseste_cea_mai_lunga_subsecventa_domino(lista_numerelor)

print(f'Cea mai lungă subsecvență domino este: {subsecventa_domino}')
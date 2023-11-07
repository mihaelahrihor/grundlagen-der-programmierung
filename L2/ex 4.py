def cripteaza_lista(lista, metoda):
    if not lista:
        return []

    cheie = lista[0]
    criptata = [cheie]

    for numar in lista[1:]:
        if metoda == '+':
            cheie += numar
        elif metoda == '*':
            cheie *= numar
        elif metoda == 'XOR':
            cheie = cheie ^ numar
        criptata.append(cheie)

    return criptata

lista_numerelor = [5, 3, 7, 2, 8]

metoda_criptare = '*'  # Schimbați în '+', '*', sau 'XOR' pentru metoda dorită

lista_criptata = cripteaza_lista(lista_numerelor, metoda_criptare)

print(f'Lista criptată: {lista_criptata}')


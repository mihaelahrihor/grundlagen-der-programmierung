def generare_cel_mai_mare_numar(lista):
    # Conversia elementelor listei la șiruri de caractere
    lista_str = list(map(str, lista))

    # Sortarea șirurilor în ordine descrescătoare, cu funcția de comparație personalizată
    lista_str.sort(key=lambda x: x * 3, reverse=True)

    # Concatenarea șirurilor pentru a obține cel mai mare număr
    cel_mai_mare_numar = ''.join(lista_str)

    return cel_mai_mare_numar


lista_numerelor = [9, 5, 31, 48]
cel_mai_mare = generare_cel_mai_mare_numar(lista_numerelor)

print(f'Cel mai mare număr posibil este: {cel_mai_mare}')


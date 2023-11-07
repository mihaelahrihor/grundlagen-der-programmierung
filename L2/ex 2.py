def numara_perechi_simetrice(lista):
    numar_perechi_simetrice = 0

    for x, y in lista:
        if (x, y) in lista or (y, x) in lista:
            numar_perechi_simetrice += 1

    return numar_perechi_simetrice

lista_numerelor = [ (1, 2), (3, 4), (2, 1), (5, 5)]

rezultat = numara_perechi_simetrice( lista_numerelor)

print('numarul de perechi simetrice este : ', rezultat)
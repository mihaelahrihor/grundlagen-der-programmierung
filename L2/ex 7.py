import math

def gaseste_cmc_dintre_indici(lista, de_la, catre):
    if de_la < 0 or catre < 0 or de_la >= len(lista) or catre >= len(lista) or de_la > catre:
        return "Indicii specificați nu sunt valizi."

    sublist = lista[de_la:catre + 1]

    def cmmdc(x, y):
        return x if y == 0 else cmmdc(y, x % y)

    def cmmmc(x, y):
        return x * y // cmmdc(x, y)

    cmc = sublist[0]
    for numar in sublist[1:]:
        cmc = cmmmc(cmc, numar)

    return cmc


lista_numerelor = [2, 3, 4, 5, 6, 7, 8, 9]

de_la = 2  # Indicele de la

catre = 5  # Indicele către

cmc = gaseste_cmc_dintre_indici(lista_numerelor, de_la, catre)
print(f'Cel mai mic multiplu comun între indicii {de_la} și {catre} este: {cmc}')
def citeste_din_fisier(fisier):
    f = open(fisier, "r")
    linie = f.readline().strip("\n")
    cuvinte = linie.split(" ")
    f.close()
    return cuvinte

def scrie_in_fisier(filename, text):
    f = open(filename, "w")
    f.write("\n")
    string = list_to_string(text)
    f.write(string)
    f.close()

def list_to_string(lista):
    string = ""
    for cuvant in lista:
        string += cuvant + " "
    return string

def solve(nume_fisier):
    cuvintele_mele = citeste_din_fisier(nume_fisier)
    print(cuvintele_mele)
    cuvant_de_inlocuit = input("Introduceti cuvantul de inlocuit: ")
    cuvant_nou = input("Introduceti cuvantul cu care il inlocuiti: ")
    numar_inlocuiri = int(input("Introduceti numarul de inlocuiri: "))
    am_inlocuit_de_n_ori = 0
    for i in range(len(cuvintele_mele)):
        cuvant_curent = cuvintele_mele[i]
        if cuvant_curent == cuvant_de_inlocuit and am_inlocuit_de_n_ori < numar_inlocuiri:
            cuvintele_mele[i] = cuvant_nou
            am_inlocuit_de_n_ori += 1
    return cuvintele_mele

inlocuit = solve("input.txt")
print(inlocuit)
scrie_in_fisier("input.txt", inlocuit)
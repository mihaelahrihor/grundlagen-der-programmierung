def inlocuieste_cuvant(fisier, cuvant_de_inlocuit, cuvant_de_inlocuire):
    file = open(fisier, 'r')    #deschidem un fisier de citire
    text = file.read()      #citim continutul fisierului si il retinem in variabila text
    file.close()    #inchidem fisierul
    #inlocuim aparitiile cuvantului de inlocuit cu noul cuvand in textul citit din fisier
    text_modificat = text.replace(cuvant_de_inlocuit, cuvant_de_inlocuire)

    file = open(fisier, 'w')    #deschidem un fisier de scriere si se va sterge continutul anterior din fisier
    file.write(text_modificat)      #adaugam textul modificat in fisier
    file.close()    #inchidem fisierul
    #calculam de cate ori a fost gasit si inlocuit cuvantul original in textul original
    count = text.count(cuvant_de_inlocuit)
    if count > 0:       #in functie de rezultat afisam mesajul corespunzator
        print(f'Înlocuiește "{cuvant_de_inlocuit}" cu "{cuvant_de_inlocuire}" de {count} ori.')
    else:
        print(f'Cuvântul "{cuvant_de_inlocuit}" nu a fost găsit în fișier.')

fisier = input("Calea către fișier: ")
cuvant_de_inlocuit = input("Cuvânt de înlocuit: ")
cuvant_de_inlocuire = input("Cuvânt de înlocuire: ")

inlocuieste_cuvant(fisier, cuvant_de_inlocuit, cuvant_de_inlocuire)

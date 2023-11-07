def elimina_duplicate(lista):
    lista_unica = []
    [lista_unica.append(item) for item in lista if item not in lista_unica] #
    return lista_unica



lista = ['12', '34', '56', '12', '78', '34']
lista_filtrata = elimina_duplicate(lista)

print("Lista initială:", lista)
print("Listă fără duplicate:", lista_filtrata)
#probl 1.a
# ''
# def isprime(n):
#     nrdiv=0 #se initializeaza cu 0 un contor pentru divizorii lui n
#     for i in range(1,n+1): #se parcurg numerele de la 1 la n si se verifica daca sunt divizori a lui n
#         if n%i == 0:
#          nrdiv += 1
#     if (nrdiv == 2):# daca numarul divizorilor este 2 (divizorii proprii) atunci n este prim
#         return True
#     return False
#
#
# def listprime(n):
#     prime=[] #initializam lista in care vom pune nr prime
#     for i in range(2,n+1):
#         if isprime(i):  #se verifica daca nr e prim apeland functia pentru prim si se adauga in lista pentru prime
#             prime.append(i)
#
#     return prime
# n = int(input("n="))
#
# print(listprime(n))
#
#
#
# #probl 1.b
# def Teilfolge(list,n):
#     num=0   #se incepe prin initializarea variabilelor num si count cu 0
#     count=0
#
#     list.sort() #lista de intrare este sortata
#     v=[] #se initializeaza o lista goala v si se adauga primul element din lista sortata in ea
#     v.append(list[0])
#
#     for i in range(1,n): #se parcurge lista sortata si se adauga elemente distincte in lista v
#         if(list[i]!=list[i-1]):
#             v.append(list[i])
#
#     for i in range(len(v)): #dupa ce lista v este creata se parcurge pentru a gasi cea mai lunga subsecventa de numere consecutive
#         if(i>0 and v[i]==v[i-1]+1):
#             count+=1 #variabila count este actualizata ori de cate ori sunt intalnite numere consecutive
#
#         else:
#             count = 1
#         num=max(num, count) #se tine evidenta valorii maxime a lui cont in variabila num
#
#     return num #in final se returneaz num, care reprezinta lungimea celei mai lungi subsecvente de numere consecutive
#
#
# list = [4,1,2,2,3,4,5,0]
# n=len(list)
#
# print('Longest subsequence: ', Teilfolge(list,n))
#


#probl 12.a

def is_prime(n):
    nrd = 0
    for i in range(1, n + 1):
        if n % i == 0:
            nrd += 1
    if nrd == 2:
        return True
    return False

def cmmdc(a, b): #functia calculeaza cel mai mare divizor comun dintre 2 numere folosind a si b
    while a != b:
        if a > b:
            a = a - b #se scad repetat nr mai mici din nr mai mari pana se ajunge la CMMD
        else:
            b = b - a
    return a

def prime_intre_ele(n): #functia gaseste toate numerele prime mai mici decat n si ca sa fie prime intre ele cu n, cmmd trebuie sa fie 1
    new_list = []
    for i in range(1, n):
        if is_prime(i) and cmmdc(i, n) == 1:
            new_list.append(i)
    print(new_list)

n = int(input("n="))
prime_intre_ele(n)

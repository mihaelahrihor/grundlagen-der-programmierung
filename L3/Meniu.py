from Rechteck import rechteck
from Hertz import hertz
from Hauser import hauser
def printmenu():
    o = 'Meniu\n'
    o = o + '1. Rechteck\n'
    o = o + '2. Hertz\n'
    o = o + '3. Häuser\n'
    o = o + '4. Exit\n'

    print(o)

def lesenmoglichkeit():

    moglichkeit = int(input('Moglichkeit'))
    print(moglichkeit)
    return moglichkeit

def main():

    stop = False
    while(stop == False):
        printmenu()
        m = lesenmoglichkeit()

        if(m == 1):
            rechteck()
        elif (m == 2):
             hertz()
        elif (m == 3):
            hauser()
        elif (m == 4):
            stop = True
        else:
            print('Moglichkeit existiert nicht')

main()





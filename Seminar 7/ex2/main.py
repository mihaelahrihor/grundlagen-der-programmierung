


def main():

    ''''
    d = Die(6)
    roll = d.roll()
    while roll != 6:
        print(f'rolled: {roll}')
        roll = d.roll()

    print(f'rolled: {roll}')
    '''
    f1 = Frac(4, 12)
    #f1.extend(10)
    f1.reduce()
    print(f'{f1.n}/{f1.m}')


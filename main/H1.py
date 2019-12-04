'''
Hovedoppgave 1, Vetle Løvmo Endresen

Eventuelle teorispørsmål kan besvares med multiline-kommentarer som denne.
'''

# Oppgave 1
import math

def pi(d=2):
    integer = int(d)
    if 0 < integer <= 20:
        desimals = int(d)
        pi_format = round(math.pi, desimals)
        return pi_format
    elif integer > 20:
        return f'For mange desimaler {d}'
    else:
        pi_format = round(math.pi, d)
        return pi_format


# Oppgave 2
def temperaturKonvertering(grader, format='C'):
    try:
        if format == 'C':
            print('Konverterer til fahrenheit')
            fahrenhet = (grader*(9/5)) + 32
            return (f'{grader:.1f}c = {fahrenhet:.1f}f ')

        elif format == 'F':
            print('Konverterer til celsius')
            celsius = ((grader - 32) * (5 / 9))
            return (f'{grader:.1f}f = {celsius:.1f}c ')

        elif format == '':
            print('Konverterer til fahrenheit')
            fahrenhet = (grader*(9/5)) + 32
            return (f'{grader:.1f}c = {fahrenhet:.1f}f ')

    except ValueError:
        print('Legg inn en tallverdi!')

grader = float(input('Grader: '))
format = input('Format C/F: ')
print(temperaturKonvertering(grader, format))

'''
Alternativt, så kan du kalle på temperaturKonvertering() funksjonen i konsollen. 
Her har du også mulighet til å legge inn temperaturene og få riktig formatering. 
Tilsvarende hvis du ikke legger inn et format.
'''


# Oppgave 3 a
saldo = 500
rentesats = 0.01
renter = 0


def innskudd(innskudd):
    global saldo
    global rentesats
    saldo += innskudd
    if saldo >= 1000000:
        print('Gratulerer, du får bonusrente')
        rentesats = 0.02
    else:
        rentesats = 0.01


def uttak(uttak):
    global saldo
    global rentesats
    saldo -= uttak
    if 0 <= saldo < 1000000:
        print('Du har ordinær rente')
        rentesats = 0.01
    elif saldo >= 1000000:
        rentesats = 0.02
    else:
        print('overtrekk')
        saldo += uttak


def beregnRente():
    global saldo
    global rentesats
    global renter
    if saldo < 1000000:
        renter = saldo * rentesats
        print(f'Renter = {renter:.2f}')
    else:
        renter = saldo * rentesats
        print(f'Renter = {renter:.2f}')


def renteoppgjør():
    global saldo
    global renter
    saldo = saldo + renter
    print(f'{saldo:.2f}')


# oppgave 3b

saldo = 500
renter = 0
rentesats = 0.01


def rentesatsberegning():
    global saldo
    global rentesats

    if 0 <= saldo < 1000000:
        rentesats = 0.01
    elif saldo >= 1000000:
        rentesats = 0.02


def innskudd():
    while True:
        global saldo
        global rentesats
        inp = float(input('Beløp: '))

        try:
            saldo += inp
            rentesatsberegning()
            break
        except:
            print('Feil verdi')


def uttak():
    while True:
        global saldo
        inp = float(input('Beløp: '))

        if inp <= saldo:
            saldo -= inp
            rentesatsberegning()
            break
        else:
            print('ikke dekning')


def renteoppgjør():
    global saldo
    global renter
    rentesatsberegning()
    renter = saldo * rentesats
    saldo = saldo + renter
    print(f'{saldo:.2f}')


def kontroller():
    print('--------------------')
    print('1 - Vis saldo')
    print('2 - Innskudd')
    print('3 - uttak')
    print('4 - Renteoppgjør')
    print('5 - Avslutt')
    print('--------------------')

    while True:
        try:
            inp = float(input('Velg handling: '))
            if inp.is_integer() == True and inp == 1:
                global saldo
                print(f'{saldo:.2f}')
            elif inp.is_integer() == True and inp == 2:
                innskudd()
                print(f'Saldo: {saldo:.2f}')
            elif inp.is_integer() == True and inp == 3:
                uttak()
                print(f'Saldo: {saldo:.2f}')
            elif inp.is_integer() == True and inp == 4:
                renteoppgjør()
                print(f'Saldo: {saldo:.2f}')
            elif inp.is_integer() == True and inp == 5:
                print('Avslutter...')
                time.sleep(1)
                break
            else:
                print('Prøv igjen')
        except ValueError:
            print('Prøv igjen')


kontroller()

# Oppgave 3c

import time

saldo = 500
renter = 0
rentesats = 0.01
endringer = ['', '', '']


def sisteEndringer(ending):
    global endringer
    endringer.insert(0, ending)
    del endringer[-1]


def rentesatsberegning():
    global saldo
    global rentesats

    if 0 <= saldo < 1000000:
        rentesats = 0.01
    elif saldo >= 1000000:
        rentesats = 0.02


def innskudd():
    while True:
        global saldo
        global rentesats
        inp = float(input('Beløp: '))

        try:
            saldo += inp
            rentesatsberegning()
            sisteEndringer(f'+ {inp:.2f}')
            break
        except:
            print('Feil verdi')


def uttak():
    while True:
        global saldo
        inp = float(input('Beløp: '))

        if inp <= saldo:
            saldo -= inp
            rentesatsberegning()
            sisteEndringer(f'- {inp:.2f}')
            break
        else:
            print('ikke dekning')


def renteoppgjør():
    global saldo
    global renter
    rentesatsberegning()
    renter = saldo * rentesats
    saldo = saldo + renter
    sisteEndringer(f'+ {saldo:.2f}')
    print(f'Rentesats: {rentesats:.2f}')
    print(f'Renter: {renter:.2f}')


def kontroller():
    print('--------------------')
    print('1 - Vis saldo')
    print('2 - Innskudd')
    print('3 - uttak')
    print('4 - Renteoppgjør')
    print('5 - Siste endringer')
    print('6 - Avslutt')
    print('--------------------')

    while True:
        try:
            inp = float(input('Velg handling: '))
            if inp.is_integer() == True and inp == 1:
                global saldo
                print(f'{saldo:.2f}')
            elif inp.is_integer() == True and inp == 2:
                innskudd()
                print(f'Saldo: {saldo:.2f}')
            elif inp.is_integer() == True and inp == 3:
                uttak()
                print(f'Saldo: {saldo:.2f}')
            elif inp.is_integer() == True and inp == 4:
                renteoppgjør()
                print(f'Saldo: {saldo:.2f}')
            elif inp.is_integer() == True and inp == 5:
                for e in endringer:
                    print(e)
            elif inp.is_integer() == True and inp == 6:
                print('Avslutter...')
                time.sleep(1)
                break
            else:
                print('Prøv igjen')
        except ValueError:
            print('Prøv igjen')


kontroller()


# Oppgave 4
import random


def randomiser():
    tall = [str(random.randint(1, 9)), str(random.randint(1, 9)), str(random.randint(1, 9))]
    tall.sort()

    for i in tall:
        print(''.join(i), end='')


randomiser()

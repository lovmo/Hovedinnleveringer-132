'''
Temaoppgave 2, Vetle Endresen
'''

# Oppgave 1

import math

def arealkalkulator(x):
    cal = math.pi * (x**2)
    return cal

def error(x):
    try:
        inp = float(x)
        return inp
    except ValueError:
        quit()

radius_ = input('Radius: ')
z = error(radius_)
radius = round(arealkalkulator(z), 3)


print(f'Radius: {z}')
print(f'Arealet til en sirkel med radius {z} er {radius}')

# Oppgave 2

def lengde(x):
    ant = float(len(x))
    return ant

inp = input('Sentence: ')
lengde_ = lengde(inp)

gjett = float(input('Guess: '))

print('Guess:', gjett)

if lengde_ == gjett:
    print('That\'s True!')
else:
    print('That\'s False!!')

print(f'answer is {lengde_ == gjett}')

# Oppgave 3

import random

def tilfeldig(x):
    y = str(x) + str(random.randint(0,100))
    return y

def konverter(x):
        inp = int(x)
        return inp

inp = int(input('Gi meg et tall:'))
ut_ = tilfeldig(inp)
ut = konverter(ut_)

print(ut, '/', inp, '=', f'{ut/inp: .3f}')


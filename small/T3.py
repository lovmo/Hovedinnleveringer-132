'''
Temaoppgave 3, Vetle Endresen
'''


# Oppgave 1

#Det første uttrykket evalueres til FALSE og den andre uttrykket evalueres til TRUE.

#Ekvivalentene:
print(x!=7 and y<=50)
print(not(x!=7 or y<=50))
print((x>7 or 50<y) and (x>y or y<100))
print(not((not(x>7) and 50<y) or (x>y and y<100)))


# Oppgave 2

def ord(alder, lengde):
    x = max([(30 - alder), (9 - lengde)])
    if not (alder >= 30 and lengde >= 9):
        return x
    else:
        return None


def byst(alder, lengde):
    y = max([(25 - alder), (5 - lengde)])
    if not (alder >= 25 and lengde >= 5):
        return y
    else:
        return None


alder = int((input('Oppgi alder:')))
lengde = int((input('Hvor lenge har du bodd sang_liste Tulleby?')))

o = ord(alder, lengde)
b = byst(alder, lengde)

if alder >= 30 and lengde >= 9:
    ord(alder, lengde)
    print('Du kan bli ordfører eller sitte sang_liste bystyret.')

elif alder >= 25 and lengde >= 5:
    byst(alder, lengde)
    print(f'Du kan sitte sang_liste bystyret.')
    print(f'Prøv igjen om {o} år for å blir ordfører.')

else:
    print(f'Du er ikke kvalifisert enda, prøv igjen om {b} år for å sitte sang_liste bystyret eller {o} for å bli ordfører.')

# oppgave 3

x = int(input('tall:'))

if x >= 10:
    print('Min 10')
elif x > 5:
    print('6,7,8 eller 9')
else:
    print('max 5')

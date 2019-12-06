## Eksamen H18

# 15:36 start, 16:14 slutt

# Oppgave 1.

lst = [3, 2, 1, 0]
result = 0
for i in lst:
    result = lst[i]
print(result)


# 3

# Oppgave 2.

def f(n, m):
    return n*m

result = 0
for i in [0, 1, 2]:
    result = f(i, i-1)
print(result)

# 2


# Oppgave 3.
# Feil kjører ikke (Mangler linjeshift)

# Oppgave 4.
trans = {0: 1, 1: 3, 3: 2, 2: 0}
print(trans[trans[trans[0]]], "-", trans[trans[0]])
# 2 - 3

# Oppgave 5.

def f(n):
    return n // 2
print(list(map(f, [2, 4, 8, 16])))

# [1,2,4,8]

# Oppgave 6.
def even(n):
    if n%2 == 0:
        return True
    return False

print(list(map(even, [0, 1, 2, 3])))

# [True, False, True, False]


# Oppgave 7.
text = "abcd"
result = ""
for i in [0, 1, 2]:
    for j in text[i:]:
        result = j
print(result)
# d

# Oppgave 8.
tall = {"null": 0, "en": 1, "to": 2, "tre": 3, "fire": 4}
s_key = lambda x: (len(x), tall[x])
print(list(sorted(tall, key = s_key)))

#
# (4, 0)
# (2, 1)
# (2, 2)
# (3, 3)
# (4, 4)
# ['en', 'to', 'tre', 'null', 'fire']


# Oppgave 9.
def flip(f):
    def result(x, y):
        return f(y, x)
    return result

def sub(x, y):
    return x - y

f = flip(sub)
print(f(2, 1))
# -1

# Oppgave 10.
'''
Tupler er på lik linje som keys in ordbøker immutable (uforandrelige). Siden verdiene
har en egen hash verdi, kan tupler benyttes som nøkler i en ordbok. Det er mulig
å endre på elementene i en liste, og en dictionary tillater derfor ikke å ha en
sub liste som key.
'''

# Oppgave 11.
'''
Python benytter seg av en hashingfunksjon for å sortere nøklene i en orbok, noe som
gjør at søkehastigheten blir betydelig raskere enn ved et lineært søk i en liste.
En ordbok sørger for en bedre sortering og oversikt over dataene. I denne situasjonen
vil det være praktisk å kunne søke på emnekoder for å finne alle studentene som tar det
faget
'''

# Oppgave 12.

class Student:

    def __init__(self):
        self.completed_courses = []

    def complete_course(self, emnekode):
        self.completed_courses.append(emnekode)


# Oppgave 13.

def handleliste(fil):
    with open(fil, 'r', encoding='utf-8-sig') as varer:
        alle_varer = [i.strip().split(';') for i in varer]
        for i in alle_varer:
            i.insert(3, float(i.pop(3)))
        tupler = [tuple(i) for i in alle_varer]
        return tupler

handle = handleliste('hei.csv')
for i in handle:
    print(i)

print()
print()
print()
print()
print()

#Oppgave 14.

def dato_varer(handlevarer):
    varer_dict = {}
    for i in handlevarer:
        if i[0] not in varer_dict.keys():
            varer_dict.update({i[0]: [(i[2],i[3])]})
        else:
            varer_dict[i[0]].append((i[2],i[3]))
    return varer_dict

dato_d = dato_varer(handle)
print(dato_d)

print()
print()
print()
print()
print()

#Oppgave 15.

def dato_priser(salg, dato):
    priser = []
    if dato in salg:
        for i in salg[dato]:
            priser.append(i[1])
    return f'evaluere til {priser}.'

priser = dato_priser(dato_d, "03.11.2018")
print(priser)

print()
print()
print()
print()
print()

# Oppgave 16.

def sum_dato_priser(salg, datoer):
    salgssum = []
    for i in datoer:
        if i in salg:
            for k in salg[i]:
                salgssum.append(k[1])
    print(salgssum)
    
    sum_s = sum(salgssum)
    tekst = '+'.join([str(i) for i in salgssum])
    return f'som gir {sum_s} ({tekst}).'


sum_alle = sum_dato_priser(dato_d, ["03.11.2018", "03.11.2018"])
print(sum_alle)

# 3

# 2

# Feil

# 2-3

# [1,2,4,8]

# 0%2 = 0 T
# 1%2 = 1 F
# 2%2 = 0 T
# 3%2 = 1 F

# d

# (4,0)
# (2,1)
# (2,2)
# (3,3)
# (4,4)
# -----> [1, 2, 3, 0, 4]



# -1

# Årsaken er fordi det ikke er mulig å endre verdien i tuplene. Hvis vi skal ha
# nøkler sammensatt av flere verdier, er det tupler som er løsningen. En liste med sub
# lister som inneholder sammensatte nøkkelverdier kan ikke konverteres til en ordbok.

# En ordbok i python benytter en hashing funksjon for å sortere/finne verdier, noe som
# dette til en veldig effektig og rask metode for å hente ut data.


class Student:

    def __init__(self):
        self.completed_courses = []

    def complete_course(self, emnekode):
        self.completed_courses.append(emnekode)


def varer(fil):
    with open(fil, 'r', encoding='utf-8-sig') as salg:
        alle_salg = [i.strip().split(';') for i in salg]
        for i in alle_salg:
            i.insert(3, float(i.pop(3)))
        alle_salg_tupler = [tuple(i) for i in alle_salg]
        return alle_salg_tupler

k = varer('hei.csv')
for i in k:
    print(i)

print()
print()
print()
print()

def ordbok(varer):
    salg = {}
    for i in varer:
        if i[0] not in salg.keys():
            salg.update({i[0]: [(i[2],i[3])]})
        else:
            salg[i[0]].append((i[2],i[3]))
    return salg


m = ordbok(k)
print(m)
print()
print()
print()
print()


def prices_for_date(salg, dato):
    priser = [i[1][1] for i in salg.values() if dato in salg]
    return f'evalueres til {priser}'

l = prices_for_date(m, "03.11.2018")
print(l)
print()
print()
print()
print()


def sum_for_dates(salg, datoer):
    priser = []
    for dato in datoer:
        if dato in salg:
            for i in salg[dato]:
                priser.append(i[1])
    tekst = '+'.join([str(i) for i in priser])
    return f'som gir {sum(priser)} ({tekst}).'

                     
d = sum_for_dates(m, ["03.11.2018", "03.11.2018"])
print(d)



print('Oppg1')
print()
lst = [3, 2, 1, 0]
result = 0
for i in lst:
    result = lst[i]
print(result)

print('Oppg2')
print()

def f(n, m):
    return n*m

result = 0
for i in [0, 1, 2]:
    result = f(i, i-1)
    
print(result)

print('Oppg3')
print()




print('Oppg4')
print()

trans = {0: 1, 1: 3, 3: 2, 2: 0}
print(trans[trans[trans[0]]], "-", trans[trans[0]])

print('Oppg5')
print()

def f(n):
    return n // 2
print(list(map(f, [2, 4, 8, 16])))

print('Oppg6')
print()

def even(n):
    if n%2 == 0:
        return True
    return False
print(list(map(even, [0, 1, 2, 3])))

print('Oppg7')
print()

text = "abcd"
result = ""
for i in [0, 1, 2]:
    for j in text[i:]:
        result = j
print(result)

print('Oppg8')
print()

tall = {"null": 0, "en": 1, "to": 2, "tre": 3, "fire": 4}
s_key = lambda x: (len(x), tall[x])
print(list(sorted(tall, key = s_key)))

print('Oppg9')
print()

def flip(f):
    def result(x, y):
        return f(y, x)
    return result

def sub(x, y):
    return x - y

f = flip(sub)
print(f(2, 1))






























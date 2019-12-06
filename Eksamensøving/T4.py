import math

def pi(d=2):
    x = math.pi
    if d < 15:
        return float(f'{x:.{d}f}')
    else:
        print('For mange desimaler')
        return x

def g_kalk(grader, enhet='C'):
    grader = float(grader)
    if enhet.upper() == 'C':
        farenheit = (grader * (9/5)) + 32
        return float(f'{farenheit:.2f}')
    elif enhet.upper() == 'F':
        celsi = (grader - 32) * (5/9)
        return float(f'{celsi:.2f}')


# a)1 b)1 c)2 d)4
# str - gjør en variabel om til en tekststreng
# type - tar inn en variabel og returnerer hvilken variabel type det er.
# len - Returnerer lengden på en variabel.
# round - Runder av en float variabel.
# input - Er en funksjon som tar inn input fra tastaturet.


# scop forteller hvor i programmet en variabel er definert. Feks en variabel med et globalt scope eller lokalt scope.
# Rekursive funksjoner er funksjoner som kaller på seg selv.

# 10)3 11)4 13) a.3 b.1 c.2 d.1 

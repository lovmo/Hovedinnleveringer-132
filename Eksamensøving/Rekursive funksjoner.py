# REKURSIVE FUNKSJONER

n = 0

def rek(n):
    if n == 10:
        return n
    else:
        print(n)
        return rek(n+1)


def snu(tekst):
    if tekst=='': return ''
    else:
        snuddRest=snu(tekst[1:])
        return snuddRest+tekst[0]

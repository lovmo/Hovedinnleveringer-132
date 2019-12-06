favorittForfattere={'Per':'Christie','Kari':'Ibsen', \
 'Liv':'Rowling','Ola':'Ibsen', \
'Anne':'Allende', 'Jens':'Christie'}


def f_l(forfattere):
    forf = [forfattere[i] for i in forfattere]
    return sorted(set(forf))

x = f_l(favorittForfattere)
print(x)

print()
print()
print()
print()


def fans(forfattere):
    fav = {}
    for i in forfattere.items():
        if i[1] not in fav.keys():
            fav.update({i[1]: [i[0]]})
        else:
            fav[i[1]].append(i[0])
    return fav


k = fans(favorittForfattere)
print(k)
print()
print()
print()
print()

def favbøk(favorittForf, forfattere):
    with open(forfattere, 'r', encoding='utf-8-sig') as forf:
        ut_data = {}
        forf_dic = {}
        f = [i.strip().split(',') for i in forf]
        
        for i in f:
            if i[0] not in forf_dic.keys():
                forf_dic.update({i[0]: [i[1]]})
            else:
                forf_dic[i[0]].append(i[1])

        for i in favorittForf.items():
            if i[0] not in ut_data.keys():
                ut_data.update({i[0]: forf_dic[i[1]]})            

        return ut_data

b = favbøk(favorittForfattere,'forfattere.txt')

print(b)
print()
print()
print()
print()

def skriv(b):
    for i in sorted(b):
        print(i,'----')
        for u in b[i]:
            print(u)

skriv(b)


tekst = 'Dette er en historie. Veldig enkel å forstå!'
vokaler = 'aeiouyøæå'

d = tekst.translate({ord(i): 'iiii' for i in vokaler})
print(d)


        


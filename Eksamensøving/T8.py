def ordliste():
    with open('ordlisteUTF8.txt', 'r', encoding='utf-8-sig') as ordliste:
        ord_i = input('Ord: ')
        elementer = [i.strip().split(',') for i in ordliste if len(i.strip().split(',')) == 2]
        dict_elementer = {}
        for i in elementer:
            dict_elementer.update({i[0]: i[1]})

        ut = [(i,y) for i,y in dict_elementer.items() if i.startswith(ord_i.lower())]
        if len(ut) > 0:
            for i in ut:
                print(f'{i[0]} ={i[1]}')
        else:
            print(f'{ord_i} finnes ikke i ordlisten')
            
        
        
def adresser():
    kontakter = {}
    with open('adresse.txt', 'r', encoding='utf-8-sig') as adresse:
        adre = [i.strip().split(' ') for i in adresse]
        for i in adre:
            if i[0] not in kontakter.keys():
                kontakter.update({i[0]: i[1::]})
    print(kontakter)
    with open('adresse.txt', 'w', encoding='utf-8-sig') as adresse:
        navn = input('Navn: ')
        adress = input('Adresse: ')
        nr = input('Hus nr: ')
        kontakter.update({navn: [adress, nr]})
        for i in sorted(kontakter):
            adresse.write(f'{i} {kontakter[i][0]} {kontakter[i][1]}\n')
    

def liste(k, r, l=0):
    m = l
    liste_rep = [['0' for i in range(r)]for i in range(k)]
    if len(m)>0:
        for i in liste_rep:
            for u in i:
                k = i.index(u)
                i.pop(k)
                i.insert(k, m.pop(0))
        
    for i in liste_rep:
        for u in i:
            print(f'{str(u).center(10)}', end=' ')
        print()
        
x=[1,2,3,4,5,6,7,8,9,10,11,12]

from statistics import mean

def temp():
    with open('tempFil.txt', 'r', encoding='utf-8-sig') as fil:
        m = [i.strip().split(' ') for i in fil if len(i.strip().split(' ')) == 3]
        k = [tuple(i) for i in m]
        return k

tuples = temp()
print(tuples)

def sett():
    global tuples
    sted = input('Sted: ')
    dag = input('Dag: ')
    temp = input('Temperatur: ')
    tuples.append((sted, dag, temp))

def snitt():
    global tuples
    over = {}
    for i in tuples:
        if i[0] not in over.keys():
            over.update({i[0]: [float(i[2])]})
        else:
            over[i[0]].append(float(i[2]))

    for i in over:
        s = mean(over[i])
        print(f'{i}: {s:.1f}')

def lagre():
    with open('tempFil.txt', 'w', encoding='utf-8-sig') as fil:
        for i in sorted(tuples):
            fil.write(f'{i[0]} {i[1]} {i[2]}\n')
        






















        

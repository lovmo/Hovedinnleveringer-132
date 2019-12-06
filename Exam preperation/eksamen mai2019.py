def liste1(liste):
    for verdi in liste:
        print(verdi)

def liste3(liste):
    ny_liste = [ liste[i:i+3] for i in range(0, len(liste), 3)]
    for verdier in ny_liste:
        for verdi in verdier:
            print(f'{str(verdi).center(6)}', end=' ')
        print()

x = [1,2,3,1,2,3,1,2,3,1,2,4,5,1,3,1,3,1,5,57,8,89,235,124,5,21]

from tkinter import *

class GUI:

    def __init__(self, master):
        self.master = master

        self.Knapp = Button(self.master, text='Trykk her', command=self.funksjon)
        self.Knapp.grid(row=0, column=1)

    def funksjon(self):
        self.nyttvindu = Toplevel(self.master)
        self.tekst = Label(self.nyttvindu, text='Takk!', width=6)
        self.tekst.grid(row=0, columnspan=6)


#m = Tk()
#l = GUI(m)
#m.mainloop()

def slå(liste):
    ny_liste = []
    for i in liste:
        for u in i:
            ny_liste.append(u)
    return ny_liste
        
p = [[1, 2], ['tre', 'fire', 'fem'], [6, 'sju']]


def csv():
    with open('hei.csv', 'r', encoding='utf-8-sig')as varer:
        l = [i.strip().split(';') for i in varer]
        for varer in l:
            for vare in varer:
                varer.insert(3, float(varer.pop(3)))
        m = [tuple(i) for i in l]
        return m

liste_tup = csv()
print(liste_tup)
print()
print()
print()

def ordb(liste):
    bok = {}
    for i in liste:
        if i[0] not in bok.keys():
            bok.update({i[0]: [(i[2],i[3])]})
        else:
            bok[i[0]].append((i[2],i[3]))
    return bok

bok = ordb(liste_tup)
print(bok)

print()
print()
print()

def listpris(bok, dato):
    priser = []
    if dato in bok:
        for i in bok[dato]:
            priser.append(i[1])
    return priser

priser = listpris(bok, "03.11.2018")
print(priser)
print()
print()
print()

def sum_salg(bok, datoer):
    priser = []
    for i in datoer:
        if i in bok.keys():
            for verdier in bok[i]:
                priser.append(verdier[1])
    priser_ut = '+'.join([str(i) for i in priser])
    return f'som gir {sum(priser)} ({priser_ut}).'
        
    
    








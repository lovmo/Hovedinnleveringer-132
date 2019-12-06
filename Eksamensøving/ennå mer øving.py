i=1
while i<4:
    for m in 'ab':
        print(i,m)
    i=i+1


x = 1
y = 'asd'

def bytt(x,y):
    x = y
    y = x

def liste1(liste):
    for i in liste:
        print(i)

def liste3(liste):
    m = [liste[i:i+3] for i in range(0,len(liste),3)]
    for i in m:
        for u in i:
            print(u, end=' ')
        print()

from tkinter import *

class GUI:

    def __init__(self, master):
        self.master = master

        self.knapp = Button(self.master, text='Trykk her', command=self.nyttvindu)
        self.knapp.grid(row=0, column=0)

    def nyttvindu(self):
        self.vindu = Toplevel(self.master)
        self.tekst = Label(self.vindu, text='Takk!')
        self.tekst.grid(row=0, column=0)


m = Tk()
l = GUI(m)
m.mainloop()


op = [[1, 2], ['tre', 'fire', 'fem'], [6, 'sju']]

def liste_s(liste):
    ut = []
    for i in liste:
        for u in i:
            ut.append(u)
    return ut


favorittForfattere={'Per':'Christie','Kari':'Ibsen', \
 'Liv':'Rowling','Ola':'Ibsen', \
'Anne':'Allende', 'Jens':'Christie'}



def forfatterListe(favorittForfattere):
    forf = [i for i in favorittForfattere.values()]
    return sorted(set(forf))


for1 = forfatterListe(favorittForfattere)
print(for1)
print()
print()
print()


def fans(forf):
    fans_dict = {}
    for i in forf.items():
        if i[1] not in fans_dict.keys():
            fans_dict.update({i[1]: [i[0]]})
        else:
            fans_dict[i[1]].append(i[0])
    return fans_dict

for2 = fans(favorittForfattere)
print(for2)
print()
print()
print()


def favorittBøker(pers, fil):
    with open(fil, 'r', encoding='utf-8-sig') as forfattere:
        bøker = [i.strip().split(',') for i in forfattere]

        bøker_dict = {}
        for i in bøker:
            if i[0] not in bøker_dict.keys():
                bøker_dict.update({i[0]: [i[1]]})
            else:
                bøker_dict[i[0]].append(i[1])

        for per in pers:
            for forfatter in bøker_dict:
                if forfatter in pers[per]:
                    pers[per] = bøker_dict[forfatter]

        return pers

for3 = favorittBøker(favorittForfattere, 'forfattere.txt')
print(for3)
print()
print()
print()

def skriv(b):
    for i in sorted(b):
        print(i, '-----')
        for v in b[i]:
            print(v)
        print()




    
        


























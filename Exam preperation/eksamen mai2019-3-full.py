# Eksamen 27.05.2019

#oppgave 1

#a1.
'''
En variabel et objekt som kan få en tilordnet verdi. En variabel kan bestå av integers,
floats, strings, klasser osv...
'''

#a2.
'''
GUI-element kan komme i flere varianter, som Buttons, Radiobuttons, Labels osv... Dette
er elementer som vises grafisk i GUIen, og som en bruker kan interagere med. Alle GUI
elementene befinner seg innenfor GUI rammen/vinduet.
'''

#A3
'''
En ordbok(dictionary) er en måte å sortere data på. Python har en inebygd hashing funksjon
som organiserer og sorterer dataen i en ordbok. Dette sørger for at søketiden blir
redusert betydelig sammenlignet med feks lister. En dictonary består av key og value par.
En dictionary er immutable, noe som betyr at nøkler ikke kan endres på. 
'''

#A4
'''
Break og Continue benyttes når man snakker om loops. Break benyttes for å bryte en løkke,
hoppe ut og fortesette med resten av programmet. Hvis Continue blir brukt i en løkke,
vil løkken hoppe over et steg i syklussen hvis en betingelse er oppfylt.
'''

#A5
'''
Arv benyttes i klasser, og benyttes for å gi ekstra/spesielle attributter til arv klassen,
som super klassen ikke har. Et arv objekt arver alle attributtene til super klassen.
'''

##B
'''
liste = append
iterasjon = break
modul = import
GUI = mainloop()
Operatropresedens = PEMDAS
funksjon = return
fil = open
klasse = Super()
Bool'ske uttrykk = False
Fortegnelse = items()
'''

##C
'''
En datamaskin består av 5 hovedkomponenter. En CPU (Central prosessing unit),
ALU (Arithmetic/Logic unit), RAM (Random access memmory), Input og Output. CPUen er
hjernen i datamaskinen, og får instruksene om hvilke oppgaver den skal utføre av RAM.
RAM er en rask og midlertidig lagringsenhet, og alle programmer som kjøres på datamaskinen
lastes inn i RAM. Gjennom en FETCH/EXECUTE syklus henter CPU ut instruksjoner fra RAM,
og utfører alle regneprosesse ved hjelp av ALU. Input sørger for at datamaskinen kan ta inn
signaler fra en mus, eller tastatur, skjermkort osv. Output sender ut signaler til feks
en skjerm.
'''

#D1 --> i.0
#D2 --> i. Returnerer en resultatverdi og kan ha side-effekter.
#D3 --> i.8
#D4 --> USIKKER

##E --> 1, 3, 4

# Oppgave 2.

#A1 --> 6
#A2 --> ['3', 'fire']
#A3 --> 1
#[1,'to',3,'fire',5,'seks',1,'to',3,'fire',5,'seks']

#(x+x) --- [   x[2]:  x[2]+x[4]  ] --- [(x+x)[8]]
#()[3:8] [3]
#['fire',5,'seks',1,'to']


#A4 --> 12
#A5 -->
def f(x): return x*x

print('Oppgave 2, 5a.\n')
for i in (1, 2, 3):
    print(str(i)+':'+str(f(i)))
      
print()
print()
      
# '1:1'
# '2:4'
# '3:9'


##B
i=1
while i<4:
    for y in 'ab':
         print(i, y)
    i=i+1

##D1

liste = [1,2,3,4,5,6,7,8,9,10]

def liste1(liste):
    for i in liste:
        print(i)

l1 = liste1(liste)

print()
print()
print()
print()

##D2

def liste3(liste):
    ny = [liste[i:i+3] for i in range(0,len(liste), 3)]
    for i in ny:
        for u in i:
            print(u, end=' ')
        print()
liste3(liste)
print()
print()
print()

##E

from tkinter import * 

class GUI:

    def __init__(self, b):
        self.b = b
        self.knapp = Button(self.b, text='Trykk her!', width=10, command=self.nytt_vindu)
        self.knapp.grid(row=0, column=0)

    def nytt_vindu(self):
        self.vindu = Toplevel(self.b)
        self.txt = Label(self.vindu, text='Takk', width=10)
        self.txt.grid(row=0, column=0)

G = Tk()
X = GUI(G)
G.mainloop()

##F

inn = [[1, 2], ['tre', 'fire', 'fem'], [6, 'sju']]

def slå_sammen(liste):
    sammenslått = []
    for i in liste:
        for u in i:
            sammenslått.append(u)
    return sammenslått

sammen = slå_sammen(inn)

print(sammen)
print()
print()
print()


# Oppgave 3.


favorittForfattere={'Per':'Christie','Kari':'Ibsen', \
 'Liv':'Rowling','Ola':'Ibsen', \
'Anne':'Allende', 'Jens':'Christie'}

##A

def forfatterListe(fav):
    forf = [i for i in fav.values()]
    return sorted(set(forf))

forf_liste = forfatterListe(favorittForfattere)
print(forf_liste)
print()
print()
print()


##B

def fans(fav):
    forfattere = {}
    for i in fav.items():
        if i[1] not in forfattere.keys():
            forfattere.update({i[1]: [i[0]]})
        else:
            forfattere[i[1]].append(i[0])
    return forfattere

fans_forf = fans(favorittForfattere)
print(fans_forf)
print()
print()
print()

##C

def favorittBøker(fav, fil):
    with open(fil, 'r', encoding='utf-8-sig') as forfattere:
        import_bøker = [i.strip().split(',') for i in forfattere]

        # Legger inn forfattene som keys, og bøkene som values.
        bøker = {}
        for element in import_bøker:
            if element[0] not in bøker.keys():
                bøker.update({element[0]: [element[1]]})
            else:
                bøker[element[0]].append(element[1])
                
        # Iterere gjennom fav, og bruker verdiene som tilhører nøklene
        # for å identifisere forfatteren
        f = {}
        for navn in fav:
            if fav[navn] in bøker.keys():
                f.update({navn: bøker[fav[navn]]})
        # Returnerer en ny dictionary
        return f


fav_bøker = favorittBøker(favorittForfattere, 'forfattere.txt')
print(fav_bøker)
print()
print()
print()

def skriv(b):
    for i in sorted(b):
        print(i)
        for u in b[i]:
            print(u)
        print()

skriv(fav_bøker)




            















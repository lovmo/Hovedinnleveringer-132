# H3
from random import sample

spar='\u2660'
ruter='\u2666'
kløver='\u2663'
hjerter='\u2665'

class kort:

    def __init__(self):
        self.symboler = [spar, kløver, ruter, hjerter]
        self.verdier = ['7','8','9','10','J','Q','K','A']
        self.alle = []
        for symbol in self.symboler:
            for verdi in self.verdier:
                self.alle.append(symbol+verdi)
        self.alle_kort = sample(alle, len(alle))
        self.bunker = [self.alle_kort[i:i+4] for i in range(0,len(self.alle_kort),4)]

    def p(self):
        print(self.bunker)



alle_bunker = kort
print(alle_bunker)



def engine():
    alle_bunker = kort.bunker

    while True:
        aktiv = [i[0] for i in alle_bunker]
        valg = ['A','B','C','D','E','F','G','H']
        ut = []
        for i in aktiv:
            indeks = aktiv.index(i)
            if len(alle_bunker[indeks])==0:
                continue
            else:
                ut.append([i])
                
    
    

        

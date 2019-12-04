'''
Temaoppgave 5, Vetle Løvmo Endresen

Eventuelle teorispørsmål kan besvares med multiline-kommentarer som denne.
'''


# Oppgave 1
def antallVokaler(streng):
    vokaler = list('aeiouyæøå')

    if any(v in vokaler for v in streng):
        total_antall_vokaler = 0
        for x in streng:
            total_antall_vokaler += vokaler.count(x)
        return (total_antall_vokaler)
    else:
        return 'Ingen vokaler i setningen'

streng = antallVokaler(list(input('Setning: ').lower()))
print(streng)

'''
Alternativt så kan du skrive inn antallVokaler('DIN SETNING')
Funksjonen returnerer da antall vokaler automatisk.  
'''

# Oppgave 2

TV = '''
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''
print(TV)

def splitter():
    liste = TV.split('\n')
    del liste[:2]
    del liste[-1]
    ny = []
    for i in liste:
        x = i.split(': ')
        ny.append(tuple(x))
    lib = dict(ny)
    return lib

'''Finnes det en enklere måte å konvertere listen til en dict? '''

def verv(person):
    p = person.lower()
    lib = splitter()
    seperat_liste = []
    for nøkkel, medlem in lib.items():
        if p == medlem.lower():
            seperat_liste.append(nøkkel)
    print(seperat_liste)





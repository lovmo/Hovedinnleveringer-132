'''
Temaoppgave 6, Vetle Løvmo Endresen

Eventuelle teorispørsmål kan besvares med multiline-kommentarer som denne.
'''


# Oppgave 1

def add(str):
    with open('telefon.txt', 'r') as telefonliste:
        with open('telefon.txt', 'a') as t:
            t.write(str + '\n')
        print('Gjeldende liste: ')
        for lines in telefonliste:
            print(lines, end='')


while True:
    print('Legg til nye kontakter i telefonkatalogen.')
    print('1. Legg til ny kontakt')
    print('2. Avslutt\n')
    valg = input('Ditt valg: ')

    if valg == '1':
        print('Legg til navn og nummer, avslutt med <enter>')
        kontakt = input('Navn og nummer: ')
        add(kontakt)
    elif valg == '2':
        break


# oppgave 2

def change(navn, nr):
    with open('telefon.txt', 'r') as telefonliste:
        telefonL = []
        for i in telefonliste:
            telefonL.append(i.split())
        for i in telefonL:
            if navn in i:
                print(f'Gammelt telefonnummer: {i[1]}')
                telefonL.remove(i)
        with open('telefon.txt', 'w') as telefonliste:
            for i in telefonL:
                telefonliste.write(f'{i[0]} {i[1]}\n')
            telefonliste.write(f'{navn} {nr}\n')


change(input('Navn: '), input('Nr: '))


# Oppgave 3
def fjernVokaler():
    with open('tekst.txt', 'r') as fil:
        vokaler = 'aeiouyæøå'
        nySetning = fil.read().translate({ord(n): 10 for n in vokaler})
        with open('NYtreSmåKinesere.txt', 'w') as fil:
            fil.writelines(nySetning)

print('vokalene blir fjernet')
fjernVokaler()

'''
Benytter translate funksjonen for å enkelt mappe hvert vokal element i filen til typen None. 
Dette gjør det enkelt å slette enkelt bokstaver i setninger. 
'''

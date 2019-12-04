from random import sample
from time import sleep
from textwrap import wrap

spar = '\u2660'
ruter = '\u2666'
kløver = '\u2663'
hjerter = '\u2665'

inndata = []


class kortstokk():

    def __init__(self):
        self.symboler = [spar, ruter, kløver, hjerter]  # Liste med symbolene
        self.alle_kort = []  # Liste som skal holde alle kortene n = 32
        self.indiv = ['A', 'K', 'Q', 'J', '10', '9', '8', '7']  # Liste med alle attributtene for hvert symbol

        for i in self.symboler:  # Sørger for å opprette alle kortene og legger
            for n in range(len(self.indiv)):  # dem i alle_kort listen.
                self.alle_kort.append(self.indiv[n] + i)

        self.alle_kort = sample(self.alle_kort, len(self.alle_kort))  # Stokker alle kortene
        self.bunker = [self.alle_kort[i:i + 4] for i in
                       range(0, len(self.alle_kort), 4)]  # Splitter opp alle kortene i 8 bunker.


def valg():
    valg_konvert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    while True:
        valg1 = input('\nValg: ').upper()
        if valg1 == 'X':
            return valg1, valg1

        valg2 = input('Valg: ').upper()

        if (valg1 in valg_konvert) and (valg2 in valg_konvert):
            return valg_konvert[valg1], valg_konvert[valg2]

        else:
            print('Feil verdi. Prøv på nytt.')


def printer(utdata):
    """
    Lagde en funksjon som håndterer printing av spill interfacet. Sørger for at posisjoneringen til elementene er
    sentrert.
    :param utdata:
    :return:
    """
    print('{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}'.format(utdata[0][0], utdata[1][0], utdata[2][0],
                                                                    utdata[3][0], utdata[4][0], utdata[5][0],
                                                                    utdata[6][0], utdata[7][0]))
    print('{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}{:^4s}'.format(utdata[0][1], utdata[1][1], utdata[2][1],
                                                                    utdata[3][1], utdata[4][1], utdata[5][1],
                                                                    utdata[6][1], utdata[7][1]))
    print('{:^4d}{:^4d}{:^4d}{:^4d}{:^4d}{:^4d}{:^4d}{:^4d}'.format(utdata[0][2], utdata[1][2], utdata[2][2],
                                                                    utdata[3][2], utdata[4][2], utdata[5][2],
                                                                    utdata[6][2], utdata[7][2]))


def kort_syklus(alle_bunker):
    n = -1
    aktivt_dekk = []
    kontroll_liste = []
    valg = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in alle_bunker:
        n += 1
        if len(i) > 0:
            kontroll_liste.append(i[0][0])
            aktivt_dekk.append([valg[n], i[0], len(i)])
        else:
            aktivt_dekk.append([valg[n], '', len(i)])

    printer(aktivt_dekk)
    return aktivt_dekk, kontroll_liste


def fil_henter():
    """
    Henter inn en spillfil. Try/Except skal sørge for at brukeren får en ny spill.txt fil hvis den ikke allerede finnes
    i mappen programmet kjører. Hensikten er i hovedsak at bruker ikke har filen på forhånd, og skal opprette en ny
    fil første gangen programmet kjører (Dette er for å sikre at spill malen blir riktig)
    :return:
    """
    try:
        with open('spill.txt', 'r', encoding='utf-8-sig') as spill:
            # Tømmer listen inndata før vi importerer data fra save filen.
            inndata.clear()
            for i in spill:
                inndata.append(i.strip().split())
            inndata.pop(0)

    except FileNotFoundError:
        print('*' * 37)
        print(f' Finner ikke spillfilen (spill.txt).\n Oppretter ny fil: spill.txt... ')
        print('*' * 37, '\n')

        sleep(2)

        with open('spill.txt', 'w', encoding='utf-8-sig') as nytt_spill:
            nytt_spill.write('Bunker:\n')


def fil_lagre(utdata):
    """
    Sørger for at spillet kan lagres, uavhengig av antallet kort i hver bunke. Maks kort i bunken er 4, og laveste er 0.
    Bunker med antall 0 gir en tom liste [].
    :param utdata:
    :return:
    """
    with open('spill.txt', 'w', encoding='utf-8-sig') as spill:
        spill.write('Bunker:\n')
        for i in utdata:
            if len(i) == 4:
                spill.write(f'{i[0]} {i[1]} {i[2]} {i[3]}\n')
            elif len(i) == 3:
                spill.write(f'{i[0]} {i[1]} {i[2]}\n')
            elif len(i) == 2:
                spill.write(f'{i[0]} {i[1]}\n')
            elif len(i) == 1:
                spill.write(f'{i[0]}\n')
            elif len(i) == 0:
                spill.write(f'\n')


def brunksanvisning():
    print('\nTHE PACK')
    a = 'Remove all 2s - 6s to form a deck of 32 cards'
    pretty_a = wrap(a, 60)
    for text in pretty_a:
        print(text)

    print('\nTHE DEAL')
    b = 'Shuffle cards and deal 4 cards face down into a pile on the table. Deal the whole deck into piles of 4 ' \
        'cards, lining the piles up so that there are 8 total piles in a row from left to right. '
    pretty_b = wrap(b, 60)
    for text in pretty_b:
        print(text)

    print('\nTHE PLAY')
    c = 'Turn over the top cards of each pile so that they are face up. Take any cards that are pairs of the same ' \
        'kind, regardless of suit - two 10s, two Kings, etc. and clear them away.\nOnce you have removed a card from ' \
        'the top of the pile, turn over the next card on the pile so it is face up.\nTo win the game, you must clear ' \
        'away all piles in pairs. '
    pretty_c = wrap(c, 60)
    for text in pretty_c:
        print(text)

    print('\nRegler hentet fra: https://bicyclecards.com/how-to-play/wish-solitaire/')


def spill_modul():
    """
    Funksjonen starter med å sjekke om det er elementer i inndata listen. Hvis ikke opprettes en ny kortstokk
    ved bruk av klasse funksjonen vår.

    While loopen er selve kjernen i spillet og kjører i loop helt til spilleren, vinner, taper eller avslutter.

    While loop:
        Chech listen benyttes for å validere om det finnes par kombinasjoner på de øverste kortene. Benytter set()
        for å fjerne like kort. Er lengden på check og set() ulike, betyr dette at spillerene har kort å velge mellom.

        Spill_valg() henter ut valgene til brukeren. Sjekker først om spillet skal avsluttes, hvis ikke, vil det sjekkes
        om bruker har lagt inn gyldig kort kombinasjon.
    :return:
    """
    print('---Velkommen til Wish Solitaire---\n')
    print('Vennligst trekk kort... (A-H). Skriv (x) for å avslutte.')

    if len(inndata) > 0:
        alle_bunker = inndata

    else:
        alle_bunker = kortstokk().bunker

    while True:
        aktivt_dekk, kontroll_liste = kort_syklus(alle_bunker)
        if len(kontroll_liste) > len(set(kontroll_liste)):
            valg1, valg2 = valg()

            if valg1 == 'X':
                print('Ønsker du å lagre spillet?')
                a = input('Y/N:')
                if a.lower() == 'y':
                    fil_lagre(alle_bunker)
                    inndata.clear()
                    break
                else:
                    inndata.clear()
                    break

            elif aktivt_dekk[valg1][1][0] == aktivt_dekk[valg2][1][0]:
                alle_bunker[valg1].pop(0)
                alle_bunker[valg2].pop(0)

            else:
                print('Du har ikke valgt et gydlig par')

        elif len(kontroll_liste) == 0:
            print(hjerter * 26)
            print('GRATULERER DU HAR VUNNET!!')
            print(hjerter * 26)
            inndata.clear()
            break

        else:
            print('Du har dessverre tapt!\n')
            break


def start():
    while True:
        print('\n1 - Start nytt spill')
        print('2 - Hent lagret spill')
        print('3 - Bruksanvisning')
        print('4 - avslutt')
        print('Velg handling (0 for meny)\n')

        bruker_input = input('Valg: ')

        if bruker_input == '1':
            print('Starter nytt spill...\n')
            sleep(0.5)
            spill_modul()

        elif bruker_input == '2':
            print('Laster inn eksisterende spill...\n')
            fil_henter()
            spill_modul()
            sleep(0.5)

        elif bruker_input == '3':
            brunksanvisning()

        elif bruker_input == '4':
            break

        elif bruker_input == '0':
            continue


start()

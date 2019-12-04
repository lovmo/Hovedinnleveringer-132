'''
Hovedoppgave 3, Vetle Løvmo Endresen

For enkelthetsskyld er alle deloppgaver slått sammen i ett program. Jeg mener selv at oppgaven blir besvart riktig
ved å gjøre dette. Besvarelsen tar utgangspunkt i følgende:

-Data filen som lastes inn har et bestemt format. Hvis du ikke har spill.txt filen lagret på maskinen, vil programmet
    automatisk opprette en ny spill.txt med rett format.

-Data.txt malen ser slik ut:
    Bunker:
    ...
    ...

-Utformingen av dialogen er gjort etter egen tolkning av oppgaveteksten. Jeg har valgt å ikke ta med et eget valg i
    hoved menyen for å feks eventuelt lagre eller avslutte spillet. Denne funksjonen kjøres uansett, og brukeren vil
    få valget om å lagre eller ikke. Dette er for å skape mindre "friksjon" for brukeren i brukeropplevelsen.
'''
from random import sample
from time import sleep

spar = '\u2660'
ruter = '\u2666'
kløver = '\u2663'
hjerter = '\u2665'

# inndata listen inneholder by default 0 elementer. Hvis bruker laster opp en spillfil vil kort bunkene appendes denne
# listen
inndata = []


class Cards:
    """
    En klasse for hver bunke med kort. Veldig enkel struktur, hvor hver klasse inneholder et symbol og en liste med
    alle kortene innenfor det symbolet.
    """
    symbol = ''

    def __init__(self, symbol):
        self.symbol = symbol
        self.lib = ['A' + symbol, 'K' + symbol, 'Q' + symbol, 'J' + symbol, '10' + symbol, '9' + symbol, '8' + symbol,
                    '7' + symbol]

    def __repr__(self):
        return self.symbol


def bunker():
    """
    Funksjonen tar klasse objektene som er 4stk, og fletter dem sammen til en liste. Sample funksjonen lager en ny liste,
    satt tilfeldig sammen. Avslutningsvis deles listen opp i 8 deler.
    :return:
    """
    bunker_import = Cards(spar).lib + Cards(ruter).lib + Cards(kløver).lib + Cards(hjerter).lib
    usortert = sample(bunker_import, len(bunker_import))

    bun = int(len(usortert) / 8)
    alle_bunker = usortert[0:bun], usortert[bun:bun * 2], usortert[bun * 2:bun * 3], usortert[bun * 3:bun * 4], \
                  usortert[bun * 4:bun * 5], usortert[bun * 5:bun * 6], usortert[bun * 6:bun * 7], \
                  usortert[bun * 7:bun * 8]

    return alle_bunker


def spill_valg():
    """
    Sjekker inputen fra bruker. Bruker en dict til å konvertere bokstav input (A-H) til tall. Tallene benyttes som
    indeks nummer for å finne kortene som skal fjernes basert på valget til brukeren. Funksjonen tar også for seg hvis
    bruker ønsker å avslutte spillet.
    :return:
    :return:
    :return:
    """
    valg = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7
    }

    while True:
        valg_1 = input('\nBunke 1: ').upper()
        if valg_1 == 'X':
            return valg_1, valg_1

        valg_2 = input('Bunke 2: ').upper()

        if (valg_1 in valg) and (valg_2 in valg):
            return int(valg[valg_1]), int(valg[valg_2])

        else:
            print('Feil, valget er ugyldig.\n')


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


def poeng(utdata):
    """
    En tilleggsfunksjon for å holde styr på total antall kort som ligger ute. .
    :param utdata:
    :return:
    """
    kort_igjen = []
    for i in utdata:
        kort_igjen.append(i[2])

    return sum(kort_igjen)


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


def spill_interface():
    """
    Funksjonen starter med å sjekke om inndata listen er tom. Hvis den er tom, kjører funksjonen bunker(), og oppretter
    nye bunker. Er det elementer i inndata listen, vil spillet laste inn disse.

    While loopen er selve kjernen i spillet og kjører i loop helt til spilleren, vinner, taper eller avslutter.

    While loop:
        Chech listen benyttes for å validere om det finnes par kombinasjoner på de øverste kortene. Benytter set()
        for å fjerne like kort. Er lengden på check og set() ulike, betyr dette at spillerene har kort å velge mellom.

        Spill_valg() henter ut valgene til brukeren. Sjekker først om spillet skal avsluttes, hvis ikke, vil det sjekkes
        om bruker har lagt inn gyldig kort kombinasjon.
    :return:
    """

    if len(inndata) > 0:
        alle_bunker = inndata

    else:
        alle_bunker = bunker()

    print('---Velkommen til Wish Solitaire---\n')
    print('Vennligst trekk kort... (A-H). Skriv (x) for å avslutte.')
    valg = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    while True:
        n = -1
        check = []
        utdata = []

        for i in alle_bunker:
            n += 1
            if len(i) > 0:
                check.append(i[0][0])
                utdata.append([valg[n], i[0], len(i)])
            else:
                utdata.append([valg[n], '', len(i)])

        printer(utdata)
        print(utdata)
        print(f'\nDet er : {poeng(utdata)} kort igjen på bordet.')

        if len(check) > len(set(check)):
            valg1, valg2 = spill_valg()
            if valg1 == 'X':
                print('Ønsker du å lagre før du avslutter?')
                v = input('(Y/N): ')
                if v.lower() == 'y':
                    fil_lagre(alle_bunker)
                    inndata.clear()
                    break
                else:
                    inndata.clear()
                    break

            elif alle_bunker[valg1][0][0] == alle_bunker[valg2][0][0]:
                alle_bunker[valg1].pop(0)
                alle_bunker[valg2].pop(0)

            else:
                print('Du har ikke valgt et gydlig par')

        elif len(check) == 0:
            print(hjerter * 26)
            print('GRATULERER DU HAR VUNNET!!')
            print(hjerter * 26)
            break

        else:
            print('Du har dessverre tapt!\n')
            break


def start():
    while True:
        print('1 - start nytt spill')
        print('2 - hent lagret spill')
        print('3 - avslutt')
        print('Velg handling (0 for meny)\n')

        bruker_input = input('')

        if bruker_input == '1':
            print('Starter nytt spill...\n')
            sleep(0.5)
            spill_interface()

        elif bruker_input == '2':
            print('Laster inn eksisterende spill...\n')
            fil_henter()
            spill_interface()
            sleep(0.5)

        elif bruker_input == '3':
            break

        elif bruker_input == '0':
            continue


start()

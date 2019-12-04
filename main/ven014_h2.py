'''
Hovedoppgave 2, Vetle Løvmo Endresen

For enkelthetsskyld er oppgave 1a og 1b slått sammen i ett program. Jeg mener selv at oppgaven blir besvart riktig
ved å gjøre dette. Programmet er relativt fleksibelt og sikret for de fleste brukerfeil. Besvarelsen tar utgangspunkt
i følgende:

-Data filen som lastes inn har et bestemt format. Hvis du ikke har data.txt filen lagret på maskinen, vil programmet
    automatisk opprette en ny data.txt med rett format.

-Data.txt malen ser slik ut:
    Emner:
    (INFO100)

    Karakterer:
    (INFO100: B)

-Utformingen av dialogen er gjort etter egen tolkning av oppgaveteksten.
-Jeg har valgt å legge alle emner i en liste, mens karakterer er lagt i en dictionary.
'''

from statistics import mean
import time

emne_liste = []

karakterer = {}



def validator():
    """
    Validator sjekker bruker input til menyen. Hvis bruker velger alt annet enn 0-5, vil bruker få feilmelding.
    Brukeren vil få muligheten til å prøve på nytt helt til gyldig input er tastet inn.
    Lager en funksjon som forhindrer brukeren i å velge ugyldige valg.
    :return:
    """
    godkjente_valg = ['0', '1', '2', '3', '4', '5', '6']
    while True:
        inp = input('Velg handling (0 for meny): ')
        if inp in godkjente_valg:
            return inp
        elif inp.isnumeric():
            print('Du kan kun velge mellom 0-6\n')
        else:
            print('Ugyldig verdi!\n')


def karakter_validator(karakter):
    """
    Karakter_validator hjelper programmet med å sjekke om karakteren som brukes i funksjonen "sett_karakter" er
    gyldig. Bruker kan kun velge en karakter fra A-F eller legge igjen en blank karakter. Er input blank, vil en None
    verdi returneres. Denne verdien forteller en karakter i "karakterer" dictionary, skal slettes.
    :param karakter:
    :return:
    """
    godkjente_valg = ['A', 'B', 'C', 'D', 'E', 'F']
    if karakter.upper() in godkjente_valg:
        return karakter.upper()
    elif karakter is '':
        return None
    elif karakter.isnumeric():
        print('Du kan kun legge inn str verdi fra A-F')
    else:
        print('Ugyldig karakter\n')



def emne_validator(emne):
    """
    Emne_validator funksjonen sørger for at bruker legger inn en gyldig kurskode. Hvis input er riktig vil funksjonen
    returnere kurskoden med store bokstaver.
    :param emne:
    :return:
    """
    if len(emne) == 7 and emne[-3].isnumeric():
        d1_emne = emne[0:4]
        d2_emne = emne[4:7]
        d3_emne = int(emne[-3])
        if len(d1_emne) <= 4 and len(d2_emne) == 3 and d2_emne.isnumeric() and (1 <= d3_emne <= 3):
            return emne.upper()
        else:
            print('Ugyldig fagkode\n')
    elif len(emne) == 6 and emne[-3].isnumeric():
        d1_emne = emne[0:3]
        d2_emne = emne[3:6]
        d3_emne = int(emne[-3])
        if len(d1_emne) <= 3 and len(d2_emne) == 3 and d2_emne.isnumeric() and (1 <= d3_emne <= 3):
            return emne.upper()
        else:
            print('Ugyldig fagkode\n')
    else:
        print('Ugyldig emne\n')
        return None


def emne_valg(fag='', nivå=''):
    """
    Brukes for å sortere input om studieretning og nivå på faget. Returnerer alle emnene hvis det ikke oppgis noe fag.
    Tillater brukeren å bruke studieretningsnavn eller forkortet navn.
    :param fag:
    :param nivå:
    :return:
    """
    emner = []
    if fag.lower() == 'informasjonsvitenskap' or fag.lower() == 'info':
        for i in emne_liste:
            if i[0:3] == 'INF' and i[-3] == nivå:
                emner.append(i)
            elif i[0:3] == 'INF' and nivå is '':
                emner.append(i)
        return emner
    elif fag.lower() == 'økonomi' or fag.lower() == 'econ':
        for i in emne_liste:
            if i[0:3] == 'ECO' and i[-3] == nivå:
                emner.append(i)
            elif i[0:3] == 'ECO' and nivå is '':
                emner.append(i)
        return emner
    elif fag.lower() == 'geografi' or fag.lower() == 'geo':
        for i in emne_liste:
            if i[0:3] == 'GEO' and i[-3] == nivå:
                emner.append(i)
            elif i[0:3] == 'GEO' and nivå is '':
                emner.append(i)
        return emner
    elif fag is '' and nivå is '':
        for i in emne_liste:
            emner.append(i)
        return emner
    else:
        return None


def sett_karakter(emne, karakter):
    """
    Oppdaterer karakter dictionary med nye resultater eller sletter elementer hvis karakter input er lik None
    :param emne:
    :param karakter:
    :return:
    """
    if karakter is not None:
        karakterer.update({emne: karakter})
    elif karakter is None and emne in karakterer:
        karakterer.pop(str(emne))
    else:
        print('Oppdatering feilet!')


def snitt_desimal_kalulator(karakter):
    """
    Snitt_desimal_kalulator om desimal snittet til bokstav snitt
    :param karakter:
    :return:
    """
    liste = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 0,
    }
    if karakter in liste:
        return liste[karakter]


def desimal_til_bokstav(snitt):
    """
    Desimal_til_bokstav regner om desimal snittet til bokstav snitt
    :param snitt:
    :return:
    """
    if snitt >= 4.5:
        return 'A'
    elif 3.5 <= snitt < 4.5:
        return 'B'
    elif 2.5 <= snitt < 3.5:
        return 'C'
    elif 1.5 <= snitt < 2.5:
        return 'D'
    elif 0.5 <= snitt < 1.5:
        return 'E'
    else:
        return 'F'


def snitt(studie_retning):
    """
    snitt funksjonen samler sammen karakterene for de ulike studieretningene. Hvis bruker ikke oppgir studieretning,
    vile et totalt snitt for alle studieretningene returneres.
    :param studie_retning:
    :return:
    """
    alle_karakterer = karakterer.items()
    if studie_retning.lower() == 'informasjonsvitenskap' or studie_retning.lower() == 'info':
        informasjonsvitenskap = []
        for i in alle_karakterer:
            if (i[0][0:3]) == 'INF':
                informasjonsvitenskap.append(snitt_desimal_kalulator(i[1]))
        gj_snitt = desimal_til_bokstav(round(mean(informasjonsvitenskap), 2))
        return f'\nSnitt for {studie_retning.upper()}: {gj_snitt}'

    if studie_retning.lower() == 'økonomi' or studie_retning.lower() == 'econ':
        økonomi = []
        for i in alle_karakterer:
            if (i[0][0:3]) == 'ECO':
                økonomi.append(snitt_desimal_kalulator(i[1]))
        gj_snitt = desimal_til_bokstav(round(mean(økonomi), 2))
        return f'\nSnitt for {studie_retning.upper()}: {gj_snitt}'

    if studie_retning.lower() == 'geografi' or studie_retning.lower() == 'geo':
        geografi = []
        for i in alle_karakterer:
            if (i[0][0:3]) == 'GEO':
                geografi.append(snitt_desimal_kalulator(i[1]))
        gj_snitt = desimal_til_bokstav(round(mean(geografi), 2))
        return f'\nSnitt for {studie_retning.upper()}: {gj_snitt}'

    else:
        if len(list(karakterer)) > 0:
            totalt_snitt = []
            for i in alle_karakterer:
                totalt_snitt.append(snitt_desimal_kalulator(i[1]))
            gj_snitt = desimal_til_bokstav(round(mean(totalt_snitt), 2))
            return f'\nTotalt snitt: {gj_snitt}'
        else:
            return f'\nDu har ikke lagt inn noen karakterer enda.\n'


def laste_data():
    try:
        with open('data.txt', 'r') as data:
            input_liste = []
            for i in data:
                input_liste.append(i.strip())

            # Data filen splittes i to, i linjeskiftet mellom siste element i Fag listen og starten på Karakter listen
            index_splitter = input_liste.index('')

            # Legger over emne listen til "emne_liste" og k
            emne_liste.extend(input_liste[1:index_splitter])
            karakter_liste = input_liste[index_splitter + 2:]

            for i in karakter_liste:
                karakterer[i[:-3]] = i[-1]
    # Hvis data.txt filen ikke finnes, benyttes en except funksjon for å opprette en ny data.txt fil med rett format.
    except FileNotFoundError:
        print('\n--------------------------------')
        print('Kunne ikke finne data.txt filen.')
        print('Oppretter fil, med riktig format')
        print('--------------------------------\n')
        with open('data.txt', 'w') as ny_datafil:
            ny_datafil.write(f'Fag: \n')
            ny_datafil.write(f'Karakterer: \n')
        time.sleep(2.5)


def fjerner_ugyldige_karakterer():
    """
    En funksjon som ved starten sjekker om det ligger karakterer i fag som ikke eksiterer i emne listen. De karakterene
    som ikke eksisterer i emne listen blir fjernet.
    :return:
    """
    for i in list(karakterer):
        if i not in emne_liste:
            print('Ugyldige fag som fjernes:', i)
            karakterer.pop(i)


def lagre_data():
    with open('data.txt', 'w') as data:
        data.write('Fag: \n')
        for i in sorted(emne_liste):
            data.write(f'{i}\n')

        data.write('\nKarakterer:\n')
        for n in karakterer.items():
            data.write(f'{n[0]}: {n[1]}\n')


'''Henter emner og karakterer fra data filen. Legger til i emne_liste og karakterer. Passer på at ingen ugyldige
karakterer ligger i data filen.'''
laste_data()
fjerner_ugyldige_karakterer()


def start():
    while True:
        print('----------------')
        print('1 Emneliste')
        print('2 Legg til emne')
        print('3 Sett karakter')
        print('4 Karaktersnitt')
        print('5 Lagre')
        print('6 Avslutt og lagre')
        print('----------------')
        inp = validator()

        if inp == '0':
            continue
        elif inp == '1':
            fag = input('Fag: ')
            nivå = input('Nivå: ')
            presentasjon_av_emner = emne_valg(fag, nivå)
            if presentasjon_av_emner is not None:
                print(f'\nRegistrerte emner ({len(presentasjon_av_emner)} av {len(emne_liste)}):')
                for i in presentasjon_av_emner:
                    print(f'--{i}')
            else:
                print('Du har tastet inn ugyldig informasjon. \nFagkode eller nivå kan være feil')

        elif inp == '2':
            nytt_emne = emne_validator(input('Nytt emne: '))
            if nytt_emne is not None:
                emne_liste.append(nytt_emne)

        elif inp == '3':
            while True:
                nyttemne = emne_validator(input('Emne: \n'))
                nykarakter = karakter_validator(input('Karakter: \n'))

                if nyttemne is not None and nyttemne in emne_liste:
                    sett_karakter(nyttemne, nykarakter)
                    for x in karakterer.items():
                        print(f'Fag: {x[0]} || Resultat: {x[1]}')
                    break
                else:
                    print('Faget finnes ikke i faglisten.')
                    avslutt_loop = input('Skriv 0 for å gå til menyen eller (ENTER) for å prøve igjen. \n')
                    if avslutt_loop == '0':
                        break

        elif inp == '4':
            print(snitt(input('Retning: ')))

        elif inp == '5':
            lagre_data()
            print('Du har lagret alt av data\n')

        elif inp == '6':
            avslutt = input('Vil du lagre endringene? (j/n): ')
            if avslutt.lower() == 'j':
                lagre_data()
                print('Takk for nå! Alt er nå lagret trygt i filen.')
            else:
                print('Takk for nå! Ingen endringer lagret.')
            time.sleep(0.5)
            break


start()

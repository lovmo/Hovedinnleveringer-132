y = lambda i: len(i) == 2


def tlf():
    with open('telefon.txt', 'a', encoding='utf-8-sig') as fil:
        nyNr = []

        while True:
            x = input('Navn og nummer: ')
            if x == '':
                break
            else:
                nyNr.append(x.split(' '))

        nyNr = filter(y, nyNr)
        
        for i in nyNr:
            fil.write(f'{i[0]} {i[1]}\n')
        print('Suksess!')



def en():
    with open('telefon.txt', 'r', encoding='utf-8-sig') as fil:
        l = [i.strip().split(' ') for i in fil]
        navn = input('Navn: ')
        for i in l:
            if navn in i:
                print(f'Gammelt telefonnummer: {i[1]}')
                ny = input('Nytt nr:')
                i.pop(1)
                i.insert(1, ny)
    with open('telefon.txt', 'w', encoding='utf-8-sig') as fil:
        for i in l:
            fil.write(f'{i[0]} {i[1]}\n')
        print('Suksess!')


def fjern():
    with open('tresmåkinesere.txt', 'r', encoding='utf-8-sig') as fil:
        tekst = ''
        for i in fil:
            tekst += i
        vokaler = 'aeiouæøåy'
        ny = tekst.translate({ord(i): None for i in vokaler})
        
    with open('tresmåkinesereNY.txt', 'w', encoding='utf-8-sig') as fil:
        fil.writelines(ny)
        
        
        

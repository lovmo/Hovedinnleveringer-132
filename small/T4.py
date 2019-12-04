'''
Temaoppgave 4, Vetle Endresen

Eventuelle teorispørsmål kan besvares med multiline-kommentarer som denne.
'''

class Album:
    antAlbum = 0
    #Oppretter et serie nummer til albumet
    def nr(self):
        Album.antAlbum += 1
        self.nr = self.antAlbum
        return self.nr

    def __init__(self, album):
        self.album = album

    def __repr__(self):
       return (f'{self.album}')


class Artist:
    def __init__(self, navn ):
        self.navn = navn

    #Legger til medlemmene i musikkbandet.
    #Splitter opp str i en liste. Splitter str der hvor det er komma.
    def medl(self, medlemmer):
        self.medlemmer = medlemmer
        self.medlemmListe = self.medlemmer.split(', ')

    #Sjekker om artisten er soloartist eller gruppe.
    #Returnerer en str.
    def status(self):
        if len(self.medlemmListe) == 1:
            return (f'Soloartist')
        elif len(self.medlemmListe) > 1:
            return (f'Gruppe')

    def __repr__(self):
        return (f'{self.navn}')

class Sang:
    def __init__(self, sang):
        self.sang = sang

    def komp(self, komponist):
        self.komponist = komponist

    def __repr__(self):
        return (f'{self.sang}')

#Første data
Abbey_Road = Album('Abbey Road')
beatles = Artist('The Beatles')
beatles.medl('John Lennon, Ringo Starr, Paul McCartney, George Harrison')
Here_Comes_the_Sun = Sang('Here Comes the Sun')
Here_Comes_the_Sun.komp('George Harrison')

#Andre data
Greatest_Hits = Album('Greatest Hits')
Queen = Artist('Queen')
Queen.medl('Freddie Mercury, Brian May, Roger Taylor, John Deacon')
Bohemian_Rhapsody = Sang('Bohemian Rhapsody')
Bohemian_Rhapsody.komp('Freddie Mercury')

#Tredje data
Thriller = Album('Thriller')
Jackson = Artist('Michael Jackson')
Jackson.medl('Michael Jackson')
Billie_Jean = Sang('Billie Jean')


album_liste = []
sang_liste = []
artist_liste = []

album_liste.extend([Abbey_Road.album, Greatest_Hits.album, Thriller.album])
artist_liste.extend([beatles.navn, Queen.navn, Jackson.navn])
sang_liste.extend([Here_Comes_the_Sun.sang, Bohemian_Rhapsody.sang, Billie_Jean.sang])

def søk():
    artist = input('Navnet på artisten: ')
    if artist in artist_liste:
        listeNr = artist_liste.index(artist)
        print(f'Album: {album_liste[listeNr]}, Sang: {sang_liste[listeNr]}')
    else:
        print('-'*16*len(album_liste))

        for n in album_liste:
            print(n, end=' || ')

søk()
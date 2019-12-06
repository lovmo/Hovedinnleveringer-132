## Klasser og sub klasser

class General:

    def __init__(self, navn, fnr):
        self.navn = navn
        self.fnr = fnr

    def __repr__(self):
        return f'{self.navn}, {self.fnr}'

    def skriv(self):
        print('Helllloo')


class It(General):

    def __init__(self, navn, fnr, erfaring, form):
        super().__init__(navn, fnr)
        self.erfaring = erfaring
        self.form = form
        
    def __repr__(self):
        return f'{self.navn}, {self.fnr}, {self.erfaring}, {self.form}'

    def shi(self):
        print('Hemmelig')



x = General('Tore', '26.11.1996')
y = It('Vetle', '25.08.1996', '3år', 'Avdelingsleder')

print(x)
print(y)



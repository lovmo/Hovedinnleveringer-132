'''
Temaoppgave 1, Vetle Endresen

Eventuelle teorispørsmål kan besvares med multiline-kommentarer som denne.
'''

# Oppgave 1

#alternativ 1
print('Vetle')
print('Endresen')

#alternativ 2
fornavn = input('Fornavn -mellomnavn:')
etternavn = input('Etternavn: ')
print('', fornavn, '\n', etternavn)

# Oppgave 2

print("*           * ******* ******* *       *******")
print(" *         *  *          *    *       *      ")
print("  *       *   *          *    *       *      ")
print("   *     *    *******    *    *       *******")
print("    *   *     *          *    *       *      ")
print("     * *      *          *    *       *      ")
print("      *       *******    *    ******* *******")

# Oppgave 3a

x = input('Legg inn beløp sang_liste NOK: \n')
euro = round(int(x)*0.10248, 2)
dollar = round(int(x)*0.1162, 2)

print(x, 'kroner tilsvarer', euro, 'Euro og', dollar, 'dollar')

# Oppgave 3b

print('\nKonvertering med spesialtegnenene \N{euro sign} og \N{dollar sign}:')
print('NOK', x, 'tilsvarer',str(euro)+'\N{euro sign} og', str(dollar)+'\N{dollar sign}')

## Getränke
cola = 'cola'
fanta = 'fanta'
wasser = 'wasser'

## Schleifenvariable
antwort = 'j'

def getraenkAbfrage():
    print('Möchten Sie ein weiteres Getränk kaufen? j/n')

def getraenkeAuswahl():
    getraenk = '7'
    while getraenk != '1' and getraenk != '2' and getraenk != '3':
        print('Wählen Sie ein Getränk aus:\n - 1. Cola CHF 1.20\n - 2. Fanta CHF 2.10\n - 3. Wasser CHF 100.-')
        getraenk = input()

        match getraenk:
            case '1':
                print('Sie haben Cola ausgewählt')
            case '2':
                print('Sie haben Fanta ausgewählt')
            case '3':
                print('Sie haben Wasser ausgewählt')
            case _:
                print('Das ist keine gültige Option')
    getraenkAbfrage()

while antwort == 'j':
    getraenkeAuswahl()
    antwort = input()

    while antwort != 'j':
        if antwort == 'n':
            break
        else:
            print('Das ist keine gültige Antwort. Bitte wählen Sie j für Ja und n für Nein.')
            getraenkAbfrage()
            antwort = input()

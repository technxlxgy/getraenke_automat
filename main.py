## Getränke
cola = 'cola'
fanta = 'fanta'
wasser = 'wasser'

## Preise
preis_cola = 1.2
preis_fanta = 2.1
preis_wasser = 100.0
preis_total = 0


## Methode zum Getränke Abfragen
def getraenkAbfrage():
    print('Möchten Sie ein weiteres Getränk kaufen? j/n')


## Schleifenvariable
antwort = 'j'

while antwort == 'j':
    getraenk = None

    while getraenk != '1' and getraenk != '2' and getraenk != '3':

        print('Wählen Sie ein Getränk aus:\n - 1. Cola CHF 1.20\n - 2. Fanta CHF 2.10\n - 3. Wasser CHF 100.-')
        getraenk = input()

        match getraenk:
            case '1':
                print('Sie haben Cola ausgewählt')
                preis_total += preis_cola
            case '2':
                print('Sie haben Fanta ausgewählt')
                preis_total += preis_fanta
            case '3':
                print('Sie haben Wasser ausgewählt')
                preis_total += preis_wasser
            case _:
                print('Das ist keine gültige Option')

    getraenkAbfrage()
    antwort = input()

    while antwort != 'j':
        if antwort == 'n':
            break
        else:
            print('Das ist keine gültige Antwort. Bitte wählen Sie j für Ja und n für Nein')
            getraenkAbfrage()
            antwort = input()

    
print("Der Gesamtpreis beträgt CHF ", round(preis_total, 2))
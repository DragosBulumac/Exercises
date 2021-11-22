# 306 Lista
# Lista de cumparaturi 
# CP - 26/01/2013

lista = []								# Initializam lista

print ( '\t\t Bine ati venit la programul lista de cumparaturi' )

while True:
    print ( """Introduceti:
0 - Pentru afisare lista actuala
1 - Pentru introducerea unui element nou
2 - Pentru stergerea unui element existent
3 - Pentru stergerea intregii liste
q - Pentru iesire
""" )
    alegere = input ( 'Introduceti optiunea - dintre cele enumerate:\n\t' )

    if alegere == '0':
        if lista:  						# Daca lista nu e goala...
            lista.sort ( )
            print ( 'Lista cumparaturi este :\n' )
            print('-' * 30)
            for e in lista:
                print ( '=>', e )
            print('-' * 30)
        else:
            print ( 'Lista este goala\n' )
            print('-' * 30)
    elif alegere == '1':
        el_nou = input ( 'Elementul nou este:\n\t' )
        lista.append ( el_nou )
        print('-' * 30)
    elif alegere == '2':
        if lista:
            sterge = input ( 'Ce element doresti sa stergi? \n' )
            if sterge in lista:
                lista.remove( sterge )
                print ( 'Elementul ', sterge, 'a fost sters\n' )
                print('-' * 30)
            else:
                print ( sterge, 'nu a fost gasit in lista\n' )
                print('-' * 30)
        else:
            print ( 'Lista e goala\n' )
            print('-' * 30)
    elif alegere == '3':
        lista = []
        print ( 'Lista a fost stearsa\n' )
        print('-' * 30)
    elif alegere.upper ( ) == 'Q':
        print('-' * 30)
        break
print ( 'Va multumim ca ati ales acest program!\n' )

input ( 'Apasa <enter> pt a iesi.' )

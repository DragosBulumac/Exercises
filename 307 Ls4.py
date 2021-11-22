# 307 Lista
# Lista - metode aplicabile
# PF - 27/05/2016

# Metode aplicabile unei liste
week = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri']
print ( week )
week.append ( 'Sambata' )
print ( week )
week.extend ( ['Duminica', 'New_Day'] )
print ( week )
week.count ( 'Luni' )
print ( week )
week.remove ( 'New_Day' )
print ( week )
week.index ( 'Joi' )
week.index ( 'Vineri' )
week.pop ()
week.insert ( 6, 'Duminica' )
print ( week )
week.reverse ( )
print ( week )

# cream o lista identica pentru a o sorta (nu schimbam ordinea in lista initiala)
week1 = week.copy()

print ( week1 )
week1.sort ( )
print ( week1 )

week1 = list ( week )

del week1  								# nu este o metoda, este o functie
max ( week )
min ( week )
lista1 = [3, 7, 13]
sum ( lista1 )  						# doar pentru elem numerice
sum ( lista1 ) / len ( lista1 )  		# media aritmetica

# Dublu split intr-un text
x = 'From paul@infoacademy.net Tue May  24 22:22:22 2016'
lista_cuv = x.split ( )
print ( lista_cuv )
email = lista_cuv[1]
comp = email.split ( '@' )
print(comp)
print ( 'Host:', comp[0] )
print ( 'Domeniu:', comp[1] )


# Enumerate

for e, l in enumerate(['ian','feb','mar','apr','may',
					   'iun','iul','aug','sep', 'oct','nov','dec']):
    print('{:2d}'.format(e), l)

for e, l in enumerate(['ian','feb','mar','apr','may',
					   'iun','iul','aug','sep', 'oct','nov','dec']):
    print('{:2d}'.format(e + 1), l)
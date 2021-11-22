# 303 Tuplu
# Tuplu
# PF - 27/05/2016

# Exemplu
a = 'Canta cucu\' ...'  		# variabila
x = (3, 'Acasa e soare', ('Si aici e soare', True, 7), False, a)  # tuplu
print ( x[1] )
print ( x[2][0][3:7] ) 				# un tuplu este indexabil
print ( x[1][6] )
x[0] = 5  						# incercam sa atribuim valoarea 5 primului element (imutabil)

for items in x:
    print ( items ) # for in tuplu


for items in x:
    print ( items )
    if type ( items ) is str:
        print ( items.split ( ' ' ) )
print ( len ( x ) )             # numara elementele tuplului
print ( type ( x ) )

# Comparare tupluri
a = (1, 3, 4)
b = (1, 3, 5)
c = (2, 1, 1)
a > b
b > a
c > b
('abc', 1, 2) > ('aaa', 777, 'ssst..')
('abc', 1, 2) > ('abc', 1, 'ssst..')

# Metode si functii aplicabile
dir ( x )
x.count ( 3 )                   # numara aparitiile unui element in tuplu
x.count ( 'Acasa e soare' )
x.index (False)                   # returneaza indexul unui element

len ( x )

# Stoc
stoc = None

if not stoc:
    print ( 'Stoc zero.' )

stoc = ('Tigla', 'Tabla', 'Sitza')

print ( 'Stocul cuprinde: ', stoc )

count = 0
for item in stoc:
    print ( 'Index:', count, '- Element:', item )
    count += 1

input ( 'Apasa <enter> pt a iesi.' )

# alta fatza a tuplurilor

a = 'ana', 'are', 'multe', 'mere'   # creare tuplu
print(a)

x, y, z, w =a   # 'spargerea' in variabile a uni tuplu

print(x,y,z,w)


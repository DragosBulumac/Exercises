# 301 Indexarea sirurilor
# Indexare
# PF - 27/05/2016


# Concatenare + indexare
cuv = 'Tele' + 'cinemateca'             # concatenare stringuri
print(cuv)
lit = cuv[4]
print(lit)
x = 7
y = cuv[x + 3]                          # index calculat cu o expresie
print(y)

# Bucla while intr-un sir - returneaza index - litera
index = 0                               # initializare variabila
while index < len(cuv):
    litera = cuv[index]                    # parsare
    print(index, '-', litera)
    index += 1                          # incrementare

# Bucla for intr-un sir - returneaza index - litera
index = 0
for i in cuv:
    # i = cuv[index]
    print(index, '-', i)
    index += 1

# Numararea aparitiilor unei litere
count = 0
for i in cuv:
    if i == 'e':
        count += 1
print(count)

# Numara vocalele si ponderea in total
voc = 0
tot = 0
for i in cuv:
    tot += 1
    if i in ('a', 'e', 'i', 'o', 'u'):
        voc += 1
print('Sunt', voc, 'vocale si', tot - voc, 'consoane.\
	Vocalele reprezinta: {0}'.format(voc / tot * 100), '%')

# Slicing
print(cuv[0:4])  # incepe de la primul caracter, termina la al doilea argument fara sa-l includa

print(cuv[4:8])  # incepe cu primul argument, termina la al doilea fara sa-l includa

print(cuv[4:20])  # daca al doilea numar e mai mare decat len(string) se opreste la sfarsitul stringului

print(cuv[:4])  # returneaza primele caractere fara sa includa argumentul final

print(cuv[12:])  # returneaza toate caracterele incepand cu argumentul dinaintea ':'

print(cuv[:])  # returneaza tot stringul

copy_cuv = cuv[:]  # facem o copie a stringului intr-o alta variabila

print(copy_cuv)

print(cuv is copy_cuv)

# Inversam ordinea literelor intr-un sir
sir = input('Introduceti un sir: ')
#iteratii = 0
sir_invers = ''
print('Sirul tau este', sir)
for var in sir:
    #iteratii += 1
    sir_invers = var + sir_invers
print(sir_invers)
print('Sirul tau se scrie invers: ', sir_invers)

input('Apasa <enter> pt a iesi.')




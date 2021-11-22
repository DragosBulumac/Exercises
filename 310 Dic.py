# 310 Dictionare
# Lucrul cu liste si dictionare
# PF - 27/05/2016

lista_filme = list ( )  				# lista contine dictionare cu filme. Un film, un dictionar
film1 = dict ( )

# 	populam dictionarul pentru film1
film1['Director'] = 'Alejandro G. Inarritu'
film1['Title'] = 'The Revenant'
film1['Release year'] = '2015'
film1['Running Time'] = '156 minutes'
film1['Rating'] = 'AG-15'
print(film1)

# populam lista cu datele din dictionar
lista_filme.append ( film1 )

film2 = dict ( )

# populam dictionarul pentru film2
film2['Director'] = 'Radu Jude'
film2['Title'] = 'Aferim!'
film2['Release Year'] = '2015'
film2['Running Time'] = '108 min'
film2['Rating'] = 'AG-12'

# populam lista cu datele din dictionar
lista_filme.append ( film2 )
print ( lista_filme )

# selectie elem convenabile din lista prin keys
keys = ['Title', 'Director']

for item in lista_filme:
	print ( "---------------------------" )
	for key in keys:
		print ( key, ': ', item[key] )
print ( "---------------------------" )

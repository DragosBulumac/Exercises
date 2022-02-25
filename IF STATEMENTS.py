'Sunt conditi pe care le pui '

is_male = True
is_tall = True
is_prost= False
is_tampit= True
if is_male or is_tall :
    print("you are a male or tall or both")

else:
    print("you are not a male or tall")


if is_male and is_tall :
    print("you are a tall male ")
elif is_male and not(is_tall):
    print("you are a short male")
elif is_male and not is_tall:
    print("you are a short male")
else:
    print("you are not a male or tall")

if is_prost and is_tampit:
    print("PROSTULE")
elif is_tampit and not (is_prost) :
    print("cretinule")
else:
    print("smekeritule")
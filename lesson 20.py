# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "bro Code!"

#eğer ilk öğe küçükse onu büyük harfe çeviriyor
#if(name[0].islower()):
#    name = name.capitalize()

first_name = name[:3].upper() #.upper hepsini büyük yazdırdı
last_name  = name[4:].lower() #.lower hepsini küçük yazdırdı
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
import  random

x = random.randint(1,6) #rastgele tam sayı üretir
y= random.random() #virgüllü random sayı üretir

myList=['rock','paper','scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards) #.shuffle karıştırır
print(cards)
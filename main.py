#----------------DERS 1-------------#
#print("mrhaba pizza")
#print("bu iyi")
#----------------DERS 2-----------------#
# variable = a container for a value.
#name = "Bro"

#print("name")
#print("Hello"+ name)
#print(type(name))

#first_name = "Bro"
#last_name = "code"
#full_name = first_name +" "+ last_name
#print("Hello "+ full_name)

#age = 21
#age = age + 1
#print(age)
#print(type(age))

#height =250.5
#print(height)
#print(type(height))
#print("your height is :"+str(height)+"cm")

human = True
#print(human)
#print(type(human))
#print("are you a human : "+str(human))

#Multiple assigment = allows us to assign multiple variables at the same time in one line of code
#name = "Bro"
#age = 21
#attractive = True

#name, age, attractive = "Bro", 21, True
#print(name)
#print(age)
#print(attractive)


#spongebob = 30
#patric = 30
#sandy = 30
#squidward = 30

#spongebob = patrick = sandy = squidward = 30

#print(spongebob)
#print(patrick)
#print(sandy)
#print(squidward)

#-------------------------Ders 4 --------------
#name = "Bro Code"

#print(len(name))  #uzunluğu veriyor
#print(name.find("r")) #hangi sırada olduğunu buluyor
#print(name.capitalize()) # ilk kelimeyi büyük harfle başlatıyor
#print(name.upper()) #hepsini büyük harf yapıyor
#print(name.lower()) #hepsini küçük harf yapıyor
#print(name.isdigit()) #dizide sayı bulunursa "TRUE" sadece harf varsa "FALSE" yazdırır
#print(name.isalpha()) # dizide içerisindeki tüm karakterler harf ise True basar değilse false basar
#print(name.count("o")) #içerisinde o karakterden kaç tane olduğunu sayar
#print(name.replace("o","a")) #dizde bulunan ilk verilen karakterlerin yerine ikinci verilen karakterleri yazar
#print(name*3) #çarıpım kadar name yi yazdırır
#**
#-----------------------DERS 5 -----------------------

#type casting = convert the data type of a value to another data type.

#x=1  #int
#y=2.0 # float
#z= "3" #str

#x= str(x)
#y= str(y)
#z= str(z)

#print(x)
#print(y)
#print(z*3)
#**
#------------------------Ders 6 -----------

#name = input("What is your name ?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#print("Hello "+name)
#print("you are "+str(age)+" years old")
#print("you are "+str(height)+"cm tall")

#**
#--------------------------Ders 7 -----------------
import math

#pi= 3.14

#x = 1
#y = 2
#z = 3

#round yuvarlar
#print(round(pi))

#print(math.ceil(pi))
#math.ceil en yakın yukardaki sayıya yuvarlar

#print(math.floor(pi))
#math.floor aşağı yuvarlar

#print(abs(pi))
#abs mutlak değere alır

#print(pow(pi,2))
#pow virgulden sonraki syı kadar kuvvet alır

#print(math.sqrt(pi))
#math.sqrt kare kök içine alır

#print(max(x,y,z))
# max en büyüğünü bulur

#print(min(x,y,z))
#min en küçüğünü bulur
#**

#------------------Ders 8 -----------------
#slicing = create a substring elements from another string
#          indexing[] or slice()
#           [start:stop:step]

#name ="Bro Code"

#first_name = name[:3]
#last_name  = name[4:]
#funky_name = name[0:8:2]
#reversed_name = name[::-1]

#print(reversed_name)

#website1= "http://google.com"
#website2= "http://wikipedia.com"
#slice = slice(7,-4)

#print(website1[slice])
#print(website2[slice])
#**

#--------------------Ders 9 ----------------------

#if statement = a block of code that will execute if it's condition is true

#age = (int(input("How old are you?: ")))

#if age == 100:
#    print("You are a centry old!")
#elif age >= 18:
#    print("Your are an adult!")
#elif age<0 :
 #   print("You haven't been born yet!")

#else:
 #   print("you are a child!")
#**

#-------------------------Ders 10 -----------

#Logical operators (and,or) = used to check if two or more condtional statements is true
#temp = int(input("What is the temperature outside?: "))

#if temp >=0 and temp <=30:
 #   print("the temperature is good today!")
  #  print("go outside!")

#elif temp <0 or temp >30:
 #   print("The temperature is bad today")
  #  print("stay inside")

#**
#---------------------Ders 11 ------------------

#while loop = a statement that will execute it'is block of code,
    #         as long as it's condition remains true
#name = ""

#while len(name) ==0 :
 #   name= input("Enter your name: ")

#print("Hello "+name)

#**
#------------------------Ders 12 ----------------
import time
# for loop = a statement that will execute it's block of code
#            a limited amount of times

#           while loop = unlimited
#            for loop  = limited
#
#for i in range(10):
 #   print(i+1)

#for i in range(50,100+1,2):
 # print(i)

 #for i in "Bro Code": !!!
    # print(i)         !!!

 #for seconds in range(10,0,-1):
#   print(seconds)
#   time.sleep(1) #Bekleme süresi
# print("Happy New Year !")

#**
#---------------------Ders 13 ------------

#Nested loops = The "inner loop" will finish all of it's iterations before
#               finishing one iteration of the "outer loop"


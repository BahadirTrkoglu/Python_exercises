#list = used to store  multiple items in a single variable

food= ["pizza","hamburger","hotdog","spaghetti","puding"]

food[0] = "sushi"


food.append("ice cream")    #.append öğe kelemede kullanılır
food.remove("hotdog")       #.remove öğeyi siler
food.pop()                  #son öğeyi siler
food.insert(0,"cake")  #belirttiğimiz indexe istediğimiz öğeyi ekler
food.sort()                 #alfabetik olarak sıralar
food.clear()                #listeyi temizler

for x in food:
    print(x)

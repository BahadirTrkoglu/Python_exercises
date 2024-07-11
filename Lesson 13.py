#Nested loops = The "inner loop" will finish all of it's iterations before
#               finishing one iteration of the "outer loop"

rows    = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol  = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()

#Eğer biz bir alt satıra geçmek yerine yine aynı satırda işlemlerimize devam etmek istersek ve ya alt satıra geçmek yerine satır sonundan belli karakterler (boşluk,/, ? , ! vb.) ile devam etmek istersek end parametresini kullanırız.
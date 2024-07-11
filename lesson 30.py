# exception =  events detected during execution the flow of a program

try:
    numerator   = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result      = numerator / denominator

except ZeroDivisionError as a:
    print(a)
    print("You can't divide by zero! idiot!")

except  ValueError as a:
    print(a)
    print("Enter only number plz")

except Exception as a:
    print(a)
    print("something went wrong : ")

else:
    print(result)
finally:
    print("This will always execute")



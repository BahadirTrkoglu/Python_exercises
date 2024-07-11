# *args = parameter that will pack all arguments into a tuple
#         useful so tahat a functioncan accept a varying amount of arguments


def add(*args):
    sum= 0
    args = list(args) #not necessary
    args[0] = 0       # "     " 
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6 ))
#scope = The region tahat a variable is recognized
#        A variable is only avaible from  inside the region it is created.
#        A global and locally scoped versions of a variable can be created

name = "Bro" #Global scope (avaible inside & outside functions)

def display_name():
    name = "Code"  #local scope (available only inside this function)
    print(name)

display_name()
print(name)
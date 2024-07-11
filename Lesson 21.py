# function = a block of code which is executed only when it is called.

def hello (name):
    print("hello" + name)
    print("Have a nice day!")

hello(" Bro")
hello(" Dude")

my_name = " Bro"
hello(my_name)

def hello (firs_name,last_name,age):
    print("hello" + firs_name+ " " +last_name)
    print("You are "+str(age) + "years old")
    print("Have a nice day!")

hello("Bro","Code",21)
#Read a file

try:
    with open('C:\\Users\\AsusRogStrix\\Desktop\\test.tt') as file:
          print(file.read())
except FileNotFoundError:
    print("That file was not found :(( ")

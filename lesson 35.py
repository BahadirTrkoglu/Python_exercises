#move a file

import os

source = "test1.txt"
destination = "C:\\Users\\AsusRogStrix\\Desktop\\test1.txt"

try:
    if os.path.exists(destination):
        print("There is a alreeady a file there")
    else:
        os.replace(source,destination)
        print(source+ " was moved")

except FileNotFoundError:
    print(source+ "was not found")

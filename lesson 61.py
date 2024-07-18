#zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets,etc.)
#                  creates a zip object with paird elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword","abc123","guest")

users = dict(zip(usernames,passwords))

print(type(users))

for i in users:
    print(i)

for key,value in users.items():
    print(key+ " : "+value)

print("      ")
#------------------------------------------------------------
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users_1 = zip(usernames,passwords,login_date)

for i in users_1:
    print(i)
#list comprehension = a way to create a new list with syntax
#                     can mimic certain lambda function, easier to read
#                     list = [expression for item in iterable](1)
#                     list = [expression for item in iterable if conditional](2)
#                     list = [expression if/else for item in iterable](3)
#-----------------------------------------------------------------
#(1)
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

squares = [i *i for i in range(1,11)] #list comprehension
print(squares)
#-------------------------------------------------------------------
#(2)
students = [100,90,80,70,60,50,40,30,0]

#passed_student = list(filter(lambda x:x >= 60,students))

passed_student = [ i for i in students if i >= 60] #list comprehension

print(passed_student)


#--------------------------------------------------------------------
#(3)

passed_student_3= [i if i >= 60 else "Failed" for i in students]

print(passed_student_3)
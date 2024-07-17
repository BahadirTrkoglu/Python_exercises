# sort() method   = used with list
# sort() function = used with iterables
#------------------------------------------------------------------
#students = ("Squidward","Sandy","Patric","Spongebob","Mr.Krabs")

#students.sort(reverse = True) [] için
#sorted_students = sorted(students,reverse = True)

#for i in sorted_students:
#    print(i)

#-----------------------------------------------------------------

students = [("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","B",20),
            ("Mr.Krabs","C",78)]
grade = lambda grades: grades[1]
students.sort(key=grade)

for i in students:
    print(i)
# set = collection which is unordered , unindexed. no duplicate values

utensils = {"fork","spoon","knife"}
dishes   = {"bowl","plate","cup","knife"}

#utensils.add("napkin")    #kümeye öğe ekler
#utensils.remove("fork")   #kümeden öğe siler
#utensils.clear()          #hepsini siler
#utensils.update(dishes)    #iki kümeyi birleştirir
#dinner_table = utensils.union(dishes) #başka bir küme için iki kümeyi birleiştirdi

print(utensils.difference(dishes)) # ilk yazılandakilerden hangileri ikinci kümede yoksa onu yazdırır
print(utensils.intersection(dishes))  #ortak olanı bulur

#for x in dinner_table:
 #   print(x)
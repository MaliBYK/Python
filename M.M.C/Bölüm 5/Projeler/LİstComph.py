#uzun yol
list1 =[1,2,3,4]
list2 = list()
for i in list1:
    list2.append(i)
#kolay yol
list3 = [i for i in list1]
print(list3)
#uzun yol
list4 = [i*2 for i in list3]
print(list4)
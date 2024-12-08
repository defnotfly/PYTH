for x in range (3):
    for x in range (1, 10):
        print(x, end = " ")
    print()

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,4,6,8,10}
set3 = {1,3,5,7,9}

print(set2 | set3) #12345678910
#print(set2.add(1)) #none, u cant print while adding an element
#set2.add(1) #1246810
print(set2 - set1)
print(set1 - set2)
print(set2 & set3) #set() no intersection

print(set2.issubset(set1)) #TRUE
print(set1.issuperset(set3)) #TRUE

print(set2 ^ set3) #appeared not on both
print(set2 - set3)
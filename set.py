set1 = [2,4,10,8,2,6,8,10] #list (pwede mag duplicate ang elements)
set2 = {1,3,5,7,9} #set1
set3 = {1,2,3,4,5,6,7,8,9,10} #set2
new_set1 = set (set1) #list to set (mawawala mga duplicate)

print(set1)
print(set2)
print(set3)
print(new_set1)

print (new_set1 | set2) #union
print (new_set1 & set2) #intersection
print (new_set1 & set3) #intersection
print (set3 - set2)
print (set3 - (set2 & new_set1))
print (set2 & (set3 - new_set1))

print (10 in set2) #False
print (1 in set3) #True


print(set2.issubset(set1)) #true, kasi andon ung elements ni set1 sa set3
print(set3.issuperset(set2)) #t


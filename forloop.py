"""
num = {1,2,3,4,5,6,7,8,9,10}
for x in num:
    print("Numbers:" , x, end = " ")


"""
"""
for x in range (1, 6): #for(start,stop,condition/step{x+1})
    for y in range (1, x+1):
        print ("*", end = " ")
    print()
"""



rows = 5 #-1 = 4

for x in range (rows,0, -1):
    for y in range (1 , x+1): #x=4 =5
        print ("*", end = " ")
    print()



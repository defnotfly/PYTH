capitals = {"USA" : "Washington D.C",
            "India" : "New Delhi",
            "China" : "Beijing" ,
            "Philippines" : "Manila" ,
            "Canada" : "Ontario"}

#print (dir(capitals))
#print (help(capitals))
"""""
word = input("Enter a country: ")
if capitals.get(word):
    print("That capital exist")
    print(capitals.get(word))
else:
    print("That capital doesn't exist")
    print(capitals.get(word)) """""

#capitals.update({"Germany" : "Berlin"})
#capitals.update({"USA" : "Detroit"})
#capitals.pop("Beijing")
#capitals.popitem()
#capitals.clear()

capitals["USA"] = "tite"
capitals["tangina"] = "bobo ka"
test = "tite"
if test in capitals.values():
    print("yes") #kailangan ng values....

del capitals["bobo ka"]
print(capitals)
#keys = capitals.keys()
#value = capitals.values()

#for x in capitals.keys():
    #print(x)
#for x in value:
    #print(x)
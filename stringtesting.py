x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))


choice = input("Bobo ba si Franz? (yes/no) ").strip().lower() == "yes"


if (choice):
    if (x > y):
        print ("TANGINA MO MAS MALAKI YUNG X GAGO!")
    else:
        print ("TANGINA MO MAS MALAKI YUNG Y GAGO!")
else:
    print ("BOBO KA PARIN POTANGINA MO")

str_ey = ["Franz" , "Tanga" , "Bobo" , "Horny" , "Adik"]
str = "Franz bobo tlga sa lahat hahal"
len_str = len(str)
rep_str = str.replace("bobo", "tanga")
str_strip = str.strip()
str_join = " na ".join(str_ey)
str_join2 = "legit toh na ".join(str)
str_find = str.find("a")
str_rfind = str.rfind("a")
str_swith = str.startswith("F")
str_ewith = str.endswith("l")
str_index = str.index("a")
str_rindex = str.rindex("a")

print(len_str)

print(rep_str)

print(str_strip)

print(str_join)

print(str_join2)

print(str_find)

print(str_rfind)

print(str_swith)

print(str_ewith)

print(str_index)

print(str_rindex)






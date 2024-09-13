#Name
name1 = input("What is your Name First person: ")
name2 = input("What is your Name Second person: ")
name3 = input("What is your Name Third person: ")
#Order
order1 = input(f"What kind of ice cream would you like,{name1}? ")
order2 = input(f"What kind of ice cream would you like,{name2}? ")
order3 = input(f"What kind of ice cream would you like,{name3}? ")
#Conditions
print("chocolate = 3 $ strawberry = 2 $ blackberry= 3 $ hazelnut=4 $ vanilla= 2 $ saffron=3 $")
if order1 == "chocolate" and order2 =="strawberry" and order3 =="blackberry":
    print ("Your ice cream will cost 8 $")
elif order1 == "chocolate" and order2 =="blackberry" and order3 =="strawberry":
    print ("Your ice cream will cost 8 $")
elif order1 == "chocolate" and order2 =="chocolate" and order3 =="chocolate":
    print ("Your ice cream will cost 9 $")
elif order1 == "chocolate" and order2 =="chocolate" and order3 =="chocolate":
    print ("Your ice cream will cost 9 $")
elif order1 == "hazelnut" and order2 =="hazelnut" and order3 =="hazelnut":
    print ("Your ice cream will cost 12 $")
elif order1 == "vanilla" and order2 =="vanilla" and order3 =="vanilla":
    print ("Your ice cream will cost 6 $")
elif order1 == "saffron" and order2 =="saffron" and order3 =="saffron":
    print ("Your ice cream will cost 9 $")
elif order1 == "strawberry" and order2 =="strawberry" and order3 =="strawberry":
    print ("Your ice cream will cost 6 $")
elif order1 == "blackberry" and order2 =="blackberry" and order3 =="blackberry":
    print ("Your ice cream will cost 9 $")
elif order1 == "blackberry" and order2 =="hazelnut" and order3 =="vanilla":
    print ("Your ice cream will cost 9 $")
elif order1 == "chocolate" and order2 =="vanilla" and order3 =="strawberry":
    print ("Your ice cream will cost 7 $")
else:
    print("Unfortunately, we do not have this kind of ice cream!!!!")    
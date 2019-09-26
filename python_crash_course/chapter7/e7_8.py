#7-8
print("#7-8")
sandwich_orders = ["sandwichA","sandwichB","sandwichC",
"pastrami","pastrami","pastrami","pastrami"]
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
print(sandwich_orders)
print(finished_sandwiches)

#7-9
print("#7-9")
sandwich_orders = ["sandwichA","sandwichB","sandwichC",
"pastrami","pastrami","pastrami","pastrami"]
print("pastrami sold out!!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)


#7-10
print("#7-10")
quit = False
mylist = []
while quit == False:
    name = input("你叫啥")
    city = input("想去哪里")
    mylist.append({name:city})
    answer = input("quit吗y/n")
    quit = (answer == "y")
#    if answer == "y"
#        quit = True
#    else:
#        quit = False
print(mylist)



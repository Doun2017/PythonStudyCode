#4-10
print("#4-10")
million = list(range(1, 1000001))
print("The first three items in the list are:")
print(million[:3])
print("Three items from the middle of the list are:")
print(million[499999:500002])
print("The last three items in the list are:")
print(million[-3:])

#4-11
print("#4-11")
names = ["boluo pisa", "niurou pisa", "haixian pisa", "liulian pisa"]
friend_pizzas = names[:]
names.append("sort posa")
friend_pizzas.append("long posa")
print(names)
print(friend_pizzas)

#4-12
print("#4-12")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)


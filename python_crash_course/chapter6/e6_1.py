#6-1
print("#6-1")
people = {"first_name": "shi",
"last_name": "liu",
"age": 21,
"city ": "shanghai",}
print(people)
#for key, value in people.items():
#    print("\nKey: " + key)
#    print("Value: " + value)

#6-3
print("#6-3")
biao = {"key":"键", "value":"值"}
print("key:" + biao["key"])
print("value:" + biao["value"])

#6-4
print("#6-4")
for key,value in biao.items():
    print(key + ":" + value)


#6-6
print("#6-6")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
names = ["jen", "edward", "haixian pisa", "liulian pisa"]

for name in names:
    if name in favorite_languages.keys():
        print(name+" has voted, Thank you!")
    else:
        print("Invite "+name+" to vote!")


#6-7
print("#6-7")
people1 = {"first_name": "yan",
"last_name": "ren",
"age": 16,
"city ": "shanghai",}
people2 = {"first_name": "hang",
"last_name": "shu",
"age": 15,
"city ": "shanghai",}
persons = []
persons.append(people)
persons.append(people1)
persons.append(people2)
for item in persons:
    print(item)


#6-8
print("#6-8")
pet_dog = {"type": "dog",
"master": "liushi",}
pet_cat = {"type": "cat",
"master": "renyan",}
pet_pig = {"type": "pig",
"master": "shuhang",}
pets = []
pets.append(pet_dog)
pets.append(pet_cat)
pets.append(pet_pig)
for item in pets:
    print(item)


#6-9
print("#6-9")
favorite_places = {"liushi":["shanghai", "beijing", "guangzhou"],
"renyan":["shanghai", "beijing", "guangzhou"],
"xialijie":["shanghai", "beijing", "guangzhou"],
}
print(favorite_places)

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




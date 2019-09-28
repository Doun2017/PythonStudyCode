#8-9
def show_magicians(names):
    print(names)
#8-10
def make_great(names):
#    for item in names:
#        item = "The Great " + item
    for index in range(len(names)):
        names[index] = "The Great " +names[index]
    
#8-11
def make_great11(names):
#    for item in names:
#        item = "The Great " + item
    for index in range(len(names)):
        names[index] = "The Great " +names[index]
    return names


print("#8-9")
names = ("boluo pisa", "niurou pisa", "haixian pisa", "liulian pisa",'pizza', 'falafel', 'carrot cake')
show_magicians(names)

print("#8-10")
names1 = ["boluo pisa", "niurou pisa", "haixian pisa", "liulian pisa",'pizza', 'falafel', 'carrot cake']
make_great(names1)
show_magicians(names1)


print("#8-11")
names11 = ["boluo pisa", "niurou pisa", "haixian pisa", "liulian pisa",'pizza', 'falafel', 'carrot cake']
show_magicians(make_great11(names11[:]))
show_magicians(names11)



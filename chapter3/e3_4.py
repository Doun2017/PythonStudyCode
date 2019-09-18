#3-4
names = ["ren yan", "xia li jie", "shu hang", "zhang hui ru"]
print("nameList:" + str(names))
#3-5
print(names[1] + " can't come!")
names[1] = "a gan"
print("nameList:" + str(names))
#3-6
print("I found a bigger table!")
names.insert(0, "yang li chao")
names.insert(3, "zhang shaung qing")
names.append("zhu jun")
print("nameList:" + str(names))
#3-7
print("I can only invite two person!")
print("sorry, I can not invite " + names.pop() + " to denner!")
print("sorry, I can not invite " + names.pop() + " to denner!")
print("sorry, I can not invite " + names.pop() + " to denner!")
print("sorry, I can not invite " + names.pop() + " to denner!")
print("sorry, I can not invite " + names.pop() + " to denner!")
print("nameList:" + str(names))
del names[0]
del names[0]
print("nameList:" + str(names))
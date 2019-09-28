#8-3
def make_shirt(size, text):
	print("Size="+size+"\tText="+text)
#8-4
def make_shirt1(size, text="“I love Python”"):
	print("Size="+size+"\tText="+text)
#8-5
def describe_city(city, country="China"):
	print(city+" is in "+country)

print("#8-3")
make_shirt("L", "I'm OK")
make_shirt(size="M", text="I'm OK!")
print("#8-4")
make_shirt1("L")
make_shirt1("M")
make_shirt1("M", "fjdsaogheoaw")
print("#8-4")
describe_city("Qingdao")
describe_city("Beijing")
describe_city("Reykjavik","Iceland")
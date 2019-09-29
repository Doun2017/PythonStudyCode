#10-3
print("#10-3")
name = input("input your name:")
filename = 'guest.txt'
with open(filename,"w") as file_object:
	file_object.write(name)
	

#10-4
print("#10-4")
filename = 'guest_book.txt'
with open(filename, "a") as file_object:
	while True:
		name = input("input your name," +
		"\ninput q to quit:")
		if name == "q":
			break
		file_object.write(name + "\n")
		print("hello, " + name + "!\n")




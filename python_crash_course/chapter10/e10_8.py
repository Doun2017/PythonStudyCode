#10-8
print("#10-8")
filename = "cats.txt"
try:
	with open(filename) as cat_file:
		for line in cat_file:
			print(line.rstrip())
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	print("print over!")

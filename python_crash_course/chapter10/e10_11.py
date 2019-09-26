import json


def input_number():
	while True:
		number1 = input("input a number('q' to quit):")
		if number1 == "q":
			return number1
		else:
			try:
				n1 = int(number1)
			except ValueError:
				print("你刚才输入的不是数字吧？")
				continue
			else:
				return n1


#10-11
print("#10-11")
filename = "faverate_number.txt"
num = input_number()
if num and num != "q":
	with open(filename, "w") as json_file:
		json.dump(num, json_file)

try:
	with open(filename) as jsonfile:
		num1 = json.load(jsonfile)
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	print("I know your favorite number! It's _____." 
	+ str(num1))








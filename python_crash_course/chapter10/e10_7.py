#10-7
print("#10-7")
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

while True:
	number1 = input_number()
	if number1 == "q":
		break
	number2 = input_number()
	if number2 == "q":
		break
	sum = number1 + number2
	print("sum = " + str(sum) + "\n")

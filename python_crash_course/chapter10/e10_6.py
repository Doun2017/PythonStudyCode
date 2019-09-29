#10-6
print("#10-6")
number1 = input("input a number:")
number2 = input("input another number:")

try:
	number = number1+number2
	print(number)
	n1 = int(number1)
	n2 = int(number2)
except ValueError:
	print("你刚才输入的不是数字吧？")
else:
	print("sum = " + str(n1+n2))



#7-3
print("#7-3")
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " is 10 的整数倍.")
else:
    print("\nThe number " + str(number) + " is not 10 的整数倍.")

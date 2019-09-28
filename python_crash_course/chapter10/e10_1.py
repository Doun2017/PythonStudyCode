#filename = 'pi_million_digits.txt'
#with open(filename) as file_object:
#	lines = file_object.readlines()
#pi_string = ''
#for line in lines:
#	pi_string += line.rstrip()	
#	
#birthday = input("Enter your birthday, in the form mmddyy: ")
#if birthday in pi_string:
#	print("Your birthday appears in the first million digits of pi!")
#else:
#	print("Your birthday does not appear in the first million digits of pi.")
	
#10-1
print("#10-1")
filename = 'learning_python.txt'
print("第一次读取")
with open(filename) as file_object:
	data = file_object.read()
	print(data)
print("第二次读取")
with open(filename) as file_object0:
	for line in file_object0:
		print(line.rstrip())
print("第三次读取")
with open(filename) as file_object1:
	lines = file_object1.readlines()
for line in lines:
	print(line.rstrip())

#10-2
print("#10-2")
for line in lines:
	print(line.rstrip().replace("Python","C"))





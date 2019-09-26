#10-10
print("#10-10")

def count_words(filename):
	""" 计算一个文件大致包含多少个单词 """
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# 计算文件大致包含多少个单词
		num_words = contents.lower().count("the")
		print("The file " + filename + " has about " + str(num_words) +
		" 'the' words.")
filename = 'alice.txt'
count_words(filename)
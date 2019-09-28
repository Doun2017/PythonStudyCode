from random import randint

		
class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print("result=" + str(randint(1, self.sides)))


def test(sides):
	print(str(sides) + "面筛子：")
	die = Die(sides)
	for i in range(10):
		die.roll_die()

test(6)
test(10)
test(20)

#print("6面筛子：")
#die6 = Die()
#for i in range(10):
#	die6.roll_die()
#print("10面筛子：")
#die10 = Die(10)
#for i in range(10):
#	die10.roll_die()
#print("20面筛子：")
#die20 = Die(20)
#for i in range(10):
#	die20.roll_die()

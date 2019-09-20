#9-1
class Restaurant():
	def __init__(self,restaurant_name, cuisine_type):
		"""初始化"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("restaurant_name: " + self.restaurant_name + 
		"\t\tcuisine_type: " + self.cuisine_type+ 
		"\t\tnumber_served: " + str(self.number_served))

	def open_restaurant(self):
		print(self.restaurant_name + "OPEN ")

	def set_number_served(self, num):
		self.number_served = num

	def increment_number_served(self):
		self.number_served += 100
		


print("#9-1")
my_restaurant = Restaurant("云之馆", "chinese food")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print("#9-2")
my_restaurant1 = Restaurant("小杨生煎", "包子")
my_restaurant2 = Restaurant("老鸿兴", "chinese food")
my_restaurant.describe_restaurant()
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()

print("#9-4")
my_restaurant.number_served = 1993
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(2345)
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served()
my_restaurant.describe_restaurant()






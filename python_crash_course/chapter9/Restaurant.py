
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







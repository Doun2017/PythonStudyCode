import unittest

def citys(city, country, population=''):
	if population:
		return city.title() + ", " + country.title() + ", " + str(population)
	else:
		return city.title() + ", " + country.title()


class CitysTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_name = citys("beijing", "china")
		self.assertEqual(formatted_name, 'Beijing, China')

	def test_city_country_population(self):
		formatted_name = citys("beijing", "china", population=5000000)
		self.assertEqual(formatted_name, 'Beijing, China, 5000000')

unittest.main()



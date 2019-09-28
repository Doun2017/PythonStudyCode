#7-6
print("#7-6")
prompt = "\nPlease enter the name of a 调料 you want:"
prompt += "\n(Enter 'quit' when you are finished.) "
city = input(prompt)

while city != 'quit':
    print("I'd love to add " + city.title() + " to your pisa!")
    city = input(prompt)


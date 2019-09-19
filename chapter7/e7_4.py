#7-4
print("#7-4")
prompt = "\nPlease enter the name of a 调料 you want:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to add " + city.title() + " to your pisa!")


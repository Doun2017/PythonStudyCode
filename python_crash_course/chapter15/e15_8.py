from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 3 D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
range_num = 10000
for roll_num in range(range_num):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    num = 0
    for x in range(1, die_1.num_sides+1):
        for y in range(1, die_2.num_sides+1):
            for z in range(1, die_3.num_sides+1):
                if x+y+z == value:
                    print("sum"+str(value)+": " + str(x)+"  "+str(y)+"  "+str(z)+" ")
                    num+=1
    print("sum"+str(value)+"num=" + str(num))

# Visualize the results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice ' + str(range_num) + ' times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
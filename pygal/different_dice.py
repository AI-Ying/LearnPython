import pygal

from die import Die

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequences = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequences.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist._title = "Results of rolling a D6 and a D10 50,000 times."
hist.xlabels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
    '13', '14', '15', '16']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6+D10", frequences)
hist.render_to_file('different_dice.svg')
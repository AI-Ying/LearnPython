import csv

from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # 打印文件头
    # print(header_row)

    # 打印文件头即第一行
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    
    # 打印第二列
    # hights = []
    # for row in reader:
    #     hights.append(row[1])
    # print(hights)

    # 从文件中读取日期、最高气温和最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
    print(highs)

# 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=14)
plt.xlabel('', fontsize=16)
# fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()








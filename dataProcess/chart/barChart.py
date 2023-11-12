import pandas as pd
import matplotlib.pyplot as plt

# 从第一个CSV文件中读取数据
data1 = pd.read_csv('../../imuRecord/10-14/行驶时记录数据2023-10-14 16:39:02.csv')

# 从第二个CSV文件中读取数据
data2 = pd.read_csv('../../imuRecord/10-14/行驶时记录数据2023-10-14 16:40:47.csv')

# 输入速度的阈值
speed_threshold = 2

# 筛选速度大于阈值的数据并分组
grouped_data1 = data1[data1['v'] > speed_threshold].groupby((data1['v'] // 0.1) * 0.1).size()
grouped_data2 = data2[data2['v'] > speed_threshold].groupby((data2['v'] // 0.1) * 0.1).size()

# 绘制第一个柱状图
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(grouped_data1.index, grouped_data1.values, width=0.08)
plt.xlabel('speed')
plt.ylabel('data')
plt.title('Speed Profile - File 1')
for index, value in zip(grouped_data1.index, grouped_data1.values):
    plt.text(index, value, str(value), ha='center', va='bottom')

# 绘制第二个柱状图
plt.subplot(1, 2, 2)
plt.bar(grouped_data2.index, grouped_data2.values, width=0.08)
plt.xlabel('speed')
plt.ylabel('data')
plt.title('Speed Profile - File 2')
for index, value in zip(grouped_data2.index, grouped_data2.values):
    plt.text(index, value, str(value), ha='center', va='bottom')

# 显示图形
plt.tight_layout()
plt.show()

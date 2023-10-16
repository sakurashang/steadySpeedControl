import pandas as pd
import matplotlib.pyplot as plt

# 从第一个CSV文件中读取数据
data1 = pd.read_csv('../imuRecord/10-14/行驶时记录数据2023-10-14 17:37:13.csv')

# 从第二个CSV文件中读取数据
data2 = pd.read_csv('../imuRecord/10-14/行驶时记录数据2023-10-14 17:42:54.csv')

# 输入速度的阈值
speed_threshold = 6.5

# 筛选速度大于阈值的数据
filtered_data1 = data1[data1['v'] > speed_threshold]
filtered_data2 = data2[data2['v'] > speed_threshold]

# 按照0.1为间隔划分数据
grouped_data1 = filtered_data1.groupby((filtered_data1['v'] // 0.1) * 0.1).size()
grouped_data2 = filtered_data2.groupby((filtered_data2['v'] // 0.1) * 0.1).size()

# 绘制饼状图
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.pie(grouped_data1.values, labels=[f'{val:.1f}' for val in grouped_data1.index], autopct='%.1f%%')
plt.title('Data 1')

plt.subplot(1, 2, 2)
plt.pie(grouped_data2.values, labels=[f'{val:.1f}' for val in grouped_data2.index], autopct='%.1f%%')
plt.title('Data 2')

plt.tight_layout()
plt.show()

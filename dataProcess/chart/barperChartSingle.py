import pandas as pd
import matplotlib.pyplot as plt

# 从第一个CSV文件中读取数据，跳过前120行
data1 = pd.read_csv('../../imuRecord/10-19/田地——速度5直线掉头.csv', skiprows=range(1, 200))



# 计算总行数
total_data1 = len(data1)


# 每0.1一段，对数据分组
grouped_data1 = data1.groupby((data1['v'] // 0.1) * 0.1).size() / total_data1 * 100


# 绘制第一个柱状图
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(grouped_data1.index, grouped_data1.values, width=0.08)
plt.xlabel('Speed')
plt.ylabel('Percentage of Total Data')
plt.title('Speed Profile - File 1')

# 在柱子上方显示数值标签
for index, value in zip(grouped_data1.index, grouped_data1.values):
    plt.text(index, value + 1, f'{value:.1f}', ha='center')



# 显示图形
plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np


file_path = '../imuRecord/10-16/果园—下坡4.csv'  # 请替换为实际的CSV文件路径
df = pd.read_csv(file_path)

# 提取速度数据列
speed_data = df['v']  # 请替换为实际的速度数据列名

# 计算均值、方差、标准差和均方根误差
mean_speed = np.mean(speed_data)
variance_speed = np.var(speed_data)
std_dev_speed = np.std(speed_data)
target_speed = 4  # 请替换为实际的目标速度
rmse = np.sqrt(np.mean((speed_data - target_speed) ** 2))

# 将计算结果覆盖到原CSV文件的新列
df['均值'] = mean_speed
df['方差'] = variance_speed
df['标准差'] = std_dev_speed
df['均方根误差'] = rmse

# 保存带有新列的CSV文件（覆盖原文件）
df.to_csv(file_path, index=False, encoding='utf-8-sig')

print("统计数据已添加到原文件。")

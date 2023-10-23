import pandas as pd
import math

# 读取CSV文件
data = pd.read_csv('../imuRecord/10-16/果园—上坡4.csv')

# 剔除前10秒（前67行数据）和 'v' 不为零的数据之前的零
non_zero_indices = data[data['v'] != 0].index
print(non_zero_indices)
if len(non_zero_indices) > 0:
    start_index = non_zero_indices[0]
    data = data.iloc[start_index:]

# 初始化空的DataFrame用于存储计算结果
result_data = pd.DataFrame(columns=['坡度', '速度指令', '实际速度'])

print(data['v'].mean() / 3.6 )

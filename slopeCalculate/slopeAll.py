import pandas as pd
import math

# 读取CSV文件
data = pd.read_csv('../imuRecord/10-14/行驶时记录数据2023-10-14 17:42:54.csv')

# 自行选择数据的起始和结束位置（示例中选择前1000条数据）
start_index =  2022 # 设置起始位置的索引
end_index = 2200  # 设置结束位置的索引（不包含该索引对应的数据）

# 提取起始和结束位置的GPSTime值，以秒为单位
start_time = data['GPSTime'].iloc[start_index]
end_time = data['GPSTime'].iloc[end_index - 1]

# 计算斜坡长度（假设速度乘以时间差得到横向位移）
slpe_displacement = data['v'].iloc[start_index:end_index].mean() * (end_time - start_time)

# 计算纵向位移（结束位置的高度减去起始位置的高度）
longitudinal_displacement = data['imu_altitude'].iloc[end_index - 1] - data['imu_altitude'].iloc[start_index]

# 计算横向位移
lateral_displacement = math.sqrt(slpe_displacement ** 2 - longitudinal_displacement ** 2)

# 求坡度
a = math.atan2(longitudinal_displacement, lateral_displacement)
total_slope = a * 180 / math.pi  # 弧度转角度

print("总坡度：", total_slope)

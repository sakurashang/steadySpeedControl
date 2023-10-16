import pandas as pd
import math

# 读取CSV文件
data = pd.read_csv('../imuRecord/10-14/行驶时记录数据2023-10-14 16:50:09.csv')

# 剔除前10秒（前100行数据）和 'v' 不为零的数据之前的零
non_zero_indices = data[data['v'] != 0].index
print(non_zero_indices)
if len(non_zero_indices) > 0:
    start_index = non_zero_indices[0]
    data = data.iloc[start_index:]

# 初始化空的DataFrame用于存储计算结果
result_data = pd.DataFrame(columns=['坡度', '速度指令', '实际速度'])

# 计算坡度和平均速度指令，并存储到新的DataFrame中
for i in range(0, len(data), 10):
    if i + 10 <= len(data):
        subset = data.iloc[i:i + 10]
        # 计算斜坡长度（假设速度乘以1秒得到横向位移）
        slpe_displacement = subset['v'].mean() * 1
        # 计算纵向位移（第十条数据的高度减去第一条数据的高度）
        longitudinal_displacement = subset['imu_altitude'].iloc[-1] - subset['imu_altitude'].iloc[0]
        # 计算横向位移
        lateral_displacement = math.sqrt(slpe_displacement ** 2 - longitudinal_displacement ** 2)
        # 求坡度
        a = math.atan2(longitudinal_displacement, lateral_displacement)
        slope = a * 180 / math.pi  # 弧度转角度
        # 取第五条数据的速度指令
        command_speed = subset['cmd_v'].iloc[4]
        # 计算十条数据中的实际速度平均值
        actual_speed = subset['v'].mean()
        # 将计算结果加入新的DataFrame
        result_data = result_data.append({'坡度': slope, '速度指令': command_speed, '实际速度': actual_speed}, ignore_index=True)

# 导出到CSV文件
result_data.to_csv('../imuRecord/slopeData/行驶时记录数据2023-10-14 16:50:09_10.csv', index=False)

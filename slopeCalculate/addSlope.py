import pandas as pd
import math

# 读取CSV文件
data = pd.read_csv('../imuRecord/10-16/果园—上坡4.csv')


# 定义一个函数来计算两点之间的距离（使用经纬度信息）
def calculate_distance(lat1, lon1, lat2, lon2):
    # 将经纬度转换为弧度
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # 地球半径（单位：公里）
    R = 6371.0

    # 计算差值
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # 使用Haversine公式计算两点间的距离
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance


# 定义一个函数来计算地理坡度
def calculate_slope(data, current_index, num_points=5):
    # 获取当前点的经纬度和高度
    current_lat = data['imu_lat'][current_index]
    current_lon = data['imu_lon'][current_index]
    current_height = data['imu_altitude'][current_index]

    # 计算当前点和后续若干点的距离和高度差
    total_distance = 0
    total_height_diff = 0
    for i in range(current_index + 1, current_index + num_points):
        if i < len(data):
            next_lat = data['imu_lat'][i]
            next_lon = data['imu_lon'][i]
            next_height = data['imu_altitude'][i]

            # 计算两点之间的距离
            distance = calculate_distance(current_lat, current_lon, next_lat, next_lon)

            # 计算高度差
            height_diff = next_height - current_height

            # 更新总距离和总高度差
            total_distance += distance
            total_height_diff += height_diff

    # 计算地理坡度
    total_distance = total_distance * 1000
    slope = total_height_diff / total_distance

    return slope


# 计算坡度并将结果添加到CSV文件中
for i in range(len(data) - 3):
    slope = calculate_slope(data, i, num_points=4)
    # 将坡度值添加到'坡度'列中
    data.at[i, '坡度'] = slope

# 将带有坡度值的DataFrame保存为新的CSV文件
data.to_csv('output_with_slope.csv', index=False)

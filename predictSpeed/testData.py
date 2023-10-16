import pandas as pd
import random
from decimal import Decimal

# 生成10000条测试数据
num_samples = 10000


# 生成符合逻辑条件的随机数据
def generate_data(num_samples):
    data = []
    for _ in range(num_samples):
        # 生成随机的坡度，精确到小数点后两位，范围在-30.00到30.00
        slope = round(random.uniform(-30.00, 30.00), 2)

        # 生成随机的速度指令，精确到小数点后三位，范围在0.000到15.000
        command_speed = round(random.uniform(0.000, 15.000), 3)

        # 根据坡度和速度指令生成实际速度
        if slope > 0:
            # 当坡度为正时，实际速度略小于速度指令，差别随坡度增加而增大
            max_difference = slope * 0.06  # 最大差别随坡度增加而增大
            actual_speed = round(random.uniform(command_speed - max_difference, command_speed), 3)
        elif slope < 0:
            # 当坡度为负时，实际速度略大于速度指令，差别随坡度绝对值增加而增大
            max_difference = abs(slope) * 0.06  # 最大差别随坡度绝对值增加而增大
            actual_speed = round(random.uniform(command_speed, command_speed + max_difference), 3)
        else:
            # 当坡度为零时，实际速度和速度指令基本相等，差别在0.05以下
            actual_speed = round(random.uniform(command_speed - 0.05, command_speed + 0.05), 3)

        # 将坡度、速度指令和实际速度添加到数据中
        data.append([slope, command_speed, actual_speed])
    return data


# 生成数据
data = generate_data(num_samples)

# 创建DataFrame
df = pd.DataFrame(data, columns=['坡度', '速度指令', '实际速度'])

# 保存数据到CSV文件
df.to_csv('test_data.csv', index=False)

print("已生成测试数据并保存到test_data.csv文件中。")

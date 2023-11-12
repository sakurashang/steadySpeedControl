import os
import pandas as pd

# 指定包含CSV文件的文件夹路径
folder_path = '../your_folder_path'  # 请替换为实际的文件夹路径

# 获取文件夹中所有的CSV文件
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# 定义每隔多少个数据点计算一次平均值
window_size = 5

# 遍历每个CSV文件，进行数据处理并保存到新的CSV文件中
for file in csv_files:
    file_path = os.path.join(folder_path, file)

    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 指定要删除的行数范围
    start_row = 2
    end_row = 150

    # 删除指定行数的数据
    df = df.drop(df.index[start_row - 2:end_row - 1])

    # 计算平均值并保存到新的DataFrame中
    averaged_speed = []
    averaged_timestamp = []
    for i in range(0, len(df['v']), window_size):
        window_data = df['v'][i:i + window_size]
        average_speed = window_data.mean()
        averaged_speed.append(average_speed)
        # 每五条数据选择第三条的时间戳作为新的时间戳
        averaged_timestamp.append(df['GPSTime'][i + 2])

    # 创建新的DataFrame保存平均值和新的时间戳数据
    averaged_df = pd.DataFrame({'Average_Speed': averaged_speed, 'GPSTime': averaged_timestamp})

    # 将平均值和新的时间戳数据保存为新的CSV文件（在文件名前面加上'processed_'前缀）
    output_file_path = os.path.join(folder_path, 'processed_' + file)
    averaged_df.to_csv(output_file_path, index=False)

print('处理完成，生成的文件保存在文件夹中。')

import pandas as pd

# 读取CSV文件
file_path = '../imuRecord/10-19/田地——速度8直线掉头.csv'  # 请替换成你的CSV文件路径
data = pd.read_csv(file_path)

# 定义要删除的行范围  csv表格中显示的行数
start_row = 4499  # 起始行（inclusive）
end_row = 4964   # 结束行（exclusive）

# 删除指定行范围的数据  我想删除 表格中的2-3，那实际索引时 1 - 2 ，
data = data.drop(data.index[start_row - 2:end_row - 1])

# 保存修改后的数据到CSV文件
data.to_csv('../imuRecord/10-19/田地——速度8直线掉头.csv', index=False)  # 请替换成你想保存的文件路径

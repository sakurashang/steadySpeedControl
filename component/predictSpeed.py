import pandas as pd
from sklearn.linear_model import LinearRegression

# 从CSV文件中读取数据
data = pd.read_csv('output_file3.csv')

# 提取坡度和期望速度作为输入特征
X = data[['坡度', '实际速度']]

# 提取速度指令值作为输出
y = data['速度指令']

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X, y)

# 假设你希望进行预测的坡度和期望速度
slope = -2  # 坡度为十度
desired_speed = 0.42  # 期望的实际速度

# 进行预测
predicted_command_speed = model.predict([[slope, desired_speed]])

print("预测的速度指令值：", predicted_command_speed[0])

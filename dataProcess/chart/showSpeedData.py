import os
import pandas as pd
import plotly.graph_objects as go

# 指定包含CSV文件的文件夹路径
folder_path = '../tempdata/速度4/'  # 请替换为实际的文件夹路径

# 获取文件夹中所有的CSV文件
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# 创建一个空的Figure对象
fig = go.Figure()

# 遍历每个CSV文件，读取数据并添加到Figure对象中
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    # 添加折线到Figure对象中，使用文件名作为标签
    fig.add_trace(go.Scatter(x=df.index, y=df['v'], mode='lines', name=file))

# 设置图表布局和标题
fig.update_layout(title='Speed Data Comparison', xaxis_title='Row Number', yaxis_title='Speed (km/h)')

# 显示交互式图表
fig.show()

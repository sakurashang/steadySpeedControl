import pandas as pd
import plotly.express as px
import numpy as np

# 读取CSV文件中的数据
df = pd.read_csv('../2.csv')

# 移动平均滤波，窗口大小为3，可以根据需要调整
df['Speed_filtered'] = df['v'].rolling(window=3).mean()

# 创建交互式折线图
fig = px.line(df, x='GPSTime', y=['v', 'Speed_filtered'], title='Speed Data with Moving Average Filtering',
              labels={'Speed': 'Speed (km/h)', 'Timestamp': 'Timestamp'})

# 显示交互式图表
fig.show()

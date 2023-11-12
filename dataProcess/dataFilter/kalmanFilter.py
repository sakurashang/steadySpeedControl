import pandas as pd
import numpy as np
from pykalman import KalmanFilter
import plotly.express as px

# 读取CSV文件中的数据
df = pd.read_csv('../2.csv')

# 使用卡尔曼滤波器进行速度数据处理
kf = KalmanFilter(initial_state_mean=0, n_dim_obs=1)
kf = kf.em(df['v'].values, n_iter=10)
(filtered_state_means, _) = kf.filter(df['v'].values)

# 将滤波后的数据保存到DataFrame中
df['Speed_filtered'] = filtered_state_means

# 创建交互式折线图
fig = px.line(df, x='GPSTime', y=['v', 'Speed_filtered'], title='Speed Data with Kalman Filtering',
              labels={'Speed': 'Speed (km/h)', 'Timestamp': 'Timestamp'})

# 显示交互式图表
fig.show()

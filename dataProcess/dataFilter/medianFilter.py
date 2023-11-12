import pandas as pd
import plotly.express as px
import scipy.signal

# 读取CSV文件中的数据
df = pd.read_csv('../../imuRecord/10-16/processed_果园—上坡4.csv')

# 中值滤波，窗口大小为3，可以根据需要调整
df['Speed_filtered'] = scipy.signal.medfilt(df['v'], kernel_size=3)

df['GPSTime'] = df['GPSTime'].astype(str).str[-6:]

# 创建交互式折线图
fig = px.line(df, x='GPSTime', y=['v', 'Speed_filtered'], title='Speed Data with Median Filtering',
              labels={'Speed': 'Speed (km/h)', 'Timestamp': 'Timestamp'})

# 显示交互式图表
fig.show()

import pandas as pd
from sklearn.svm import SVR
import pickle

# 从CSV文件中读取数据
data = pd.read_csv('test_data.csv')

# 提取坡度和实际速度作为输入特征
X = data[['坡度', '实际速度']]

# 提取速度指令值作为输出
y = data['速度指令']

# 创建SVR模型
model = SVR(kernel='rbf', C=1.0, epsilon=0.2)

# 训练模型
model.fit(X, y)

# 保存模型到文件
with open('svr_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)


import  pickle
# 加载模型
with open('svr_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# 假设你希望进行预测的坡度和实际速度
slope = 8  # 坡度为十度
actual_speed = 10  # 实际的速度指令

# 自定义逻辑判断和重新预测的循环
while True:
    # 进行预测
    predicted_output = loaded_model.predict([[slope, actual_speed]])

    if slope > 0 and predicted_output < actual_speed:
        # 当坡度为正时，如果预测的速度指令值小于实际速度，将坡度增加1度进行重新预测
        slope += 1
    elif slope < 0 and predicted_output > actual_speed:
        # 当坡度为负时，如果预测的速度指令值大于实际速度，将坡度减小1度进行重新预测
        slope -= 1
    else:
        # 如果满足条件，跳出循环
        break

print("预测的速度指令值（经过逻辑判断后）：", predicted_output[0])

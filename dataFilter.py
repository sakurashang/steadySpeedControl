import csv

# 打开CSV文件
with open('imuRecord/10-10/行驶时记录数据2023-10-10 11:07:50.csv', 'r') as csvfile:
    # 读取CSV文件内容
    csvreader = csv.reader(csvfile)

    # 跳过第一行（标题行）
    next(csvreader)

    # 遍历CSV文件的每一行
    for idx, row in enumerate(csvreader):
        # 确保当前行有足够的字段（根据实际情况可能需要调整）
        if len(row) >= 2:
            # 获取v字段的值（假设v字段在第二列，索引为1）
            v_value = float(row[6])  # 转换为浮点数进行比较

            # 判断v字段的值是否在指定范围内
            if v_value > 3.3 or 2 < v_value < 2.7:
                print(f"Row {idx + 2}: {row}")

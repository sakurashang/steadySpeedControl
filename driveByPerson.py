import os
import time
from component import classOfDataRecord2
from component.classOfIMU import Imu

def check_mkdir(path_prefix):
    """
        检查文件夹是否存在，若不存在，则创建
    :param path_prefix:路径前缀，string型。eg:"pathRecord/ctrlCAN/"
    :return:
    """

    is_exists = os.path.exists(path_prefix + time.strftime("%Y-%m-%d", time.localtime()))
    if not is_exists:
        os.makedirs(path_prefix + time.strftime("%Y-%m-%d", time.localtime()))
    else:
        print("path 存在")






if __name__ == "__main__":
    cmd_v = 8
    # 0代表人驾驶  1代表自动驾驶
    control_mode = 0
    shiftLevel = 10
    path = r'imuRecord/10-19/'
    record = classOfDataRecord2.DataRecord(path + "行驶时记录数据" +
                                           time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +
                                          ".csv")
    imu = Imu()
    while True:
            imuInfo = imu.stateOfCar()
            msg = imuInfo + [cmd_v,control_mode,shiftLevel]
            record.data_record(msg)
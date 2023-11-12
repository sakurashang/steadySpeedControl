import os
import time
from component import classOfDataRecord2, classOfDF2204
from component.classOfDF2204 import Tractor
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
    cmd_v = 5
    shiftLevel = 10
    #1、车速（0-60） 2、前进（1前进，0空档，-1后退）4、导航模式（0、手动模式 1、扭矩2、自动模式）
    NAVI_cmd_list = [cmd_v, 1, 0, 2, 0, 0]  # v=3,前进挡，测试横纵向连通性
    #1、档位选择（#0-9 低档 10-20 中档 21-60 高档
    NAVI2_cmd_list = [shiftLevel, 0, 250, 250, 250]
    #5、前轮转角 7、请求刹车(0不刹车、1、刹车 ，扭矩模式时起作用） 8控制扭矩（扭矩模式时起作用）
    NAVI3_cmd_list = [0, 0, 0, 0, 0, 0, 0, 0]

    # 20210705 更新:测试横向跟踪性能
    tractor = Tractor("send")
    # while True:
    #     tractor.send_msg("NAVI", NAVI_cmd_list)
    #     NAVI3_cmd_list[4] = 0
    #     tractor.send_msg("NAVI3", NAVI3_cmd_list)

    # 读取车辆信息，并显示,还有记录下来
    # tractor.send_msg("NAVI", NAVI_cmd_list)
    # tractor.send_msg("NAVI2", NAVI2_cmd_list)
    # tractor_recv = classOfDF2204.Tractor("recv")
    # # 判断文件夹是否存在
    # path_prefix = 'tractorStatusInfoRecord/'
    # check_mkdir(path_prefix)
    # path_name = path_prefix + time.strftime("%Y-%m-%d", time.localtime()) + '/'
    # # 数据存储
    # data_record = classOfTractorStatusDataRecord.TractorStatusDataRecord(
    #     path_name + "行驶反馈数据" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ".csv")
    # while True:
    #     # print()
    #     msg_list = tractor_recv.recv_msg_full_dbc_id()
    #     data_record.data_record([time.time()] + msg_list)


    path = r'imuRecord/10-19/'
    record = classOfDataRecord2.DataRecord(path + "行驶时记录数据" +
                                           time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +
                                          ".csv")
    tractor_recv = classOfDF2204.Tractor("recv")
    imu = Imu()
    # v = tractor_recv.recv_msg_v()
    # print(v,imu.stateOfCar())
    # time.sleep(10)
    # imu.stateOfCar()
    # v = tractor_recv.recv_msg_v()
    # print(v, imu.stateOfCar())
    #i = 1
    # while True:
    #     i += 1
    #     if i <= 80 :
    #         tractor.send_msg("NAVI", NAVI_cmd_list)
    #         tractor.send_msg("NAVI2", NAVI2_cmd_list)
    #         imuInfo = imu.stateOfCar()
    #         v = tractor_recv.recv_msg_v()
    #         msg = imuInfo+ [cmd_v,v,shiftLevel]
    #         record.data_record(msg)
    #     elif 80 < i <= 120:
    #         cmd_v = 4
    #         shiftLevel = 3
    #         # 1、车速（0-60） 2、前进（1前进，0空档，-1后退）4、导航模式（0、手动模式 1、扭矩2、自动模式）
    #         NAVI_cmd_list = [cmd_v, 1, 0, 2, 0, 0]  # v=3,前进挡，测试横纵向连通性
    #         # 1、档位选择（#0-9 低档 10-20 中档 21-60 高档
    #         NAVI2_cmd_list = [shiftLevel, 0, 250, 250, 250]
    #         # 5、前轮转角 7、请求刹车(0不刹车、1、刹车 ，扭矩模式时起作用） 8控制扭矩（扭矩模式时起作用）
    #         NAVI3_cmd_list = [0, 0, 0, 0, 0, 0, 0, 0]
    #         tractor.send_msg("NAVI", NAVI_cmd_list)
    #         tractor.send_msg("NAVI2", NAVI2_cmd_list)
    #         imuInfo = imu.stateOfCar()
    #         v = tractor_recv.recv_msg_v()
    #         msg = imuInfo + [cmd_v, v, shiftLevel]
    #         record.data_record(msg)
    #     else:
    #         cmd_v = 5
    #         shiftLevel = 10
    #         # 1、车速（0-60） 2、前进（1前进，0空档，-1后退）4、导航模式（0、手动模式 1、扭矩2、自动模式）
    #         NAVI_cmd_list = [cmd_v, 1, 0, 2, 0, 0]  # v=3,前进挡，测试横纵向连通性
    #         # 1、档位选择（#0-9 低档 10-20 中档 21-60 高档
    #         NAVI2_cmd_list = [shiftLevel, 0, 250, 250, 250]
    #         # 5、前轮转角 7、请求刹车(0不刹车、1、刹车 ，扭矩模式时起作用） 8控制扭矩（扭矩模式时起作用）
    #         NAVI3_cmd_list = [0, 0, 0, 0, 0, 0, 0, 0]
    #         tractor.send_msg("NAVI", NAVI_cmd_list)
    #         tractor.send_msg("NAVI2", NAVI2_cmd_list)
    #         imuInfo = imu.stateOfCar()
    #         v = tractor_recv.recv_msg_v()
    #         msg = imuInfo + [cmd_v, v, shiftLevel]
    #         record.data_record(msg)

    while True:
            tractor.send_msg("NAVI", NAVI_cmd_list)
            tractor.send_msg("NAVI2", NAVI2_cmd_list)
            imuInfo = imu.stateOfCar()
            car_v = tractor_recv.recv_msg_v()
            msg = imuInfo + [cmd_v,car_v,shiftLevel]
            record.data_record(msg)
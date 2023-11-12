# 程序一运行就开始记录小车的轨迹，以一定的时间间隔，这样来减少记录的点数
# 重点就是读取IMU数据并保存为csv
import time
import component.classOfIMU as classOfIMU_CGI610
import component.classOfDataRecord as classOfDataRecord

imu = classOfIMU_CGI610.Imu()
path = r'pathRecord/'
name = '记录下的要跟踪的轨迹点' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '.csv'
record = classOfDataRecord.DataRecord(name)

delta_t = 1   # 这个是录轨迹点的时间间隔，单位s

cmd_steering = 0
cmd_v = 0
path_target_point_index = 1
while 1:
    # 不断读取imu，然后保存为csv
    path_generate_inte_navi_info = imu.stateOfCar()
    msg = path_generate_inte_navi_info
    record.data_record(msg)
    time.sleep(delta_t)

del record

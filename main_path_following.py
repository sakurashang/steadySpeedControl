"""当前模块进行路径跟踪功能开发，上层的任务规划产生具体的路径点序列。"""
import time
import component.classOfIMU as classOfIMU_CGI610
import component.classOfDF2204 as classOfDongFengSF2204
# import classOfYunLe
import math
import component.steering_ctrl as steering_ctrl
import component.classOfDataRecord as classOfDataRecord
# import classOfCollect_info



#  TODO(wen):把这两个合成一个函数模块，功能为返回utm格式路径点
#  读取utm格式路径点

path_x_y = []
path_slope = []
path_doc = 'slopeCalculate/output_with_slope.csv'
def path_read(path_doc, x_pos, y_pos,slope_pos, path_x_y,path_slope):
    with open(path_doc, 'r') as fileopen:
        fileopen.readline()  # 去表头
        content = fileopen.readlines()
        for msg_line in content:
            # 得到经纬度，然后转换成path_x_y
            msg_line_list = msg_line.split(',')
            # ciee_test.csv
            y = float(msg_line_list[y_pos])
            x = float(msg_line_list[x_pos])  # weiDu
            slope = float(msg_line_list[slope_pos])
            path_x_y.append((x, y))
            path_slope.append(slope)
        fileopen.close()
    print('点加载完成')
# path_read(path_doc, 0, 1, path_x_y)  # ciee_fina
#这里的位置后面还要进行更改
path_read(path_doc, 5, 6, 7,path_x_y,path_slope)   # 记录后再循迹
# path_read(path_doc, 1, 2, path_x_y)   # caochang

# 临时加载20210629，直线路径点
# path_x_y = [(44502.86203611083, 4428582.758912923), (444502.8896622462, 4428582.261046626), (444502.9172883816, 4428581.763180329), (444502.944914517, 4428581.265314032), (444502.9725406524, 4428580.767447736), (444503.0001667877, 4428580.26958144), (444503.0277929231, 4428579.771715143), (444503.0554190585, 4428579.273848847), (444503.08304519387, 4428578.775982549), (444503.11067132925, 4428578.278116253), (444503.13829746464, 4428577.780249956), (444503.1659236, 4428577.282383659), (444503.1935497354, 4428576.784517363), (444503.2211758708, 4428576.286651066), (444503.2488020061, 4428575.78878477), (444503.2764281415, 4428575.290918473), (444503.3040542769, 4428574.793052176), (444503.3316804123, 4428574.29518588), (444503.3593065477, 4428573.797319583), (444503.38693268306, 4428573.299453286), (444503.41455881845, 4428572.801586989), (444503.44218495383, 4428572.303720692), (444503.4698110892, 4428571.805854396), (444503.49743722455, 4428571.3079881), (444503.52506335994, 4428570.810121804), (444503.5526894953, 4428570.312255506), (444503.5803156307, 4428569.81438921), (444503.6079417661, 4428569.316522913), (444503.6355679015, 4428568.818656616), (444503.66319403687, 4428568.32079032), (444503.69082017225, 4428567.822924023), (444503.71844630764, 4428567.325057725), (444503.74607244297, 4428566.82719143), (444503.77369857836, 4428566.329325133), (444503.80132471374, 4428565.831458837), (444503.8289508491, 4428565.33359254), (444503.8565769845, 4428564.835726243), (444503.8842031199, 4428564.337859946), (444503.9118292553, 4428563.839993649), (444503.9394553907, 4428563.342127353), (444503.967081526, 4428562.844261057), (444503.9947076614, 4428562.3463947605), (444504.0223337968, 4428561.848528463), (444504.04995993216, 4428561.350662166), (444504.07758606755, 4428560.85279587), (444504.10521220294, 4428560.354929573), (444504.1328383383, 4428559.857063277), (444504.1604644737, 4428559.35919698), (444504.1880906091, 4428558.861330682), (444504.2157167444, 4428558.363464387), (444504.2433428798, 4428557.86559809), (444504.2709690152, 4428557.367731794), (444504.2985951506, 4428556.869865497), (444504.32622128597, 4428556.3719991995), (444504.35384742136, 4428555.874132903), (444504.38147355674, 4428555.376266606), (444504.40909969213, 4428554.87840031), (444504.4367258275, 4428554.380534013), (444504.46435196284, 4428553.882667717), (444504.49197809823, 4428553.38480142), (444504.5196042336, 4428552.886935123), (444504.547230369, 4428552.389068827), (444504.5748565044, 4428551.89120253), (444504.6024826398, 4428551.393336233), (444504.63010877516, 4428550.895469937), (444504.65773491055, 4428550.397603639), (444504.68536104594, 4428549.899737343), (444504.71298718126, 4428549.401871047), (444504.74061331665, 4428548.90400475), (444504.76823945204, 4428548.406138454), (444504.7958655874, 4428547.9082721565), (444504.8234917228, 4428547.41040586), (444504.8511178582, 4428546.912539563), (444504.8787439936, 4428546.414673266), (444504.90637012897, 4428545.91680697), (444504.93399626436, 4428545.418940673), (444504.9616223997, 4428544.921074377), (444504.9892485351, 4428544.42320808), (444505.01687467046, 4428543.925341784), (444505.04450080585, 4428543.427475487), (444505.07212694123, 4428542.92960919), (444505.0997530766, 4428542.4317428935), (444505.127379212, 4428541.933876596), (444505.1550053474, 4428541.436010299), (444505.1826314828, 4428540.938144003), (444505.2102576181, 4428540.440277707), (444505.2378837535, 4428539.942411411), (444505.2655098889, 4428539.4445451135), (444505.29313602427, 4428538.946678817), (444505.32076215965, 4428538.44881252), (444505.34838829504, 4428537.950946223), (444505.3760144304, 4428537.453079927), (444505.4036405658, 4428536.95521363), (444505.4312667012, 4428536.4573473325), (444505.4588928365, 4428535.959481037), (444505.4865189719, 4428535.46161474), (444505.5141451073, 4428534.963748444), (444505.5417712427, 4428534.465882147), (444505.5693973781, 4428533.9680158505), (444505.59702351346, 4428533.470149553), (444505.62464964885, 4428532.972283256), (444505.65227578423, 4428532.47441696), (444505.6799019196, 4428531.976550663), (444505.70752805495, 4428531.478684368), (444505.73515419033, 4428530.9808180705), (444505.7627803257, 4428530.482951773), (444505.7904064611, 4428529.985085477), (444505.8180325965, 4428529.48721918), (444505.8456587319, 4428528.989352884), (444505.87328486727, 4428528.491486587), (444505.90091100265, 4428527.9936202895), (444505.928537138, 4428527.495753994), (444505.95616327337, 4428526.997887697), (444505.98378940875, 4428526.500021401), (444506.01141554414, 4428526.002155104), (444506.0390416795, 4428525.504288807), (444506.0666678149, 4428525.00642251), (444506.0942939503, 4428524.508556213), (444506.1219200857, 4428524.010689917), (444506.1495462211, 4428523.51282362), (444506.1771723564, 4428523.014957325), (444506.2047984918, 4428522.517091027), (444506.2324246272, 4428522.01922473), (444506.26005076256, 4428521.521358434), (444506.28767689795, 4428521.023492137), (444506.31530303333, 4428520.52562584), (444506.3429291687, 4428520.027759544), (444506.3705553041, 4428519.5298932465), (444506.3981814395, 4428519.03202695), (444506.4258075748, 4428518.534160654), (444506.4534337102, 4428518.036294358), (444506.4810598456, 4428517.538428061), (444506.508685981, 4428517.040561764), (444506.53631211637, 4428516.542695467), (444506.56393825175, 4428516.04482917), (444506.59156438714, 4428515.546962873), (444506.6191905225, 4428515.049096577), (444506.6468166579, 4428514.55123028), (444506.67444279324, 4428514.053363984), (444506.70206892863, 4428513.555497687), (444506.729695064, 4428513.057631391), (444506.7573211994, 4428512.559765094), (444506.7849473348, 4428512.061898797), (444506.8125734702, 4428511.564032501), (444506.84019960556, 4428511.0661662035), (444506.86782574095, 4428510.568299907), (444506.89545187633, 4428510.07043361), (444506.92307801166, 4428509.572567314), (444506.95070414705, 4428509.074701018), (444506.97833028244, 4428508.576834721), (444507.0059564178, 4428508.078968424), (444507.0335825532, 4428507.581102127), (444507.0612086886, 4428507.08323583), (444507.088834824, 4428506.585369534), (444507.11646095937, 4428506.087503237), (444507.14408709476, 4428505.5896369405), (444507.1717132301, 4428505.091770644), (444507.19933936547, 4428504.593904347), (444507.22696550086, 4428504.096038051), (444507.25459163624, 4428503.598171754), (444507.28221777163, 4428503.100305458), (444507.309843907, 4428502.60243916), (444507.3374700424, 4428502.104572863), (444507.3650961778, 4428501.606706567), (444507.3927223132, 4428501.10884027), (444507.4203484485, 4428500.610973975), (444507.4479745839, 4428500.113107678), (444507.4756007193, 4428499.61524138), (444507.50322685466, 4428499.117375084), (444507.53085299005, 4428498.619508787), (444507.55847912544, 4428498.121642491), (444507.5861052608, 4428497.623776194), (444507.6137313962, 4428497.125909897), (444507.6413575316, 4428496.6280436), (444507.6689836669, 4428496.130177304), (444507.6966098023, 4428495.632311008), (444507.7242359377, 4428495.134444711), (444507.7518620731, 4428494.636578414), (444507.77948820847, 4428494.138712117), (444507.80711434386, 4428493.64084582), (444507.83474047924, 4428493.142979524), (444507.86236661463, 4428492.645113227), (444507.88999274996, 4428492.147246932), (444507.91761888535, 4428491.649380635), (444507.94524502073, 4428491.151514337), (444507.9728711561, 4428490.653648041), (444508.0004972915, 4428490.155781744), (444508.0281234269, 4428489.657915447), (444508.0557495623, 4428489.160049151), (444508.08337569766, 4428488.662182854), (444508.11100183305, 4428488.164316557), (444508.1386279684, 4428487.666450261), (444508.16625410377, 4428487.168583965), (444508.19388023915, 4428486.670717668), (444508.22150637454, 4428486.172851371), (444508.2491325099, 4428485.674985074), (444508.2767586453, 4428485.177118777), (444508.3043847807, 4428484.679252481), (444508.3320109161, 4428484.181386184), (444508.3596370515, 4428483.683519887), (444508.3872631868, 4428483.1856535915), (444508.4148893222, 4428482.687787294), (444508.4425154576, 4428482.189920998), (444508.47014159296, 4428481.692054701), (444508.49776772835, 4428481.194188404), (444508.52539386373, 4428480.696322108), (444508.5530199991, 4428480.198455811), (444508.5806461345, 4428479.700589514), (444508.6082722699, 4428479.202723217), (444508.6358984052, 4428478.704856921), (444508.6635245406, 4428478.206990625), (444508.691150676, 4428477.709124328), (444508.7187768114, 4428477.211258031)]
path_x_y = [(0, 0),(10, 10)]
# path_x_y.reverse()

"""增加读取经纬度数据的功能"""
# path_x_y = []
# with open('hardwareInitShell_Doc/ciee_test.csv', 'r') as fileopen:
#     fileopen.readline()  # 去表头
#     fileopen.readline()  # 去表头
#     content = fileopen.readlines()
#
#     for msg_line in content:
#         # 得到经纬度，然后转换成path_x_y
#         msg_line_list = msg_line.split(',')
#         # ciee_test.csv
#         msg_lon = float(msg_line_list[1])
#         msg_lat = float(msg_line_list[0])  # weiDu
#         # caochang_test.csv
#         # msg_lon = float(msg_line_list[1])
#         # msg_lat = float(msg_line_list[2])  # weiDu
#         x, y = ll2xy.ll2xy(lat=msg_lat, lon=msg_lon)
#         path_x_y.append((x, y))
#
#     fileopen.close()


# 增加功能：从csv文件中加载要跟踪的路径。这里加载路径非常耗时,要启动很久。
# path_x_y = []
# with open('记录下的要跟踪的轨迹点2021-01-22 15:12:36.csv', 'r') as fileopen:
#     fileopen.readline()  # 去表头
#     content = fileopen.readlines()
#
#     for msg_line in content:
#         # 得到经纬度，然后转换成path_x_y
#         msg_line_list = msg_line.split(',')
#         msg_lon = float(msg_line_list[2])
#         msg_lat = float(msg_line_list[3])
#         x, y = ll2xy.ll2xy(lat=msg_lat, lon=msg_lon)
#         path_x_y.append((x, y))
#
#     fileopen.close()


#  初始化小车控制参数
headingAngle = 0
x, y = 0, 0
v = 0
Kp = 1.0  # PID参数之一


def isArrive(vehicle_x_y,path_x_y,i):
    # 计算小车与当前目标点的距离
    goalPoint = path_x_y[i]
    distance = math.sqrt((vehicle_x_y[0]-goalPoint[0])**2+(vehicle_x_y[1]-goalPoint[1])**2)
    print("离路径点" + str(i) + "的距离为：" + str(distance))

    # 增加一个记录功能
    net_goal_point = path_x_y[i+1]
    distance2net_point = math.sqrt((vehicle_x_y[0]-net_goal_point[0])**2+(vehicle_x_y[1]-net_goal_point[1])**2)

    if (distance < 1) or (distance2net_point < distance):  # 说明两点的距离要大于0.8m，直线情况下无所谓，但是转弯情况下就有可能跟踪不上路径。可能会出现转圈的情况
        # 此时认为小车到达了
        return True
    else:
        return False

    # 可以启用另一种判别，即到下一点的距离比到当前点的距离小。
    # 即满足小于误差，或者上述条件


def is_arrive(vehicle_x_y, path_x_y, i):
    """
        纯追踪判断小车是否逻辑到达目标点，方便切换目标点用
    :param vehicle_x_y:
    :param path_x_y:
    :param i:
    :return:
    """
    global v
    # 计算小车与当前目标点的距离
    goal_point = path_x_y[i]
    distance = math.sqrt((vehicle_x_y[0] - goal_point[0]) ** 2 + (vehicle_x_y[1] - goal_point[1]) ** 2)
    print("离路径点" + str(i) + "的距离为：" + str(distance))

    # 计算与下一个跟踪点的距离
    next_goal_point = path_x_y[i + 1]
    distance2net_point = math.sqrt((vehicle_x_y[0] - next_goal_point[0]) ** 2 + (vehicle_x_y[1] - next_goal_point[1]) ** 2)

    kv = v
    # 给kv设置上下限
    if kv < 1:
        kv = 1
    if kv > 3.0555:  # 11km/h
        kv = 3.0555

    if (distance < kv) or (distance2net_point < distance):  # 用纯追踪判断，这里k设置为1
        # 此时认为小车到点了
        return True
    else:
        return False


def PIDCtrl():
    pass


def calcAngOfTwoVector(vector1, vector2):
    """
        这里向量用元组来实现，已经是计算好的以原点为起点的向量
    :param vector1:
    :param vector2:
    :return: 返回两个向量的夹角，范围0~180°
    """
    #endAng=0
    AB = [0, 0, vector1[0],vector1[1]]
    CD = [0, 0, vector2[0],vector2[1]]

    def angle(v1, v2):
        # 计算v1，v2两角的0-180度角度
        dx1 = v1[2] - v1[0]
        dy1 = v1[3] - v1[1]
        dx2 = v2[2] - v2[0]
        dy2 = v2[3] - v2[1]
        angle1 = math.atan2(dy1, dx1)
        angle1 = angle1 * 180 / math.pi
        # print(angle1)
        angle2 = math.atan2(dy2, dx2)
        angle2 = angle2 * 180 / math.pi
        # print(angle2)
        if angle1 * angle2 >= 0:
            included_angle = abs(angle1 - angle2)
        else:
            included_angle = abs(angle1) + abs(angle2)
            if included_angle > 180:
                included_angle = 360 - included_angle
        return included_angle

    ang1 = angle(AB, CD)
    # 浮点数应该可以比较大小，但是比较相等要用精度判断
    # if waypoint_x - x > 0:
    #     # 在右边，0~180
    #     endAng = ang1
    # else:
    #     # 在左边，180~360
    #     endAng = 360 - ang1
    print("AB和CD的夹角")
    print(ang1)
    return ang1


def calcAngErrorOfCarAndPoint(vector1, vector2):
    """
        2021/1/12 未完成，完成功能后删除
        实现目标航向和小车航向的偏差计算
    :param vector1:目标航向
    :param vector2:实际航向
    :return: 返回两个向量的夹角，范围从目标航向逆时针0~180°，从目标航向顺时针0~-180°
    """
    #endAng=0
    AB = [0, 0, vector1[0],vector1[1]]
    CD = [0, 0, vector2[0],vector2[1]]

    def angle(v1, v2):
        # 计算v1，v2两角的0-180度角度
        dx1 = v1[2] - v1[0]
        dy1 = v1[3] - v1[1]
        dx2 = v2[2] - v2[0]
        dy2 = v2[3] - v2[1]
        angle1 = math.atan2(dy1, dx1)
        angle1 = angle1 * 180 / math.pi
        # print(angle1)
        angle2 = math.atan2(dy2, dx2)
        angle2 = angle2 * 180 / math.pi
        # print(angle2)
        if angle1 * angle2 >= 0:
            included_angle = abs(angle1 - angle2)
        else:
            included_angle = abs(angle1) + abs(angle2)
            if included_angle > 180:
                included_angle = 360 - included_angle
        return included_angle

    ang1 = angle(AB, CD)
    # 浮点数应该可以比较大小，但是比较相等要用精度判断
    # if waypoint_x - x > 0:
    #     # 在右边，0~180
    #     endAng = ang1
    # else:
    #     # 在左边，180~360
    #     endAng = 360 - ang1
    print("AB和CD的夹角")
    print(ang1)
    return ang1


def calcAngOfY_Axis(vector):
    """
        计算向量与Y轴的顺时针夹角，范围0~360°
    :param vector:
    :return: 返回两个向量的夹角
    """
    #endAng=0
    vector1 = (0, 1)  # Y axis
    vector2 = vector
    AB = [0, 0, vector1[0], vector1[1]]
    CD = [0, 0, vector2[0], vector2[1]]

    def angle(v1, v2):
        # 计算v1，v2两角的0~180度角度
        dx1 = v1[2] - v1[0]
        dy1 = v1[3] - v1[1]
        dx2 = v2[2] - v2[0]
        dy2 = v2[3] - v2[1]
        angle1 = math.atan2(dy1, dx1)
        angle1 = angle1 * 180 / math.pi
        # print(angle1)
        angle2 = math.atan2(dy2, dx2)
        angle2 = angle2 * 180 / math.pi
        # print(angle2)
        if angle1 * angle2 >= 0:
            included_angle = abs(angle1 - angle2)
        else:
            included_angle = abs(angle1) + abs(angle2)
            if included_angle > 180:
                included_angle = 360 - included_angle
        return included_angle

    ang1 = angle(AB, CD)
    # 浮点数应该可以比较大小，但是比较相等要用精度判断
    # if waypoint_x - x > 0:
    #     # 在右边，0~180
    #     endAng = ang1
    # else:
    #     # 在左边，180~360
    #     endAng = 360 - ang1
    if vector2[0] < 0:
        ang1 = 360-ang1
    print("小车指向目标点向量与Y轴夹角=", ang1)
    return ang1


def PControl(target, current):
    """
        P控制器
    :param target:
    :param current:
    :return:
    """
    a = Kp * (target - current)

    return a


class WorkOperation(object):
    # 本类暂时只针对播种作业
    def __init__(self):
        pass

    # 作业路径直线跟踪，机具全部放下
    def work_line_tracking_operation(self):
        pass

    # 掉头前进跟踪路径，机具全部抬起
    def turn_line_tracking_operation(self, direction_flag):
        pass

    # 有中断就保存中断点的信息
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, error):
        self.integral += error
        derivative = error - self.prev_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return output

# 读取坡度和当前速度，并进行PID控制
def control_speed(slope, current_speed):
    # 计算速度差
    speed_error = desired_speed - current_speed

    # 使用PID控制器计算输出
    pid_output = pid_controller.compute(speed_error)

    # 考虑坡度对速度的影响，你可以根据实际需求调整这个映射关系
    # 这里简单地将坡度值乘以一个系数，加到PID输出上
    slope_factor = 0.1  # 调整这个系数以控制坡度对速度的影响
    speed_command = pid_output + slope * slope_factor

    return speed_command




if __name__ == "__main__":
    # 进行算法拖拉机迁移
    # 开启一个线程，进行故障信号的检测

    # 室外路面建议2公里以上
    target_speed = 0  # 单位为km/h
    # 设定速度参考值
    desired_speed = 10.0  # 你的目标速度，单位可以是米/秒
    imu = classOfIMU_CGI610.Imu()
    # tractor = classOfYunLe.Car(1)
    tractor = classOfDongFengSF2204.Tractor("send")
    vcu_cmd = classOfDongFengSF2204.VCUCmd(tractor)
    # 初始化PID控制器
    pid_controller = PIDController(kp=0.1, ki=0.01, kd=0.05)
    path = r'pathRecord/'
    record = classOfDataRecord.DataRecord(path + "行驶时记录数据" +
                                          time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +
                                          ".csv")
    cmd_steering = 0
    cmd_v = 0.5
    Lf = 1.0  # look-ahead distance
    control_mode = 2 # 自动驾驶模式
    shiftLevel = 10 # 中档
    #  初始化第一个跟踪的路径点
    i = 0
    length = len(path_x_y)

    # 测试一下运行一次时间开销:150ms左右
    while i <= length-2:  # 当跟踪的最后一个点时候，结束跟踪，小车制动。因为每步只跟踪一个点，所以i的范围可以从0~length-1,设为len-2保险
        starttime = time.time()
        """全部处理完再合成指令发送"""
        waypoint = path_x_y[i]

        GPSWeek, GPSTime, imu_lon, imu_lat, imu_altitude,headingAngle, x, y, v,  = imu.stateOfCar()  # 执行一次采样一次。这里用imu.stateOfCar实现
        # 20210820新增组合导航状态判断，并记录日志
        # 判断inte_navi status,不是42则停车等待。
        # while inte_navi_status != 42:
        #     # 发送停车指令
        #     vcu_cmd.send_motion_ctrl_msg(2, "空挡", 0.0, 0, 1)
        #     time.sleep(0.2)
        #     inte_navi_status = imu.stateOfCar()[8]


        print(headingAngle, x, y, v)
        vehicle_x_y = (x, y)
        # 计算小车是否到达跟踪点
        if isArrive(vehicle_x_y, path_x_y, i) == False:
            # TODO 进行横向跟踪控制，将控制指令的产生用函数来实现
            # 判断小车航向角是否满足要求:

            # 先判断向量的象限，再计算目标夹角

            # 计算小车指向目标点的向量
            car2goalPoint = (waypoint[0]-x, waypoint[1]-y)

            goalHeadingAng = calcAngOfY_Axis(car2goalPoint)
            #etc = goalAng - headingAngle


            # 转向控制pid实现，需要调参
            #target_headingAngle=0 #小车指向目标点航向角
            cmd_steering = steering_ctrl.PControl(goalHeadingAng, headingAngle, 1)   #这里应该是需要转换角度到相同的起始部位。heading是正北顺时针，goalAng方向是目标方向，是小车指向目标点的方向。
            # cmd_steering = steering_ctrl.pure_pursuit(goalHeadingAng, headingAngle, Lf)
            print('goalHeadingAng-headingAngle=', goalHeadingAng-headingAngle)
            #cmd_steering = headingAngle+cmd_steering
            #cmd_steering = cmd_steering

            # (小车情况)限定在小车接收范围内，+—120°以内，精度0.1。并且误差在60°以上时就方向盘打满.在60°以下进行缩放
            # （拖拉机）计算航向角误差在40°外则打满，不在则取系数为1，暂时先这样，后期再调整。
            if cmd_steering > 40:   # 直接打满40°
                cmd_steering = 40.0
            elif cmd_steering < -40:
                cmd_steering = -40.0
            else:
                cmd_steering = cmd_steering*1
            # 以上，符合条件的转角命令生成完毕

        else:
            # 更新跟踪点为下一个点
            i = i + 1

        # cmd_v filter
        if cmd_v <= 0.0:
            cmd_v = 0.0
        print('cmd_steering=', cmd_steering, 'cmd_v', cmd_v)
        # 示例用法
        slope_value = path_slope[i]  # 假设的坡度值，具体值需要根据实际情况获取
        current_speed_value = v  # 当前速度值，具体值需要根据实际情况获取
        # 计算控制后的速度命令
        result_speed = control_speed(slope_value, current_speed_value)
        speed_cmd = result_speed + current_speed_value
        print('控制后的速度命令:', result_speed)
        vcu_cmd.send_motion_ctrl_msg(2, "前进高档", cmd_steering, speed_cmd, 0)

        # 记录状态。需要记录的数据字段：GPSweek，GPStime，经度，纬度，航向角，x,y,小车发送的指令（转角，速度）.一共九个。
        # 需求：再增加一个字段，存跟踪的i
        # GPSWeek, GPSTime, imu_lon, imu_lat, headingAngle, x, y, v, cmd_steering, cmd_v
        msg = [GPSWeek, GPSTime, imu_lon, imu_lat, headingAngle, x, y, v, cmd_steering, cmd_v,control_mode,shiftLevel]
        record.data_record(msg)

        endtime = time.time()
        print("mpns_循环花销"+str(endtime-starttime)+"s")
        # 按步上传数据
        # collect_info.Info_tran(gps_time=time.time(), gps_status=inte_navi_status, gps_way=1, latitude=imu_lat,
        #                        longitude=imu_lon, altitude=imu_altitude, speed=v, satellite_num=imu_satellite_num,
        #                        warning=imu_warning)
        # collect_info.Info_tran(1,2,3,4,5,6,7,8,9)  # debug

    # collect_info.Info_close()

    # 最后需要停下来，制动
    vcu_cmd.send_motion_ctrl_msg(2, "空挡", 0.0, 0, 1)
    del record

    while 1:
        print('死循环等待')
        time.sleep(1)


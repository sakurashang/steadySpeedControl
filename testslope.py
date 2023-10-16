import math

lateral_displacement = 41
# 纵向位移
longitudinal_displacement = 3.64
# 求坡度
a = math.atan2(longitudinal_displacement, lateral_displacement)
slope = a / math.pi * 180
print(slope)
#print(1696403801.3218622 - 1696403794.9215155 )

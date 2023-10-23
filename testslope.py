import math

slpe_displacement = 230 * 0.98547
#print(slpe_displacement)
# 纵向位移
longitudinal_displacement = 64.16 - 45.52
lateral_displacement = math.sqrt(slpe_displacement ** 2 - longitudinal_displacement ** 2)
#print(lateral_displacement)
# 求坡度
a = math.atan2(longitudinal_displacement, lateral_displacement)
slope = a / math.pi * 180
print(slope)
#print(1696403801.3218622 - 1696403794.9215155 )

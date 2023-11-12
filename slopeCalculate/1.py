import  math
lon1 = 121.51338959
lat1 = 37.43329307
lon2 = 121.51339077
lat2 = 37.43329295
lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

# 地球半径（单位：公里）
R = 6371.0

# 计算差值
dlon = lon2 - lon1
dlat = lat2 - lat1

# 使用Haversine公式计算两点间的距离
a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = R * c

print(distance)
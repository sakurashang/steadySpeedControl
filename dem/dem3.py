import pandas as pd
from osgeo import gdal

def utm_to_pixel(utm_x, utm_y, dataset):
    # 获取地理转换信息
    transform = dataset.GetGeoTransform()

    # 计算像素坐标
    pixel_x = int((utm_x - transform[0]) / transform[1])
    pixel_y = int((utm_y - transform[3]) / transform[5])

    return pixel_x, pixel_y

def get_elevation_at_coordinates(utm_x, utm_y, dataset):
    # 将UTM坐标转换为像素坐标
    pixel_x, pixel_y = utm_to_pixel(utm_x, utm_y, dataset)

    try:
        # 读取DEM中的高程数据
        band = dataset.GetRasterBand(1)
        elevation_data = band.ReadAsArray(pixel_x, pixel_y, 1, 1)

        return elevation_data[0][0]
    except Exception as e:
        print(f"Error reading elevation data: {e}")
        return None

# 读取CSV文件
csv_file_path = "行驶时记录数据2023-11-07+17_26_57.csv"
df = pd.read_csv(csv_file_path)

# DEM文件路径
dem_file_path = "zouping+dem+tiff.tif"
dataset = gdal.Open(dem_file_path)

if dataset is not None:
    # 遍历CSV中的每个跟踪点
    for index, row in df.iterrows():
        utm_x = row['utm_x']  # 请根据实际列名替换
        utm_y = row['utm_y']  # 请根据实际列名替换

        elevation_at_coordinates = get_elevation_at_coordinates(utm_x, utm_y, dataset)

        if elevation_at_coordinates is not None:
            print(f"At UTM coordinates ({utm_x}, {utm_y}), elevation is: {elevation_at_coordinates} meters")
else:
    print("无法打开DEM文件")

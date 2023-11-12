from osgeo import gdal
from osgeo import osr

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

    # 读取DEM中的高程数据
    band = dataset.GetRasterBand(1)
    elevation_data = band.ReadAsArray(pixel_x, pixel_y, 1, 1)

    return elevation_data[0][0]

# 示例使用
dem_file_path = "zouping+dem+tiff.tif"
utm_x = 570879.170  # 请替换为实际的UTM X坐标
utm_y = 4089431.875 # 请替换为实际的UTM Y坐标

# 打开DEM文件
dataset = gdal.Open(dem_file_path)

if dataset is not None:
    elevation_at_coordinates = get_elevation_at_coordinates(utm_x, utm_y, dataset)
    print(f"在UTM坐标({utm_x}, {utm_y})处的高程为：{elevation_at_coordinates} 米")
else:
    print("无法打开DEM文件")

from osgeo import gdal

def read_dem(file_path):
    # 打开DEM文件
    dataset = gdal.Open(file_path)

    if dataset is None:
        print("无法打开DEM文件")
        return None

    # 获取DEM的行数、列数
    rows = dataset.RasterYSize
    cols = dataset.RasterXSize

    # 读取DEM中的高程数据
    band = dataset.GetRasterBand(1)  # 1表示获取第一个波段
    elevation_data = band.ReadAsArray(0, 0, cols, rows)

    # 关闭DEM文件
    dataset = None

    return elevation_data

# 示例使用
dem_file_path = "zouping+dem+tiff.tif"
elevation_data = read_dem(dem_file_path)

if elevation_data is not None:
    print("成功读取DEM中的高程数据")
    print("高程数据数组：", elevation_data)
else:
    print("读取DEM失败")

from osgeo import gdal

def get_geotransform_info(file_path):
    dataset = gdal.Open(file_path)

    if dataset is not None:
        # 获取地理转换信息
        transform = dataset.GetGeoTransform()

        # 打印地理转换信息
        print(f"左上角 X 坐标: {transform[0]}")
        print(f"水平像素分辨率: {transform[1]}")
        print(f"旋转参数（通常为0）: {transform[2]}")
        print(f"左上角 Y 坐标: {transform[3]}")
        print(f"旋转参数（通常为0）: {transform[4]}")
        print(f"垂直像素分辨率: {transform[5]}")

        # 计算右下角 X 和 Y 坐标
        width = dataset.RasterXSize
        height = dataset.RasterYSize
        right_bottom_x = transform[0] + width * transform[1] + height * transform[2]
        right_bottom_y = transform[3] + width * transform[4] + height * transform[5]

        print(f"右下角 X 坐标: {right_bottom_x}")
        print(f"右下角 Y 坐标: {right_bottom_y}")

        # 关闭文件
        dataset = None
    else:
        print("无法打开文件")

# 示例使用
tif_file_path = "zouping+dem+tiff.tif"
get_geotransform_info(tif_file_path)

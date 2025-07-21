import re
import matplotlib.pyplot as plt

# 预处理正则表达式，用于解析 GPS 数据
pattern = re.compile(
    r"\$GPGGA,(\d+\.\d+),(-?\d+\.\d+),([NS]),(-?\d+\.\d+),([EW]),(\d),(\d+),(\d+\.\d+),(-?\d+\.\d+),M,(-?\d+\.\d+),M,,")

# 初始化经度、纬度列表
lons, lats = [], []

# 遍历每一行 GPS 数据
for line in open("CatchCat.txt", "r"):
    # 匹配 GPS 数据
    m = pattern.match(line)
    if m:
        # 解析 GPS 数据
        lat = float(m.group(2))
        lat_dir = m.group(3)
        lon = float(m.group(4))
        lon_dir = m.group(5)

        # 将角度转换为弧度
        lat = (lat / 100.0) + (lat % 100.0) / 60.0
        lon = (lon / 100.0) + (lon % 100.0) / 60.0

        # 根据方向符号调整经度、纬度值
        if lat_dir == "S":
          lat = -lat
        if lon_dir == "W":
          lon = -lon

        # 将经度、纬度添加到列表中
        lons.append(lon)
        lats.append(lat)

# 绘制经度、纬度坐标图
plt.plot(lons, lats)

# 添加坐标轴标签
plt.xlabel("Longitude (degrees)")
plt.ylabel("Latitude (degrees)")

# 显示图表
plt.show()

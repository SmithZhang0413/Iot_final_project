from PIL import Image, ImageDraw
from ndtest import *
import csv
import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

North_lati, North_long = 24.79610, 120.99576  # 最上
East_lati, East_long = 24.79572, 120.99632  # 最右
West_lati, West_long = 24.79481, 120.99481  # 最左
South_lati, South_long = 24.79464, 120.99541  # 最下
vertx = [North_long, East_long, West_long, South_long]
verty = [North_lati, East_lati, West_lati, South_lati]


# max = df["latitude"].max

# --------------------------------
def pltShow(xx, yy, num):
    z = np.random.random(size=[xx.size, num])

    x = (z / sum(z)).T.dot(xx)
    y = (z / sum(z)).T.dot(yy)
    # 绘制点：黄色
    plt.plot(x, y, 'yo')
    plt.grid(True)

    # 绘制顶点：绿色
    for i in range(xx.size):
        plt.plot(xx[i], yy[i], 'go')
    return x, y
    #plt.show()


def gen_poly(node_num):
    yy = np.array([North_long, East_long, West_long, South_long])
    xx = np.array([North_lati, East_lati, West_lati, South_lati])
    x,y = pltShow(xx, yy, node_num)

    return x, y

# _-------------------------------

def poly_test(testx, testy):  # 从test point印一条射线，计算它穿过的边数，用到了Jordan Curve Theorem
    c = 0
    j = 3
    for i in range(0, 4):
        if ((verty[i] > testy) != (verty[j] > testy)) \
                and (testx < (vertx[j] - vertx[i]) * (testy - verty[i]) / (verty[j] - verty[i]) + vertx[i]):
            c = ~c
        j = i
    return c


def draw_map(df):  # 纬度，经度

    plt.plot([North_lati, East_lati], [North_long, East_long], linewidth=0.5) + \
    plt.plot([East_lati, South_lati], [East_long, South_long], linewidth=0.5) + \
    plt.plot([South_lati, West_lati], [South_long, West_long], linewidth=0.5) + \
    plt.plot([West_lati, North_lati], [West_long, North_long], linewidth=0.5)

    for index, row in df.iterrows():  # 只画出四边形内的点
        if df.loc[index, 'valid'] == 1:
            plt.plot(df.loc[index, 'latitude'], df.loc[index, 'longitude'], '.')
    plt.show()


def inital(file_name):
    x1 = []
    y1 = []
    valid_node = 0
    df = pd.read_csv(file_name)
    df.insert(2, "latitude", 0)
    df.insert(3, "longitude", 0)
    df.insert(4, "valid", 0)
    df.insert(5, "valid_latitude", 0)
    df.insert(6, "valid_longitude", 0)
    # 转化GPS坐标，去掉日期只保留时间
    for index, row in df.iterrows():  # 遍历data这一col的每个data，转为16进制并补零
        num = hex(int(row['data']))  # 16进制
        hexi = num[0:2]
        num = num[2:]  # 去掉0X

        if len(num) == 16:
            num = num
        else:
            num = num.zfill(16)

        latitude = float(int(hexi + num[0:8], 16)) / 10000000  # 前8位为南北纬度
        longitude = float(int(hexi + num[8:16], 16)) / 10000000  # 后8位为东西经度
        df.loc[index, 'latitude'] = latitude
        df.loc[index, 'longitude'] = longitude
        # 去掉时间
        df.loc[index, 'Time'] = row['Time'][11:]
        # 只保留框内数据
        if poly_test(longitude, latitude) == -1:
            df.loc[index, 'valid'] = 1
            df.loc[index, 'valid_longitude'] = longitude
            df.loc[index, 'valid_latitude'] = latitude
            x1.append(latitude)
            y1.append(longitude)
            valid_node = valid_node + 1
        else:
            df.loc[index, 'valid'] = 0
    return df,valid_node,x1,y1


def main():
    file_name = "dataset/aa.csv"
    df, valid_node, x1, y1 = inital(file_name)
    draw_map(df)

    x2,y2 = gen_poly(valid_node)                        #生成均匀分布的点

    y1 = np.array(y1)
    x1 = np.array(x1)
    #print(x1.size,x2.size)

    p , d= ks2d2s(x1,y1,x2,y2,extra=True)               # KS Test
    print(p)
    print(d)


if __name__ == "__main__":
    main()

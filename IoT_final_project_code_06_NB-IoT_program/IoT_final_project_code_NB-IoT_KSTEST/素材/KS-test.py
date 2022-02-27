import matplotlib.pyplot as plt
import numpy as np
North_lati, North_long = 24.79610, 120.99576  # 最上
East_lati, East_long = 24.79572, 120.99632  # 最右
West_lati, West_long = 24.79481, 120.99481  # 最左
South_lati, South_long = 24.79464, 120.99541  # 最下
# 传入顶点的x坐标，y坐标，生成的点个数num
def pltShow(xx, yy, num):
    z = np.random.random(size=[xx.size, num])

    x = (z / sum(z)).T.dot(xx)
    y = (z / sum(z)).T.dot(yy)
    print(x[1])
    # 绘制点：黄色
    plt.plot(x, y, 'yo')
    plt.grid(True)

    # 绘制顶点：绿色
    for i in range(xx.size):
        plt.plot(xx[i], yy[i], 'go')

    plt.show()


# 随机生成N边形的N个顶点
def createPolygon(n):
    ##xx = np.random.randint(1, 500, n)
    ##yy = np.random.randint(1, 500, n)
    yy = np.array([North_long, East_long, West_long, South_long])
    xx = np.array([North_lati, East_lati, West_lati, South_lati])
    print(xx)
    print(yy)
    return xx, yy


if __name__ == '__main__':

    xx, yy = createPolygon(4)

    pltShow(xx, yy, 1000)

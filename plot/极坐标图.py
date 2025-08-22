from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 极坐标图
theta = np.arange(0, 2*np.pi, 0.02)     # np.arange()函数返回一个有终点和起点的固定步长的排列

plt.subplot(121, polar=True)
plt.plot(theta, theta/6, linewidth=2.0)     # 第一个参数是角度，第二个参数是极径

plt.subplot(122, polar=True)
plt.plot(theta, 1.4*np.cos(5*theta), linewidth=2.0)


plt.plot(theta, 1.8*np.cos(4*theta), "--", linewidth=2.0)       # 花在第二个图中
plt.rgrids(np.arange(0.5, 2, 0.5), angle=45)    # 网格绘制

plt.show()

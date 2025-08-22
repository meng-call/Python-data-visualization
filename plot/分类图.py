# 对数坐标图
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["font.family"]="KaiTi"
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0.1, 1000, 1000)  # linspace 生成等间距数值序列
y = np.abs(1/(1+0.01j*x))

plt.subplot(221)
plt.plot(x, y, linewidth=2.0, label="算术对数坐标系")
plt.ylim(0, 1.5)    # 设置y轴范围
plt.legend()

plt.subplot(222)
plt.semilogx(x, y, linewidth=2.0, label="X轴对数坐标系")
plt.ylim(0, 1.5)
plt.legend()

plt.subplot(223)
plt.semilogy(x, y, linewidth=2.0, label="Y轴对数坐标系")
plt.legend()

plt.subplot(224)
plt.loglog(x, y, linewidth=2.0, label="XY轴对数坐标系")
plt.legend()
plt.show()



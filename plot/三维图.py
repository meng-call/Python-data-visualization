from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d

rho, theta = np.mgrid[0:1:20j, 0:4:20j]
# 生成多维的网格坐标点
z = rho**2
x = rho*np.cos(theta)
y = rho*np.sin(theta)

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap="coolwarm")

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel("X")
ax.set_xticks(np.arange(-1.5, 1.5, 0.5))
ax.set_ylabel("Y")
ax.set_yticks(np.arange(-1.5, 1.5, 0.5))
ax.set_zlabel("Z")

plt.show()

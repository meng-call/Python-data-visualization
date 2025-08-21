from matplotlib.font_manager import FontProperties
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.font_manager import FontManager


mpl_fonts = set(f.name for f in FontManager().ttflist)

print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)
    # 输出所有matplotlib支持的字体

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=20)   # 使用Windows的宋体，字号16

x = np.linspace(0,10,100)   # 创建一个等差数列
y = np.cos(x)

plt.figure(1)    # 第一个图表
plt.plot(x, y)

plt.xlabel(u"时间",fontproperties=font)  # 设置x轴标签
plt.ylabel(u"振幅",fontproperties=font)   # 设置y标签
plt.title(u"余弦波",fontproperties=font)

"""还可以直接修改配置标签，这样就不需要在每次绘制文字时设置字体了"""
"""plt.rcParams["font.family"]="KaiTi"""

plt.figure(2)
x = np.random.random(50)
y = x+np.random.random(50)/8

plt.scatter(x, y)   # 散点图
plt.title(u'散点图',fontproperties=font)

plt.show()

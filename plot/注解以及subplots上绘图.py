from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# 创建画布；
# ax是坐标轴对象，后续的绘图和标注操作都基于它

data = pd.read_csv(r'D:\电子教材\python数据分析\中文\python_for_data_analysis_2nd_chinese_version-master\python_for_data_analysis_2nd_chinese_version-master\examples\spx.csv', index_col=0, parse_dates=True)
# index_col=0：此参数指定应该将CSV文件中的哪一列作为DataFrame的索引。
# index_col=0意味着第一列（即索引为0的列）将会被用作DataFrame的行标签（索引）。
# parse_dates=True：这个选项告诉Pandas尝试将数据中的某些列解析为日期时间类型。
# 当设置为True时，Pandas会试图解析index_col指定的列作为日期。
spx = data['SPX']

spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime(2008, 3, 12), 'Bear Stearns Fails'),
    (datetime(2008, 9, 15), 'Lehman Bankruptcy')
]

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                xytext=(date, spx.asof(date) + 225),
                arrowprops=dict(facecolor='black', headwidth=4, width=2,
                                headlength=4),
                horizontalalignment='left', verticalalignment='top')    # 左对齐，顶部对齐
# ax.annotate:在图上添加注释
# label:显示的文本内容
# xy是箭头指向的点，spx.asof(date)：获取在 date 当天或之前最后一个可用的 SPX 指数值。
# + 75：在该价格上方 75 个单位处作为箭头终点。
# xytext=(date, spx.asof(date) + 225)：
# 注释文本放置的位置（比箭头终点再高 150 个单位）。
# arrowprops:定义箭头样式
# Zoom in on 2007-2010
ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])

ax.set_title('Important dates in the 2008-2009 financial crisis')

plt.show()

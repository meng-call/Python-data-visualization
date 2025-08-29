import matplotlib.pyplot as plt
from collections import Counter     # 统计频率

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

decile = lambda grade: grade // 10 * 10
# 定义一个lambda函数来计算每个成绩的“十分位”，即向下取最接近的10的倍数

histogram = Counter(decile(grade) for grade in grades)
# 使用Counter统计每个“十分位”的成绩出现次数

plt.bar([x - 4 for x in histogram.keys()], histogram.values(), width = 8,align = 'edge',color = 'blue',alpha = 0.5 )
# 每个条形向左侧移动4个单位
# 给每个条形设置正确的宽度

plt.axis([-5, 105, 0, 6])
# x轴取值从-5到105
# y轴取值0到6
plt.xticks([10 * i for i in range(11)])  # x轴标记为0，10，...，100

plt.xlabel("十分相")
plt.ylabel("学生数")
plt.title("考试分数分布图")

plt.show()

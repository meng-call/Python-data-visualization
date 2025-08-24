from matplotlib import pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用指定的汉字字体类型（此处为黑体）

data1 = [107, 115, 145, 212, 280]
data2 = [338, 350, 358, 368]
label1 = ["2000年", "2001年", "2002年", "2003年", "2004年"]
label2 = ["2005年", "2006年", "2007年", "2008年"]

explode1 = [0.01, 0.01, 0.01, 0.01, 0.03]
explode2 = [0.01, 0.01, 0.01, 0.03]

fig = plt.figure(figsize=(8, 3))

ax1 = fig.add_subplot(1, 2, 1)
plt.sca(ax1)    # 将当前轴设置为ax1
plt.pie(data1, explode=explode1, labels=label1, autopct="%1.1f%%", startangle=45, radius=0.8)
"""explode设置每个饼块相对于饼圆的偏移距离，autopct设置数值显示形式，startangle设置开始角度，radius设置半径"""

plt.title("2000年-2004年大学毕业人数{0}万".format(sum(data1)))

ax2 = fig.add_subplot(122)    # 定义子图2
plt.sca(ax2)    # 选择子图2
plt.pie(data2, explode=explode2, labels=label2, autopct="%1.1f%%", startangle=90)

plt.title("2005年-2008年大学生毕业人数{0}万".format(sum(data2)))

plt.show()

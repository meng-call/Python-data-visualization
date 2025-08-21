import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=10)   # 使用Windows的宋体，字号16


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]

num_oscars = [5, 11, 3, 8, 10]

# 条形的默认宽度是0.8，因此我们对左侧坐标加上0.4
# 这样每个条形就被放置在中心了
xs = [i + 0.4 for i, _ in enumerate(movies)]

# 使用左侧x坐标[xs]和高度[num_oscars]画条形图
plt.bar(xs, num_oscars)

plt.ylabel(u"所获奥斯卡金像奖数量", fontproperties=font)
plt.title(u"我最喜爱的电影", fontproperties=font)

# 使用电影的名字标记x轴，位置在x轴上条形的中心
plt.xticks([i + 0.4 for i, _ in enumerate(movies)], movies)

plt.show()

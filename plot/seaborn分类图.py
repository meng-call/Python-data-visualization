
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="ticks")
tips = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

sns.stripplot(x="day", y="total_bill", ax=axes[0], data=tips, hue="smoker")
sns.swarmplot(x="day", y="total_bill", ax=axes[1], data=tips)     # 避免数据点出现覆盖情况

sns.despine()
# 移除坐标轴

plt.show()

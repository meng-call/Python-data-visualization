
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
# seaborn的数据集

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True, ax=axes[0])
# split将分类数据进行切分，两边颜色代表不同类别（True：将hue类别合并显示）
sns.swarmplot(x="day", y="total_bill", data=tips, color="r", alpha=.4, ax=axes[0])
# 分簇散点图，以day为x轴，total_bill为y轴

sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, inner="sticks", ax=axes[1])
# inner参数对每个数据进行可视化(‘box'(默认)显示箱线图, 'point' 显示数据点，'sticks' 显示数据分布的棍状线条)

plt.show()

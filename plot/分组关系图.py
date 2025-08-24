import matplotlib.pyplot as plt
import seaborn as sns

# 绘制单变量分布图

tips = sns.load_dataset("tips")

sns.catplot(x="size", col="sex", data=tips, col_wrap=2, kind="count", height=4, aspect=.9)
# #############################
# 单变量分布图

fig, axes = plt.subplots(2, 2, figsize=(10, 6))

sns.histplot(tips["tip"], ax=axes[0][0], bins=15, kde=True, fill=True, )
# 默认方式绘制一个直方图和密度图,bins:箱子个数
sns.histplot(tips["tip"], kde=False, color='blue', linestyle='--', linewidth=2, alpha=0.7, ax=axes[0][1])
# kde为False时不绘制密度图
sns.histplot(tips["tip"], ax=axes[1][0])
sns.histplot(tips["tip"], ax=axes[1][1])
# rug为True时为每个直方图样本点添加小细线
sns.rugplot(tips["tip"], ax=axes[1][1], color='red', alpha=0.5)

plt.tight_layout()
# 能够自动调整子图参数，使之填充整个图像区域且避免重叠。

plt.show()

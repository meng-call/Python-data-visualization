import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
# seaborn的内置数据集

plt.subplot(221)
sns.barplot(x="day", y="tip", hue="sex", data=tips)
# hue按子类别分组，生成分组柱状图；

plt.subplot(222)
sns.barplot(y='day', x='tip', data=tips,palette='Blues_d')

plt.subplot(223)
sns.barplot(x = 'size', y = 'tip', data = tips, palette="plasma_r", ci=95,
           errcolor='yellow', errwidth=2, capsize=0.1,alpha=0.3)

plt.subplot(224)
sns.countplot(x="day", data=tips, palette="Set2")
# palette配色方案

plt.show()

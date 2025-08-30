import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

macro = pd.read_csv(r'D:\电子教材\python数据分析\中文\python_for_data_analysis\python_for_data_analysis\examples\macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]

trans_data = np.log(data).diff().dropna()
# np.log()对每个变量作对数变换，消除指数增长带来的尺度差异。
# diff()再取一阶差分（本月减上月），于是得到近似月度对数收益率（连续复利增长率）
# dropna()：第一个观测差分后是 NaN，直接丢掉。

train_data = trans_data[-5:]
sns.regplot(x='m1', y='unemp', data=trans_data)
# sns.regplot 自动做线性回归并把拟合直线叠加在散点图上。
plt.title('Changes in log %s versus log %s' % ('m1', 'unemp'))

sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
# 散布图矩阵

tips = sns.load_dataset("tips")
sns.catplot(x='day', y=tips['tip']/tips['total_bill'], row='time', col='smoker', kind='bar', data=tips)
print(tips.head())

plt.show()

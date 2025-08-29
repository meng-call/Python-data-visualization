import pandas as pd
from matplotlib import pyplot as plt

tips = pd.read_csv(r'D:\电子教材\python数据分析\中文\python_for_data_analysis\python_for_data_analysis\examples\\tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.loc[:, 2:5]
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
# 先是行求和，后面再将每行除以所求的和

party_pcts.plot.bar()
plt.show()

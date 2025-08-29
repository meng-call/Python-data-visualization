import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
# np.random.randn(10) 生成十个标准正态分布
# .cumsum() 对随机数累加
s.plot(title='Random walk')
x_label = 'Time'
y_label = 'Value'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid(True)
s.plot()
plt.show()

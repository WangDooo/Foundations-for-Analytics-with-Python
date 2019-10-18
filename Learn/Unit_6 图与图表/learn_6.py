# 第六章 图与图表
# matplotlib pandas ggplot seaborn 

#=======条形图=========================================================
# .bar()
#----------------------------------------------------------------
# import matplotlib.pyplot as plt

# plt.style.use('ggplot') # 使用ggplot样式
# customers = ['Wang','Doo','Hu','Ding','Yang']
# customers_index = range(len(customers))
# sale_amounts = [127, 90, 201, 111, 232]
# fig = plt.figure() # 创建一个基础图 在基础图上创建一个或多个子图
# ax1 = fig.add_subplot(1,1,1) # 添加一个子图 (1,1,1)表示创建1行1列的子图，并使用第1个也是唯一的一个子图
# ax1.bar(customers_index,sale_amounts,align='center',color='darkblue') # bar() 创建条形图
# plt.xticks(customers_index,customers,rotation=0,fontsize='small') # 设置刻度标签 rotation=0表示水平
# plt.xlabel('Customer Name')
# plt.ylabel('Sale Amount')
# plt.title('Sale Amount per Customer')
# plt.savefig('bar_plot.png',dpi=400,bbox_inches='tight') #'tight'表示将图片四周空白部分去掉
# plt.show()
#----------------------------------------------------------------


#========直方图========================================================
# 频率分布 频率密度分布 概率分布 概率密度分布
# hist() 柱形图 
#----------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt

# plt.style.use('ggplot')
# mu1,mu2,sigma = 100,130,15
# x1 = mu1+sigma*np.random.randn(10000)
# x2 = mu2+sigma*np.random.randn(10000)
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# n,bins,patches = ax1.hist(x1,bins=50,normed=False,color='g') # bins=50 每个变量的值被分成50份 normed=False 表示数概率分布图不是概率密度
# n,bins,patches = ax1.hist(x2,bins=50,normed=False,color='orange',alpha=0.5) # alpha=0.5 透明度
# plt.xlabel('Bins')
# plt.ylabel('Number of Value in Bin')
# fig.suptitle('Histograms',fontsize=14,fontweight='bold') # suptitle() fig总图标题
# ax1.set_title('Two Frequency Distributions') # set_title() 子图标题
# plt.savefig('histograms.png',dpi=400,bbox_inches='tight')
# plt.show()
#----------------------------------------------------------------


#========折线图========================================================
# 
#----------------------------------------------------------------
# from numpy.random import randn
# import matplotlib.pyplot as plt

# plt.style.use('ggplot')
# plot_data1 = randn(50).cumsum() # cumsum() 累加求和
# plot_data2 = randn(50).cumsum()
# plot_data3 = randn(50).cumsum()
# plot_data4 = randn(50).cumsum()
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# ax1.plot(plot_data1,marker='o',color='b',linestyle='-',label='Blue Solid')
# ax1.plot(plot_data2,marker='+',color='r',linestyle='--',label='Red Dashed')
# ax1.plot(plot_data3,marker='*',color='g',linestyle='-.',label='Green Dash Dot')
# ax1.plot(plot_data4,marker='s',color='y',linestyle=':',label='Yellow Dotted')
# ax1.set_title('Line Plots: Markers, Colors, Linestyles')
# plt.xlabel('Draw')
# plt.ylabel('Random Number')
# plt.legend(loc='best') # legend() 为统计图创建图例
# plt.savefig('line_plot.png',dpi=400,bbox_inches='tight')
# plt.show()
#----------------------------------------------------------------


#=======散点图=========================================================
# 可以画一条回归曲线 使方差最小的曲线 np.polyfit() :拟合  np.poly1d() 使用这些参数创建实际的多项式方程
#----------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt

# plt.style.use('ggplot')
# x = np.arange(1,15)
# y_linear = x+5.*np.random.randn(14)
# y_quadratic = x**2 + 10.*np.random.randn(14)
# fn_linear = np.poly1d(np.polyfit(x,y_linear,deg=1))
# fn_quadratic = np.poly1d(np.polyfit(x,y_quadratic,deg=2))
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# ax1.plot(x,y_linear,'bo',x,y_quadratic,'go',x,fn_linear(x),'b-',x,fn_quadratic(x),'g-',linewidth=2) # 'bo'蓝色原点 'go'绿色原点
# ax1.set_title('Scatter Plots Regression Lines')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.xlim(min(x)-1,max(x)+1) # xlim 设置x轴的范围
# plt.ylim(min(y_quadratic)-10,max(y_quadratic)+10)
# plt.savefig('scatter_plot.png',dpi=400,bbox_inches='tight')
# plt.show()
#----------------------------------------------------------------


#======箱线图==========================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#=======pandas作图=========================================================
# 条形图 箱线图
#----------------------------------------------------------------
# import pandas as pd 
# import numpy as np
# import matplotlib.pyplot as plt

# plt.style.use('ggplot')
# fig, axes = plt.subplots(nrows=1, ncols=2) #  创建一个基础图和两个并排放置的子图
# ax1, ax2 = axes.ravel() # 使用ravel()函数将两个子图分别赋值给ax1 ax2 就不用行列索引了 axes[0,0] axes[0,1]
# data_frame = pd.DataFrame(
# 		np.random.rand(5,3),
# 		index = ['Customer 1','Customer 2','Customer 3','Customer 4','Customer 5'],
# 		columns = pd.Index(['Metric 1','Metric 2','Metric 3'], name='Metrics'))
# data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot') # 条形图
# plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
# plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
# ax1.set_xlabel('Customer')
# ax1.set_ylabel('Value')
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
# colors = dict(boxes='DarkBlue', whiskers='Gray', medians='Red', caps='Black') # 为箱线图单独创建一个颜色字典
# data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box Plot') # 箱线图 r.红色圆点
# plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
# plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
# ax2.set_xlabel('Metric')
# ax2.set_ylabel('Value')
# ax2.xaxis.set_ticks_position('bottom')
# ax2.yaxis.set_ticks_position('left')
# plt.savefig('pandas_plots.png',dpi=400,bbox_inches='tight')
# plt.show()

#----------------------------------------------------------------


#========ggplot========================================================
# 基于R的ggplot2包和图形语法 存在明显缺点
# 区别：语法将数据与实际绘图明确地分离开
# 几种基本元素：几何对象、图形属性、标度
# 附加元素：统计变换、坐标系、子窗口、可视化主题
#----------------------------------------------------------------
import seaborn as sns 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig

sns.set(color_codes=True)
# 直方图 distplot()
x = np.random.normal(size=100) # normal() 正态分布
sns.distplot(x, bins=20, kde=False, rug=True, label='Histogram w/o Density')
sns.utils.axlabel('Value', 'Frequency')
plt.title('Histogram of a Random Sample from a Normal Distribution')
plt.legend()
# 带有回归直线的散点图与单变量直方图 jointplot()
mean, cov = [5, 10],[(1, .5),(.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
data_frame = pd.DataFrame(data, columns=['x', 'y'])
sns.jointplot(x='x', y='y', data=data_frame, kind='reg').set_axis_labels('x','y')
plt.suptitle('Joint Plot of Two Variables with Bivariate and Univariate Graphs')
# 成对变量之间的散点图与单变量直方图 pairplot()
iris = sns.load_dataset('tips')
sns.pairplot(iris)
# 按照某几个变量生成的箱线图 factotplot()
tips = sns.load_dataset('tips')
sns.factorplot(x='time',y='total_bill',hue='smoker',col='day',data=tips,kind='box',size=4,aspect=.5)
# 带有bootstrap置信区间的线性回归模型
sns.lmplot(x='total_bill',y='tip',data=tips)
# 带有bootstrap置信区间的逻辑斯蒂回归模型
plt.show()
#----------------------------------------------------------------


#========seaborn========================================================
# 在matplotlib基础上开发 支持numpy pandas的数据结构 集成了scipy和statsmodels中的统计程序
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


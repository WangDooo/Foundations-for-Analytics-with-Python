#================================================================
# 使用统计图和摘要统计量对数据集进行探索和摘要分析，如何使用多元线性回归和逻辑斯蒂回顾进行回归和分类分析。
# 使用pandas 和 statasmodels 生成标准的描述性统计量和模型
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 描述性统计 计算出每列的总体描述性统计量、质量列中的唯一值及和这个唯一值对应的观测数量。
#----------------------------------------------------------------
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import statsmodels.api as sm 
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm 

# 数据读到pandas数据框中
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ','_')
# print(wine.head())
# # 显示所有变量的描述性统计量
# print(wine.describe())
# # 找出唯一值
# print(sorted(wine.quality.unique()))
# # 计算值的频率
# print(wine.quality.value_counts())
#----------------------------------------------------------------


#======分组、直方图和t检验==========================================================
# 分别分析红、白葡萄酒数据
#----------------------------------------------------------------
# # 按照葡萄酒类型显示质量的描述性统计量
# print(wine.groupby('type')[['quality']].describe().unstack('type')) # groupby()使用type列中的两个值将数据分两组。unstack()排列方式改变
# # 按照葡萄酒类型显示质量的特定分位数值
# print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
# # 按照葡萄酒类型查看质量分布
# red_wine = wine.loc[wine['type']=='red', 'quality']
# white_wine = wine.loc[wine['type']=='white', 'quality']
# sns.set_style('dark')
# sns.distplot(red_wine, norm_hist=True, kde=False, color='red', label='Red wine')
# sns.distplot(white_wine, norm_hist=True, kde=False, color='white', label='White wine')
# sns.utils.axlabel("Quality Score", "Density")
# plt.title("Distribution of Quality by Wine Type")
# plt.legend()
# plt.show()
# # 检验红白葡萄酒的平均质量是否有所不同
# print(wine.groupby(['type'])[['quality']].agg(['std']))
# # t检验
# tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
# print('tstat: %.3f pvalue: %.4f' % (tstat, pvalue))
#----------------------------------------------------------------


#=========成对变量之间的关系和相关性=======================================================
# 研究一下输入变量，计算输入变量两两之间的相关性，为输入变量创建带有回归直线的散点图
#----------------------------------------------------------------
# # 计算所有变量的相关矩阵
# print(wine.corr()) # corr()计算数据集中所有变量两两之间的线性相关性	
# # 从数据中取出一个“小”样本进行绘图
# def take_sample(data_frame, replace=False, n=200):
# 	return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]

# reds_sample = take_sample(wine.loc[wine['type']=='red',:])
# whites_sample = take_sample(wine.loc[wine['type']=='white',:])
# wine_sample = pd.concat([reds_sample, whites_sample])
# # wine数据中创建一个新列in_sample 用isin()进行填充 在抽样中为1
# wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
# print(pd.crosstab(wine.in_sample, wine.type, margins=True)) # crosstab 确定sample数目
# # 查看成对变量之间的关系
# sns.set_style('dark')
# g = sns.pairplot(wine_sample, kind='reg', plot_kws={'ci':False, 'x_jitter':0.25, 'y_jitter':0.25}, hue='type', diag_kind='hist', diag_kws={"bins":10, "alpha":1.0}, palette=dict(red="red", white="white"), markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
# print(g)
# plt.suptitle('Hist and Scatter', fontsize=15, horizontalalignment='center', verticalalignment='top', x=0.5, y=0.999)
# plt.show()
#---------------------------------------------------------------- 


#========使用最小二乘估计进行线性回归========================================================
# 测量出每个自变量在其他自变量不变时与因变量之间的关系
# y[i] ~ N(u[i],sigma^2)
# u[i] = b[0]+b[1]*x[i1]+b[2]*x[i2]+...+b[p]*x[ip]
# 使用statsmodel包进行线性回归
#----------------------------------------------------------------
# 波浪线~ 左侧 quality是因变量，右侧是自变量
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
# 拟合一个普通最小二乘回归模型
lm = ols(my_formula, data=wine).fit()
print(lm.summary()) # 摘要信息
#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------

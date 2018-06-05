#========linalg========================================================
# linalg 所有基本线性代数运算函数
# 线性方程组 linalg.solve
# x + 2y + 3z = 3
# 2x + 3y + z = -10
# 5x - y + 2z = 14
#----------------------------------------------------------------
# from numpy import array
# from scipy import linalg
# A = array([[1,2,3],[2,3,1],[5,-1,2]])
# b = array([[3],[-10],[14]])
# solution = linalg.solve(A,b)
# print(solution)
#----------------------------------------------------------------


#=======最小二乘回归=========================================================
# linalg.lstsq y = Xb + e
# y-因变量的向量 X-自变量的系数矩阵 b-要进行估计的解向量 e-从数据中计算出的残差向量
# linalg.lstsq函数使用系数矩阵X和因变量y求解出解向量b
#----------------------------------------------------------------
# import numpy as np 
# from scipy import linalg
# c1, c2 = 6.0, 3.0
# i = np.r_[1:21]
# xi = 0.1*i
# yi = c1*np.exp(-xi) + c2*xi # yi 加一些随机扰动
# zi = yi + 0.05*np.max(yi)*np.random.randn(len(yi))
# A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]
# c, resid, rank, sigma = linalg.lstsq(A, zi)
# print(c)
#----------------------------------------------------------------


#========interpolate========================================================
# 已知数据点之间进行线性插值和曲线插值的功能 
# 单变量数据 interp1d 多变量数据 griddata
# 样条插值 径向基函数 对数据进行平滑和插值
#----------------------------------------------------------------
# from numpy import arange, exp
# from scipy import interpolate
# import matplotlib.pyplot as plt 

# x = arange(0, 20)
# y = exp(-x/4.5)
# # interp1d函数接受两个数组为参数，返回一个函数对象，使用插值法找出新数据点的值
# interpolate_function = interpolate.interp1d(x, y)
# new_x = arange(0, 19, 0.1)
# new_y = interpolate_function(new_x)
# plt.plot(x,y,'o',new_x,new_y,'-')
# plt.show()
#----------------------------------------------------------------


#=======stats=========================================================
# stats 分布求值 计算描述性统计量 统计检验 回归分析
# 描述性统计量
#----------------------------------------------------------------
# from scipy.stats import norm, describe
# # 创建一个数组，从一个均值为5标准差为2的正态分布中提取1000个值。
# x = norm.rvs(loc=5, scale=2, size=1000)
# print(x.mean())
# print(x.min())
# print(x.max())
# print(x.var()) # 方差
# print(x.std()) # 标准差
# x_nobs, (x_min, x_max), x_mean, x_variance, x_skewness, x_kurtosis = describe(x)
# print(x_nobs, x_mean)

#----------------------------------------------------------------


#========线性回归========================================================
# 估计斜率、截距 linregress 返回相关系数
#----------------------------------------------------------------
# from numpy.random import random
# from scipy import stats
# x = random(20)
# y = random(20)
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
# print('R-squarrd:', round(r_value**2, 4))
# print(slope)
#----------------------------------------------------------------


import matplotlib
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter    #用于设置坐标轴

#Reference: http://www.cnblogs.com/kemaswill/archive/2012/12/07/2807963.html

#1、plot and scatter

# year=[1995,2000,2005,2010]
# pop=[1.5,2.5,4,9]
#
# plt.plot(year,pop)   #to plot the line fighre
# plt.show()
# plt.scatter(year,pop)
# plt.show()           #to plot the point fighre



#2、 process the x-axis or y x-axis
#year=list(range(1999,2017))
#gdp=[631.94,664.16,695.15,694.00,717.85,816,892.83,925.1,986.02,1095.43,1163.08,1360.56,1583.04,1667.88,1784.62,1777.18,1832.91,1965.18]
# plt.scatter(year,gdp)
# plt.xlabel('Year')   #add label for x-axis,the same as y-axis
# plt.ylabel('GDP (Agrarian)')




#3、histograms:直方图(distribution)
# life_exp=[43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.33800000000002, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.38800000000001, 60.916, 70.19800000000001, 82.208, 73.33800000000002, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000002, 71.993, 42.592, 45.678, 73.952, 59.44300000000001, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.90600000000001, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999998, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000002, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.56800000000001, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000002, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]
# #bin表示一共有几个柱子，density表示概率密度，概率密度默认为1
# plt.hist(life_exp,bins=25,orientation='horizontal',color='blue',density=1)
# plt.xlabel('life_exp')
#Finally, show the plot
#plt.show()



#4、
#import ticker里的multipleLocator和FormatStrFormatter
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

year=np.array(range(1999,2017))
print(year)
gdp=np.array([631.94,664.16,695.15,694.00,717.85,816,892.83,925.1,986.02,1095.43,1163.08,1360.56,1583.04,1667.88,1784.62,1777.18,1832.91,1965.18])
print(gdp)
plt.figure(1)
ax1=plt.subplot2grid((1,1),(0,0),colspan=2)    #subplot2grid类似于“pyplot.subplot”，但是它从0开始索引
plt.scatter(year,gdp,s=gdp,c='#FFDAB9',alpha=0.5,label='output')

#写坐标
plt.axis([1998,2017,500,2100])
plt.xlabel('Year')
plt.ylabel('Output')
plt.title('Output of Shanghai Agrarian')

#设置坐标格式精度
xmajorlocator = MultipleLocator(5) #将x主刻度标签设置为5的倍数
xmajorformatter = FormatStrFormatter('%4d') #设置x轴标签文本的格式  
xminorlocator = MultipleLocator(1) #将x次刻度标签设置为1的倍数

#设置主刻度标签的位置,标签文本的格式
ax1.xaxis.set_major_locator(xmajorlocator)
ax1.xaxis.set_major_formatter(xmajorformatter)

#显示次刻度标签的位置,没有标签文本
ax1.xaxis.set_minor_locator(xminorlocator)
ax1.xaxis.grid(True) #x坐标轴的网格使用主刻度
ax1.yaxis.grid(True)

#添加文字说明
#这里使用numpy的array以实现文字说明和点图配合，变换位置的效果
for i in range(1999,2018,4):
   plt.text(i,gdp[year==i],gdp[year==i][0],color='#FF6A6A')
#添加注释:被注释的地方xy(x, y)和插入文本的地方xytext(x, y)
plt.annotate('Constantly boomed',xy=(2006,1200),xytext=(2003,1500),
             arrowprops=dict(facecolor='black', shrink=0.01),)#箭头的方向和xy及xytext有关
#增加说明
#plt.legend(loc='upperleft')

#用线图为特定点增加注释
plt.plot([2005,2005],[0,800],color='k',linewidth=2,linestyle='-.') #s意思是线的size

#show
plt.show()





#5 hist、画板、板中画
#numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。
#关于numpy模块的随机数可以参考：https://blog.csdn.net/kancy110/article/details/69665164

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

#创建画板1（fighre（1）），并在画板使用.add_subplot()创建画纸1
#还有另一种方法叫做.add_axes().ref：https://www.zhihu.com/question/51745620
fig=plt.figure(1)
ax1=fig.add_subplot(2,1,1)

#为x,y轴命名，添加title
plt.xlabel('Distribution')
plt.ylabel('probability')
plt.title('Histogram of normal')

#添加文字
plt.text(60,0.025,r'ASD')

#plt.axis([a,b,c,d])定制坐标轴,a,b为横坐标开始结束，c,d为纵坐标开始结束
plt.axis([25,175,0,0.03])

#创立概率分布柱形图，bins为柱子数量，alpha为透明度，facecolor为颜色
plt.hist(x,bins=50,density=1,facecolor='g',alpha=0.75)
plt.grid(True)

#plt.show()

#还有另一种方法叫做.axes().   
#输入数据
dt=0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000]/0.05) # impulse response
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)]*dt # colored noise

#创建第二块画板的主画
ax2=plt.figure(2)

#画图
plt.plot(t,s)

#x,y轴的范围，定制坐标轴
plt.axis=plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])

#为x,y轴命名，添加title
plt.xlabel('time (s)')
plt.ylabel('current (nA)')
plt.title('Gaussian colored noise')

#内嵌图
ax2_1=plt.axes([.65, .6, .2, .2], facecolor='y')
n, bins, patches = plt.hist(s, 400, density=1)
plt.title('Probability')
plt.xticks([])
plt.yticks([])

#第二个内嵌图
a = plt.axes([0.2, 0.6, .2, .2], facecolor='y')
plt.plot(t[:len(r)], r)
plt.title('Impulse response')
plt.xlim(0, 0.2)
plt.xticks([])
plt.yticks([])
plt.show()
'''



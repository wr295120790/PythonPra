import matplotlib.pyplot as plt
from random import randint

squares = [1,3,4,10,21,26,66,77]
squares01 = [2,4,6,8,10,22,24,25]
seq=[1,2,3,4,5,6,7,8]
#1、制作折线图
linsqua, = plt.plot(seq,squares,'-*',label='Num1')
linsquas, = plt.plot(seq,squares01,'-o',label='Num2')
plt.xticks(seq)
#plt.plot(seq,squares,seq,squares01,linewidth=3) #linewidth参数是线条多粗
plt.legend(handles=[linsqua,linsquas],loc='best')
#plt.axis([0,8,0,80]) #axis设定x,y轴最大和最小
plt.title('Test Char') #图表名称
plt.xlabel('x Xhou') #X轴名称
plt.ylabel('y Yzhou') #Y轴名称
plt.tick_params(axis='both',labelsize=12,color='r')
#savefig中第一个参数是文件名，第二个参数是将图片以外多余的空间删除
plt.savefig('ceshi.jpg',bbox_inches='tight') #保存查询出来的图片
plt.show()

#2、制作散点图
xsca=[1,3,5,7,9]
ysca=[11,13,15,17,19]
plt.scatter(xsca,ysca,color='r')
plt.show()

#3、绘制波形
import numpy as np
xpt=np.linspace(0,10,500)
ypt1=np.sin(xpt)
ypt2=np.cos(xpt)
plt.scatter(xpt,ypt1,cmap='rainbow')
plt.scatter(xpt, ypt2)
plt.show()

#4、随机数的应用
num=100
while True:
    x=np.random.random(100)
    y=np.random.random(100)
    t=x     #色彩随x轴变化
    plt.scatter(x, y,s=100,c=t,cmap='brg')
    plt.show()
    yrn = input('是否继续?(y/n)')
    if yrn == 'n' or yrn == 'y':
        break

#5、制作多个图表
squares = [1,3,4,10,21,26,66,77]
squares01 = [2,4,6,8,10,22,24,25]
seq=[1,2,3,4,5,6,7,8]
plt.figure(1)
plt.plot(seq,squares,'-*')
plt.figure(2)
plt.plot(seq,squares01,'-o')
plt.title('Text Char')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')
plt.show()

#6、含有子图的图表
squares = [1,3,4,10,21,26,66,77]
squares01 = [2,4,6,8,10,22,24,25]
seq=[1,2,3,4,5,6,7,8]
plt.subplot(2,1,1) #如果要左右的话1,2,1
plt.plot(seq,squares,'-*')
plt.subplot(2,1,2)
plt.plot(seq,squares01,'-o')
plt.show()

#7、直方图的制作
votes=[135,222,89]
N=len(votes) #计算长度
x=np.arange(N) #直方图X坐标
width=0.35 #直方图宽度
plt.bar(x,votes,width) #绘制直方图

plt.ylabel('The Y')
plt.title('Text Char')
plt.xticks(x,('jin','liu','wang'))
plt.yticks(np.arange(0,300,30))
plt.show()

#8、csv文件绘制图表
import csv

fn='练习文件/天气变化.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)
    hight,lower=[],[]
    for row in csvReader:
        hight.append(row[1])
        lower.append(row[3])
print('最高温：',hight)
print('最低温：',lower)        
for i,header in enumerate(headerRow):  #列出文件的标题  
    print(i,header)

plt.plot(hight)
plt.title('Weather')
plt.xlabel('',fontsize=14)
plt.ylabel('Temoer',fontsize=14)
plt.tick_params(axis='both',labelsize=12,color='r')
plt.figure(dpi=80,figsize=(12,30)) #
plt.show()    




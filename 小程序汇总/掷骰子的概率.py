from random import randint
import numpy as np
import matplotlib.pyplot as plt

def dice_generator(times,sides):
    #处理随机数
    for i in range(times):
        ranNum=randint(1,sides) #产生1-6的随机数
        dice.append(ranNum)
def dice_count(sides):
    #计算1-6出现的次数
    for i in range(1,sides+1):
        frequency=dice.count(i) #计算i出现dicp列表的次数
        frequencies.append(frequency)

times =600 #投骰子的次数
sides = 6 #骰子的面数
dice =[] #建立骰子列表
frequencies = [] # 存储每面骰子出现的次数
dice_generator(times, sides) #产生投骰子的列表
dice_count(sides) #将骰子列表转成次数列表
x=np.arange(6)
width = 0.35
plt.bar(x, frequencies,width,color='g')
plt.ylabel('Freque')
plt.title('Test Char')
plt.xticks(x,('1','2','3','4','5','6'))
plt.yticks(np.arange(0,150,15))
plt.show()
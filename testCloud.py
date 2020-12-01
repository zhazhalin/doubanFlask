#-*- coding = utf-8 -*-
#@Time : 2020/7/29 
#@Author:张家林
#@File : testCloud.py
#@Software:{PyCharm}

import jieba   #分词
from matplotlib import pyplot as plt    #绘图， 数据可视化
from wordcloud import   WordCloud         #词云
from PIL import Image                  #图片处理
import numpy as np                       #矩阵运算
import sqlite3                        #数据库

list=""
conn=sqlite3.connect("豆瓣top250.db")
cur=conn.cursor()
sql="select instroduction from movie "
data=cur.execute(sql)
for item in data:
    list=list+item[0]
# print(list)

cut=jieba.cut(list)
string=' '.join(cut)
# print(string)

img=Image.open(r'venv/timg.jpg')
image_array=np.array(img)    #将图片转换成数组
wc= WordCloud (
    background_color='white',
    mask=image_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(string)
#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')  #是否显示坐标轴
# plt.show()      #显示图片
plt.savefig(r'D:\DeskTop\img.jpg',dpi=500)

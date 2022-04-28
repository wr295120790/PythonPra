#图表练习-饼图
import openpyxl
from openpyxl.chart import PieChart,Reference#图形包

wb2=openpyxl.Workbook()
ws2=wb2.active
row = [
    ['姓名','性别','年龄'],
    ['刘安珂','女',26],
    ['金晶','女',28],
    ['刘亦菲','女',35]
    ]
for name in row:
    ws2.append(name)
print('插入数据成功')    

chart =PieChart()
chart.title='人名详情'
#min_col,max_col这两个参数是列
#min_row,max_row这两个参数是行
data=Reference(ws2,min_col=3,max_col=3,min_row=1,max_row=5)
chart.add_data(data,titles_from_data=True)
xtitle=Reference(ws2,min_col=1,min_row=2,max_row=5)
chart.set_categories(xtitle)
ws2.add_chart(chart,'E1')
wb2.save('人名饼图.xlsx')
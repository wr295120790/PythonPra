import csv

fn='练习文件/UCM_USER.csv'
with open(fn,'w',newline='',encoding='UTF-8') as csvFile:
    csvWriter=csv.writer(csvFile)
    csvWriter.writerow(['姓名','年龄','性别'])
    csvWriter.writerow(['刘亦菲','35','女'])
    csvWriter.writerow(['刘安珂','26','女'])
    csvWriter.writerow(['金晶','28','女'])
    csvWriter.writerow(['夏千姿','26','女'])
    
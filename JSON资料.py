import json

listNum=[2,4,8,6,10]
tupleNum=(1,3,5,7,9)
listObject=[{'a':'成龙','c':70,'b':'男'}]
dicObj= {"a":10, "c":70, "b":30 }
json01='{"a":10, "c":70, "b":30 }'
jsonData01=json.dumps(listNum)
jsonData02=json.dumps(tupleNum)
dict01=json.loads(json01)
#sort_keys可以将转换呈json格式的对象进行排序
#indent可以对json格式进行缩排，更容易查看
jsonData03=json.dumps(listObject,sort_keys=True,indent=4) 
print('列表转换成json数据：',jsonData01)
print('元组转换成json数据：',jsonData02)
print('列表转换成json数据：',jsonData03)
print('json数组在Python的数据类型',type(jsonData01))
print('将json数据转换成Python对象：',dict01)
#将json文件进行存储
fn='jsonP.json'
with open(fn,'w') as fnObj:
    json.dump(dicObj, fnObj)  
print('保存文件成功')
with open(fn,'r') as fnrea:
    data=json.load(fnrea)
print('使用load读取文件',data)




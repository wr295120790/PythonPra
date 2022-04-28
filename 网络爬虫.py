import webbrowser
import requests
import re


head = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) appleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
}

#打开浏览器
url=webbrowser.open('https://www.baidu.com')
url1= 'https://www.baidu.com'
#判断是否获取到网页
htmlFile=requests.get(url1)
htmlFile.encoding = htmlFile.apparent_encoding
print('获取网页内容',htmlFile.text)
print(htmlFile.encoding)
if htmlFile.status_code == requests.codes.ok:
    pattern=input('请输出需要查询的字符串：')
#使用方法1    
    if pattern in htmlFile.text:
        print('搜寻 %s 成功'% pattern)
    else:
        print('搜寻 %s 失败'% pattern)
#使用方法2
    name = re.findall(pattern,htmlFile.text)
    if name != None:
        print('%s 出现 %d 次'% (pattern,len(name)))            
    else:
        print('%s 出现 0 次'% pattern)
else:
    print('网页下载失败')          
print('获取网页的大小:',len(htmlFile.text))

fn = 'baidu.txt'
with open(fn,'wb') as file_obj:
    for diskStorage in htmlFile.iter_content(10240):
        size=file_obj.write(diskStorage)
        print(size)
    print('以 %s 存储网页HTML文件成功'% fn) 

#解析网页使用BeautifulSoup模块
import bs4

htmlFile = open('练习文件/练习文件.html',encoding='utf-8')
objSoup=bs4.BeautifulSoup(htmlFile,'lxml')
print('打印BeautifulSoup对象数据类型：',type(objSoup))
print('打印title =',objSoup.title.text)

objTag=objSoup.find('title')
print('Tag内容:',objTag.text)

objTagAll=objSoup.find_all('title')
for data in objTagAll:
    print(data.text)

objTag1=objSoup.select('body')  
print('搜寻body标签下的所有数据：',objTag1)

objTag2=objSoup.select('body div p')  
print('搜寻body标签下div中的<p>的所有数据：',objTag2[3].getText())

objTag_img=objSoup.select('img')  
print('搜寻img标签下的所有数据：',objTag_img)

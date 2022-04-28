import bs4,requests,os

header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) appleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
}
'''
param = {
        'tn':'resultjson_com',
        'logid':'3675020956928247336',
        'ipn': 'rj',
        'ct': '201326592',
        'is' :'',
        'fp': 'result',
        'fr':'',
        'word': '刘亦菲',
        'cg': 'star',
        'queryWord': '刘亦菲',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid':'',
        'st': '-1',
        'z':'',
        'ic':'0',
        'hd':'',
        'latest':'',
        'copyright':'',
        's':'',
        'se':'',
        'tab':'',
        'width':'',
        'height':'',
        'face': '0',
        'istype': '2',
        'qc':'',
        'nc': '1',
        'expermode':'',
        'nojc':'',
        'isAsync':'',
        'pn': '90',
        'rn': '30',
        'gsm': '5a',
        '1650876092902':'',
        }
'''
'''url='https://image.baidu.com/search/acjson?'''
url='http://www.grandtech.info/'
#html=requests.get(url=url, headers=header, params=param)
html=requests.get(url)
print('图片下载中....')
html.raise_for_status()
print('网页下载完成')

destDir='/Users/wangrui/Desktop/Python练习汇总文档/练习文件/图片'
if os.path.exists(destDir) == False:
    os.makedirs(destDir)

objSoup = bs4.BeautifulSoup(html.text,'lxml')

imgTag=objSoup.select('img')
print('搜索到的图片数量 = ',len(imgTag))
print(imgTag)
if len(imgTag) > 0:
    for i in range(len(imgTag)):
        imgUrl=imgTag[i].get('src')
        print('%s 图片下载中 ...'% imgUrl)
        findUrl = url + imgUrl
        print('%s 图片下载中 ...'% findUrl)
        picture = requests.get(findUrl)
        #picture.raise_for_status()
        print('%s 图片下载成功'% findUrl)

        pictFile = open(os.path.join(destDir,os.path.basename(imgUrl)),'wb')
        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()    

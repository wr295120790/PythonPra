import requests
from lxml import etree
page = input('请输入要爬取多少页：')
page = int(page) + 1
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
n = 0
pn = 1
# pn是从第几张图片获取 百度图片下滑时默认一次性显示30张
for m in range(1, page):
    url = 'https://image.baidu.com/search/acjson?'

    param = {
        'tn': 'resultjson_com',
        'logid': '18394216480081385985',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'fr': 'ala',
        'word': '刘亦菲',
        'cg': 'star',
        'queryWord': '刘亦菲',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '',
        'istype': '',
        'qc': '',
        'nc': '',
        'expermode': '',
        'nojc': '',
        'isAsync': '',
        'pn':pn,
        'rn': '30',
        'gsm': '5a',
        '1650942734004': ''
    }
    page_text = requests.get(url=url, headers=header, params=param)
    page_text.encoding = 'utf-8'
    page_text = page_text.json()
#先取出所有链接所在的字典，并将其存储在一个列表当中
    info_list = page_text['data']
#由于利用此方式取出的字典最后一个为空，所以删除列表中最后一个元素
    del info_list[-1]
#定义一个存储图片地址的列表
    img_path_list = []
    for info in info_list:
        img_path_list.append(info['thumbURL'])
#再将所有的图片地址取出，进行下载
#n将作为图片的名字
    for img_path in img_path_list:
        img_data = requests.get(url=img_path, headers=header).content
        img_path = './' + str(n) + '.jpg'
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        n = n + 1

    pn += 29

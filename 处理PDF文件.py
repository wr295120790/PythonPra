import PyPDF2

pdf_name = '练习文件/刘亦菲简介.pdf'
pdfobj = open(pdf_name,'rb')
#获取页数
pdfRd = PyPDF2.PdfFileReader(pdfobj)
print('PDF的页数 =',pdfRd.numPages)
#获取内容,中文会出现乱码
pageobj = pdfRd.getPage(0)
txt = pageobj.extractText()
print(txt)

def encrypt(fn):
    #检查文件是否加密
    pdfobj1 = open(pdf_name,'rb')
    pdfRd1 = PyPDF2.PdfFileReader(pdfobj1)
    if pdfRd1.isEncrypted:
        print('%s 文件有加密'% fn)
        '''if pdfRd1.decrypt('88888888'):
            pageobj1 = pdfRd1.getPage(0)
            txt1 = pageobj1.extractText()
            print('*************解密成功********')
            print(txt1)
        else:
            print('解密失败')'''#PDF2版本问题    
    else:
        print('%s 文件没有加密'% fn)

encrypt('练习文件/刘亦菲简介.pdf')        








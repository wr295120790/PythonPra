from selenium import webdriver

brower=webdriver.Chrome()
brower.get('https://www.baidu.com/')
print('webdriver对象类型：',type(brower))

try:
    head01=brower.find_element_by_id('s_is_result_css')
    print(head01.tag_name)
except:    
    print('没找到相符的元素')

try:
    head02=brower.find_elements_by_id('s_is_result_css')
    print(head02.tag_name)
except:    
    print('没找到相符的元素')    

try:
    head03=brower.find_element_by_name('title')
    print(head03.tag_name)
except:    
    print('没找到相符的元素') 

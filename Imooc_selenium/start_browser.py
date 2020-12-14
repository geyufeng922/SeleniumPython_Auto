#coding=utf-8
import time
import random
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from util.ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
# driver=webdriver.Ie()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))
email_element=driver.find_element_by_id("register_email")
email_element.send_keys('sdfsd')
driver.find_element_by_id('captcha_code').send_keys("test")
print(driver.find_element_by_id('register_email-error').text)
print(driver.find_element_by_id('register_email-error').get_attribute('value'))
# driver.save_screenshot("E:/imooc2.png")
# code_element=driver.find_element_by_id("getcode_num")
# print(code_element.location)#{"x":123,"y":345}
# left=code_element.location['x']*1.25
# top=code_element.location['y']*1.25
# right=code_element.size['width']*1.25+left
# height=code_element.size['height']*1.25+top
# im=Image.open("E:/imooc2.png")
# img=im.crop((left,top,right,height))
# img.save("E:/imooc3.png")
#
# r = ShowapiRequest("http://route.showapi.com/184-4","451433","14410a0d29ea4c62858bb3f07c7f3767" )
# r.addBodyPara("typeId", "35")
# r.addBodyPara("convert_to_jpg", "0")
# r.addFilePara("image","E:/imooc3.png")
# res = r.post()
# text=res.json()['showapi_res_body']['Result']
# print(text) #返回信息
# time.sleep(3)
# driver.find_element_by_id('captcha_code').send_keys(text)

# for i in range(5):
#     user_email=''.join(random.sample('1234466789qwerttt',5))+"@163.com"
#     print(user_email)
element=driver.find_element_by_class_name("controls")
locator=(By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
print(email_element.get_attribute("placeholder"))
email_element.send_keys("test@163.com")
print(email_element.get_attribute("value"))
time.sleep(5)
driver.close()
# driver.find_element_by_id("register_email").send_keys("1264586967@qq.com")
# user_name_element_node=driver.find_elements_by_class_name("controls")[1]
# user_element=user_name_element_node.find_element_by_class_name("form-control")
# user_element.send_keys("geyufeng")
# driver.find_element_by_name("password").send_keys("111111")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("1111111")
# driver.close()


#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
# image=Image.open("E:/imooc1.png")
# text=pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4","451433","14410a0d29ea4c62858bb3f07c7f3767" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image","E:/imooc1.png")
res = r.post()
text=res.json()['showapi_res_body']['Result']
print(text) #返回信息

















# coding=utf-8

# 给你的头像右上角加上数字达到示例图的类似效果

from PIL import Image,ImageDraw,ImageFont

def addNum(filePath):
     img = Image.open(filePath)
     size = img.size
     fontSize = size[1] / 4
     draw = ImageDraw.Draw(img)

     ttFont = ImageFont.truetype("simsun.ttc", fontSize)
     draw.text((fontSize, fontSize), "88","black", font=ttFont)
     del draw
     img.save('F:/PY/result.png')
     img.show()

print addNum("F:/PY/p.png")
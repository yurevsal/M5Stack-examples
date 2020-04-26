from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222) #set backgrondColor RRGGBB

#lcd.qrcode('Hello world', 72, 32, 176) #lcd.qrcode(message, x, y, size)

title0 = M5Title(title="Title_001", x=12 , fgcolor=0x00d5ff, bgcolor=0x4f4f4f)#titleBar

image = M5Img(111, 56, "res/default.jpg", True) #M5Img(x, y, imgPath, visible)

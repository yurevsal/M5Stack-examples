from m5stack import *
from m5ui import *
from uiflow import *

lcd.setRotation(1)
lcd.setBrightness(100)
setScreenColor(0x222222) #set backgrondColor RRGGBB

#lcd.qrcode('Hello world', 72, 32, 176) #lcd.qrcode(message, x, y, size)

title0 = M5Title(title="Title_001", x=12 , fgcolor=0x00d5ff, bgcolor=0x4f4f4f)#titleBar
title0.setTitle('My titleBar')
title0.hide()
title0.show()
title0.setFgColor(0xffffff)
title0.setBgColor(0x333333)

image = M5Img(111, 56, "res/default.jpg", True) #M5Img(x, y, imgPath, visible)

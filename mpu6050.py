from m5stack import *
from m5ui import *
from uiflow import *
import imu

setScreenColor(0x222222)



imu0 = imu.IMU()
rectangle0 = M5Rect(5, 29, 310, 205, 0x222222, 0xffffff)
label0 = M5TextBox(14, 60, "GyX: ", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
gx_label = M5TextBox(89, 59, "???", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
title0 = M5Title(title="MPU6050", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label2 = M5TextBox(13, 119, "GyY:", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label3 = M5TextBox(13, 180, "GyZ:", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
gy_label = M5TextBox(89, 120, "???", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
gz_label = M5TextBox(89, 180, "???", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)


while True:
  gx_label.setText(str(str((imu0.ypr[1]))))
  gy_label.setText(str(str((imu0.ypr[2]))))
  gz_label.setText(str(str((imu0.gyro[2]))))
  wait_ms(2)

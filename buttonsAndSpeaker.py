from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x0000ff)

freq = [600, 1000, 1800]
dur = 100
vol = 10

# Define button callback function
def buttonA_wasPressed():
  # freq: 20 ~ 20000(hz)
  # duration: 0 ~ 2000(ms)
  # volume: 0 ~ 100
  speaker.tone(freq[0], dur, vol)
def buttonB_wasPressed():
  speaker.tone(freq[1], dur, vol)
  
def buttonC_wasPressed():
  speaker.tone(freq[2], dur, vol)
  
btnA.wasPressed(buttonA_wasPressed)
btnB.wasPressed(buttonB_wasPressed)
btnC.wasPressed(buttonC_wasPressed)

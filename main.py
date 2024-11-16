import os, sys, io
import M5
from M5 import *
from hardware import *
from machine import Timer
import time
from unit import LaserTXUnit



UI_main = None
mode_hold = None
mode_click = None
mode_toggle = None
mode_spam = None
battery_100 = None
battery_80 = None
battery_60 = None
battery_40 = None
battery_20 = None
battery_0 = None
laser_tx_0 = None


mode = None
battery_level = None
screen_on = None
laser_on = None
last_update = None

battery_timer = Timer(0)

# Describe this function...
def switch_mode():
  global mode, battery_level, screen_on, laser_on, last_update, UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0
  mode = mode + 1
  mode_hold.setVisible(False)
  mode_click.setVisible(False)
  mode_toggle.setVisible(False)
  mode_spam.setVisible(False)
  if mode == 1:
    mode_click.setVisible(True)
  elif mode == 2:
    mode_toggle.setVisible(True)
  elif mode == 3:
    mode_spam.setVisible(True)
  else:
    mode_hold.setVisible(True)

# Describe this function...
def update_battery_sprite():
  global mode, battery_level, screen_on, laser_on, last_update, UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0
  battery_level = Power.getBatteryLevel()
  battery_100.setVisible(False)
  battery_80.setVisible(False)
  battery_60.setVisible(False)
  battery_40.setVisible(False)
  battery_20.setVisible(False)
  battery_0.setVisible(False)
  if battery_level > 79 and battery_level <= 100:
    battery_100.setVisible(True)
  elif battery_level > 59 and battery_level < 80:
    battery_80.setVisible(True)
  elif battery_level > 39 and battery_level < 60:
    battery_60.setVisible(True)
  elif battery_level > 19 and battery_level < 40:
    battery_40.setVisible(True)
  elif battery_level > 0 and battery_level < 20:
    battery_20.setVisible(True)
  else:
    battery_0.setVisible(True)
    
def update_battery_timer(timer):
    update_battery_sprite()
    
battery_timer.init(period=2000, mode=Timer.PERIODIC, callback=update_battery_timer)

# Describe this function...
def toggle_screen():
  global mode, battery_level, screen_on, laser_on, last_update, UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0
  screen_on = not screen_on
  if screen_on:
    Widgets.setBrightness(100)
  else:
    Widgets.setBrightness(0)

# Describe this function...
def mode_change():
  global mode, battery_level, screen_on, laser_on, last_update, UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0
  if mode >= 4:
    mode = 0


def btnPWR_wasClicked_event(state):
  global UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0, mode, battery_level, screen_on, laser_on, last_update
  toggle_screen()
  time.sleep(0.1)


def btnA_wasClicked_event(state):
  global UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0, mode, battery_level, screen_on, laser_on, last_update
  switch_mode()


def setup():
  global UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0, mode, battery_level, screen_on, laser_on, last_update

  M5.begin()
  UI_main = Widgets.Image("res/img/UI_main.png", 0, 0, scale_x=1, scale_y=1)
  mode_hold = Widgets.Image("res/img/UI-mini-hold.png", 52, 19, scale_x=1, scale_y=1)
  mode_click = Widgets.Image("res/img/UI-mini-click.png", 52, 19, scale_x=1, scale_y=1)
  mode_toggle = Widgets.Image("res/img/UI-mini-toggle.png", 52, 19, scale_x=1, scale_y=1)
  mode_spam = Widgets.Image("res/img/UI-mini-spam.png", 52, 19, scale_x=1, scale_y=1)
  battery_100 = Widgets.Image("res/img/UI-mini-100.png", 101, 0, scale_x=1, scale_y=1)
  battery_80 = Widgets.Image("res/img/UI-mini-80.png", 101, 0, scale_x=1, scale_y=1)
  battery_60 = Widgets.Image("res/img/UI-mini-60.png", 101, 0, scale_x=1, scale_y=1)
  battery_40 = Widgets.Image("res/img/UI-mini-40.png", 101, 0, scale_x=1, scale_y=1)
  battery_20 = Widgets.Image("res/img/UI-mini-20.png", 101, 0, scale_x=1, scale_y=1)
  battery_0 = Widgets.Image("res/img/UI-mini-0.png", 101, 0, scale_x=1, scale_y=1)

  BtnPWR.setCallback(type=BtnPWR.CB_TYPE.WAS_CLICKED, cb=btnPWR_wasClicked_event)
  BtnA.setCallback(type=BtnA.CB_TYPE.WAS_CLICKED, cb=btnA_wasClicked_event)

  laser_tx_0 = LaserTXUnit((33, 32), mode=1)
  laser_tx_0.off()
  mode = 0
  UI_main.setVisible(True)
  mode_hold.setVisible(True)
  update_battery_sprite()


def loop():
  global UI_main, mode_hold, mode_click, mode_toggle, mode_spam, battery_100, battery_80, battery_60, battery_40, battery_20, battery_0, laser_tx_0, mode, battery_level, screen_on, laser_on, last_update
  last_update = time.ticks_ms()
  while True:
    M5.update()
    if mode == 0:
      while BtnB.isPressed():
        laser_tx_0.on()
        M5.update()
        last_update = 0
      while BtnB.isReleased():
        laser_tx_0.off()
        M5.update()
        break
    elif mode == 1:
      while BtnB.wasPressed():
        laser_tx_0.on()
        time.sleep_ms(10)
        laser_tx_0.off()
        M5.update()
        break
    elif mode == 2:
      laser_on = False
      while True:
        M5.update()
        if BtnB.wasPressed():
          laser_on = not laser_on
          if laser_on:
            laser_tx_0.on()
          else:
            laser_tx_0.off()
        if mode != 2:
          break
    elif mode == 3:
      while BtnB.isPressed():
        if not (BtnB.isPressed()):
          break
        laser_tx_0.on()
        time.sleep_ms(10)
        laser_tx_0.off()
        time.sleep_ms(50)
        M5.update()

    mode_change()

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")

#!/usr/bin/python
"""
retropie_clcd.py
Author       : zzeromin, member of Raspberrypi Village
Creation Date: Oct 11, 2016
Blog         : http://rasplay.org, http://forums.rasplay.org/, https://zzeromin.tumblr.com/
Thanks to    : smyani, zerocool, GreatKStar

Free and open for all to use. But put credit where credit is due.

#Reference:
runcommand of Retorpie:  https://github.com/retropie/retropie-setup/wiki/runcommand
I2C_LCD_driver developed by: Denis Pleic ( https://gist.github.com/DenisFromHR/cc863375a6e19dce359d )
IP_Script Developed by: AndyPi ( http://andypi.co.uk/ )
lcdScroll Developed by: Eric Pavey ( https://bitbucket.org/AK_Eric/my-pi-projects/src/28302f8f5657599e29cb5d55573d192b9fa30265/Adafruit_CharLCDPlate/lcdScroll.py?at=master&fileviewer=file-view-default )

#Notice:
retropie_clcd.py require I2C_LCD_driver.py, lcdScroll.py

Small script written in Python for Retropie project (https://retropie.org.uk/) 
running on Raspberry Pi 2,3, which displays all neccessary info on a 16x2 LCD display
#Features:
1. Current date and time, IP address of eth0, wlan0
2. CPU temperature and speed
3. Emulation and ROM information
"""

import I2C_LCD_driver
import os
from sys import exit
from subprocess import *
from time import *
from datetime import datetime
from lcdScroll import Scroller

def run_cmd(cmd):
   # runs whatever is in the cmd variable in the terminal
   p = Popen(cmd, shell=True, stdout=PIPE)
   output = p.communicate()[0]
   return output

def get_cpu_temp():
   tempFile = open("/sys/class/thermal/thermal_zone0/temp")
   cpu_temp = tempFile.read()
   tempFile.close()
   return float(cpu_temp)/1000

def get_cpu_speed():
   tempFile = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
   cpu_speed = tempFile.read()
   tempFile.close()
   return float(cpu_speed)/1000

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()

#get ip address of eth0 connection
cmdeth = "ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"
#get ip address of wlan0 connection
cmd = "ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"
#cmd = "ip addr show wlan1 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"

old_Temp = new_Temp = get_cpu_temp()
old_Speed = new_Speed = get_cpu_speed()

mylcd.lcd_display_string("Welcome", 1, 5)
mylcd.lcd_display_string("RAS Console Pi", 2, 1)
sleep(5) # 5 sec delay
mylcd.lcd_clear()

mylcd.lcd_display_string("RPi Village", 1, 3)
mylcd.lcd_display_string("www.rasplay.org", 2, 1)
sleep(5) # 5 sec delay
mylcd.lcd_clear()

mylcd.lcd_display_string("cafe.naver.com/", 1, 1)
mylcd.lcd_display_string("raspigamer", 2, 3)
sleep(5) # 5 sec delay
mylcd.lcd_clear()

while 1:
   
   mylcd.lcd_clear()
   sec = 0
   while ( sec < 5 ) :
      # ip & date information
      ipaddr = run_cmd(cmd)

      # selection of wlan or eth address
      count = len(ipaddr)
      if count == 0 :
         ipaddr = run_cmd(cmdeth)

      ipaddr = ipaddr.replace("\n","")
      #print datetime.now().strftime( "%b %d  %H:%M:%S" )
      #print "IP " + str( ipaddr )
      mylcd.lcd_display_string( datetime.now().strftime( "%b %d  %H:%M:%S" ), 1, 0 )
      mylcd.lcd_display_string( "IP %s" %(ipaddr), 2, 0 )
      sec = sec + 1
      sleep(1)

   mylcd.lcd_clear()
   sec = 0
   while ( sec < 5 ) :
      # cpu Temp & Speed information
      new_Temp = get_cpu_temp()
      new_Speed = int( get_cpu_speed() )

      if old_Temp != new_Temp or old_Speed != new_Speed :
         old_Temp = new_Temp
         old_Speed = new_Speed
         #print "CPU Temp: " + str( new_Temp )
         #print "CPU Speed: " + str( new_Speed )
         mylcd.lcd_display_string( "CPU Temp: " + str( new_Temp ), 1, 0 )
         mylcd.lcd_display_string( "CPU Speed: " + str( new_Speed ), 2, 0 )
         sec = sec + 1  
         sleep(1)

   mylcd.lcd_clear()
   sec = 0
   while ( sec < 1 ) :
      # show system & rom file information

      try: 
         f = open('/dev/shm/runcommand.log', 'r')
#      except FileNotFoundError:
      except IOError:
         mylcd.lcd_display_string( "You should play", 1, 0 )
         mylcd.lcd_display_string( "a game first!!", 2, 0 )
         sleep(3)
         break
         pass
      else:
         system = f.readline()
         system = system.replace("\n","")
         systemMap = {
            "fba":"FinalBurn Alpha",
            "gba":"GameBoy Advance",
            "kodi":"KODI",
            "mame-mame4all":"MAME4ALL",
            "mame-advmame":"AdvanceMAME",
            "mame-libretro":"lr-MAME",
            "msx":"MSX",
            "nes":"Famicom",   # Nintendo Entertainment System
            "psp":"PSPortable",    # PlayStation Portable
            "psx":"Playstation",
            "ports":"Ports",
            "snes":"Super Famicom", # Super Nintendo Entertainment System
            "notice":"TURN OFF",
         }
         system = systemMap.get(system)
         mylcd.lcd_display_string( "%s" %(system), 1, 0	)
         rom = f.readline()
         rom = rom.replace("\n","")
         mylcd.lcd_display_string( "%s" %(rom), 2 )
         sleep(1)
         f.close()

         lines = rom
         wait = 0
         speed = 0.1

         # Create scroller instance:
         scroller = Scroller(lines=lines)

         while True :
            if wait < 10 :
               message = scroller.scroll()       
               mylcd.lcd_display_string( "%s" %(system), 1, 0 )
               mylcd.lcd_display_string( "%s" %(message), 2 )
               sleep(speed)
               wait = wait + 0.1
            else :
               break
         sec = sec + 1
         sleep(1)

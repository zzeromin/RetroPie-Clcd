# RetroPie-Clcd
Scrolling Game Title for RetroPie v4.0.2 using 16x2 CLCD on RAS Console-Pi

<img src="https://github.com/zzeromin/RetroPie-Clcd/blob/master/RetroPie-Clcd01.jpg" width="70%" height="70%">

## About
Small script written in Python for RetroPie project (https://retropie.org.uk/) 
running on Raspberry Pi 2,3, which displays all necessary info on a 16x2 CLCD display

## Features
* Current Date and Time, IP address of eth0, wlan0
* CPU Temperature and Speed
* Emulation and ROM information

## Youtube
* https://youtu.be/W6jqBTqPqjw
* https://youtu.be/5KBNl-k6-SA
* https://youtu.be/_7mxhkkjFqk

## Development Environment
* Raspberry Pi 2, 3
* RetroPie v4.0.2 and later
* 16x2 I2C Character LCD

## Install
First, you should install Scraper( https://github.com/retropie/retropie-setup/wiki/scraper )

Second, Install below:
<pre><code>cd /home/pi
git clone https://github.com/zzeromin/RetroPie-Clcd.git
cd /home/pi/RetroPie-Clcd/
chmod 755 10.CLCD.sh
sudo ./10.CLCD.sh
</code></pre>

## Check 
You should check your I2C address of 16x2 CLCD.
I saw two types of I2C LCD modules. Those are two address each other normally => 0x27 or 0x3f.

<pre><code>sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --</code></pre>

edit line #22 in I2C_LCD_driver.py 0x27 or 0x3f.

<pre><code>cd RetroPie-Clcd/
sudo nano I2C_LCD_driver.py

# LCD Address
ADDRESS = 0x27 # or 0x3f
</code></pre>

* Raspberry Pi I2C GPIO Pinout

![Alt text](https://i.imgur.com/WTPHzsf.png)

* http://forums.rasplay.org/topic/318/scrolling-game-title-for-retropie-v4-0-2-using-16x2-clcd-on-ras-console-pi

## Reference
* https://retropie.org.uk/forum/topic/5061/scrolling-game-title-using-16x2-clcd-on-ras-console-pi
* https://retropie.org.uk/forum/topic/2211/questions-about-runcommand-sh
* https://retropie.org.uk/forum/topic/3134/meet-the-retrog-update-17-8-paintjob-pics
* https://retropie.org.uk/forum/topic/3731/solved-variables-with-runcommand-onstart-sh
* https://github.com/retropie/retropie-setup/wiki/runcommand


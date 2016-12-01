## i2c_address.sh
# Title        : Automatic I2C Address Changer for RAS Console-Pi
# Author       : zerocool, member of raspigamer
# Creation Date: Dec 1, 2016
# Web          : http://cafe.naver.com/raspigamer
# Free and open for all to use. But put credit where credit is due.
#
# How to Setup : 
# cd /home/pi/RetroPie-Clcd/
# chmod 755 I2C_Address.sh
# sudo ./I2C_Address.sh

# I2C ADDRESS DETECT
I2C_DETECT=`i2cdetect -y 1 | grep '\-\-' | cut -d: -f2 | grep [0-9a-fA-F] | awk '{ i = 1; while (i <= NF) { if($i != "--") print $i; i++} }'`

I2C_ADDRESS="0x${I2C_DETECT}"

# Get value already installed
I2C_ADDRESS_PREV=`grep '^ADDRESS' /home/pi/RetroPie-Clcd/I2C_LCD_driver.py | cut -d= -f2 | sed 's/ //'`

# Change config and restart service when different value detect
if [ $I2C_ADDRESS != $I2C_ADDRESS_PREV ]
	then
		# Change config file
		sed -i "s/ADDRESS = 0x[0-9a-fA-F][0-9a-fA-F]/ADDRESS = ${I2C_ADDRESS}/" /home/pi/RetroPie-Clcd/I2C_LCD_driver.py

		# Restart CLCD Service
		systemctl restart clcd
fi

## 10.CLCD.sh
# Title        : Scrolling Game Title for Retropie v4.0.2 using 16x2 CLCD on RAS Console-Pi
# Author       : zzeromin, member of Raspberrypi Village & raspigamer
# Creation Date: Oct 28, 2016
# Blog         : http://rasplay.org, http://forums.rasplay.org/, https://zzeromin.tumblr.com/
# Thanks to    : smyani, zerocool, superstar
# Free and open for all to use. But put credit where credit is due.
#
# How to Setup : 
# cd /home/pi
# git clone https://github.com/zzeromin/RetroPie-Clcd.git
# cd /home/pi/RetroPie-Clcd/
# chmod 755 10.CLCD.sh
# sudo ./10.CLCD.sh

cd /home/pi/
git clone https://github.com/zzeromin/RetroPie-Clcd.git
cd RetroPie-Clcd/
cp runcommand-onstart.sh /opt/retropie/configs/all/
cp runcommand-onend.sh /opt/retropie/configs/all/
cp clcd.service /lib/systemd/system/
systemctl enable clcd
echo "CLCD Setup Complete."
echo "I2C Setup is Starting Now"
sleep 1
apt-get update
apt-get -y install python-smbus i2c-tools
echo "i2c-bcm2708" >> /etc/modules
echo "i2c-dev" >> /etc/modules
sed -i 's/#dtparam=i2c_arm/dtparam=i2c_arm/' /boot/config.txt
#echo "dtparam=i2c_arm=on" >> /boot/config.txt 
echo "I2C Setup Complete. Reboot after 3 Seconds."
sleep 3
reboot

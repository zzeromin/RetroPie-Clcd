#!/usr/bin/env bash
# added and modified by zzeromin, zerocool ( 2016-10-13 )
# special thanks to zerocool
# Reference:
# runcommand of Retorpie:  https://github.com/retropie/retropie-setup/wiki/runcommand
# basic script:  https://retropie.org.uk/forum/topic/3731/solved-variables-with-runcommand-onstart-sh/9
# edit and path: $ sudo nano /opt/retropie/configs/all/runcommand-onstart.sh

# get the system name
system=$1

# get the emulator name
emul=$2

# get the full path filename of the ROM
rom=$3

# rom_bn receives $rom excluding everything from the first char to the last slash '/'
rom_bn="${rom##*/}"

# rom_bn receives $rom_bn excluding everything from the last char to the first dot '.'
#rom_bn="${rom_bn%.*}"

# For English User
# Display Game name to EmulationStation and CLCD from same gamelist.xml
GAMELIST1="/home/pi/RetroPie/roms/${system}/gamelist.xml"
GAMELIST2="/home/pi/.emulationstation/gamelists/${system}/gamelist.xml"

# For 2Byte Language User(Korean, Japanese, etc..)
# Display Game name to EmulationStation from gamelist.xml(Korean Game name)
# Display Game name to CLCD from gamelist_en.xml(English Game name)
#GAMELIST1="/home/pi/RetroPie/roms/${system}/gamelist_en.xml"
#GAMELIST2="/home/pi/.emulationstation/gamelists/${system}/gamelist_en.xml"

if [ -f ${GAMELIST1} ]
then
GAMELIST=${GAMELIST1}
else
GAMELIST=${GAMELIST2}
fi

title=`grep -A1 "${rom_bn}" ${GAMELIST} | awk '{getline;print}' | awk 'BEGIN {FS="<name>"} {print $2}' | awk 'BEGIN {FS="</name>"} {print $1}'`

echo "$system" >&2
echo "$title" >&2
#echo "$rom_bn" >&2

autorun at systemstart:
    sudo nano /etc/rc.local
    add "sudo bash /home/pi/TaPFX-Dia/work/diashow.sh"

automount von USB Stick - https://wiki.ubuntuusers.de/USB-Datentr%C3%A4ger_automatisch_einbinden/
    sudo apt-get install autofs
    Einbinden von USB Stick mit ID:312C-632A mit vfat dateisystem
    neuer stick: herausfinden mit $sudo blkid -o list -w /dev/null 
    in /etc/auto.master die folgende zeile hinzufuegen
    /media /etc/auto.automnt
    in  /etc/auto.automnt die folgende zeile hinzufuegen
    usbstick -fstype=vfat,sync,uid=0,gid=46,umask=007 :/dev/disk/by-uuid/312C-632A
    Service neu starten mit sudo service autofs reload

instaliere python3
instaliere autofs
instaliere fbi
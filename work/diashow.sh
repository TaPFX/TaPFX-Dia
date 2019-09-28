#!/bin/bash
python3 /home/pi/TaPFX-Dia/work/autorotate.py
python3 /home/pi/TaPFX-Dia/work/dialistgen.py
fbi -a -t 5 --blend 0 -v --norandom -readahead -cachemem 200 -T 2  -list /home/pi/TaPFX-Dia/work/dialist.lst

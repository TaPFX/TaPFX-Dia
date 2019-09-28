import os
import random
from random import choice

#tapdia_dir = "/home/pi/tapdia/tap/"
tapdia_dir = "/media/usbstick/Stucke/"
sponsordia_dir = "/media/usbstick/Werbung/"
sponsorrate = 3
dialist_name = "/home/pi/TaPFX-Dia/work/dialist.lst"


taplist = os.listdir(tapdia_dir)
#print(taplist)

sponsorlist = os.listdir(sponsordia_dir)
#print(sponsorlist)

f= open(dialist_name,"w+")

dialist = {}
taplist_mixed = {}
exclude = []

taplist_t = list()
for k, entry in enumerate(taplist):
    if(entry.startswith(".")):
        continue
    else:
        taplist_t.append(entry)
taplist = taplist_t

sponsorlist_t = list()
for k, entry in enumerate(sponsorlist):
    if(entry.startswith(".")):
        continue
    else:
        sponsorlist_t.append(entry)
sponsorlist = sponsorlist_t

for item in range(0,len(taplist)):
    n = choice([i for i in range(0,len(taplist)) if i not in exclude])
    taplist_mixed[item] = taplist[n]
    exclude.extend([n])

sponsorlist_mixed = {}
exclude = []
for item in range(0,len(sponsorlist)):
    n = choice([i for i in range(0,len(sponsorlist)) if i not in exclude])
    sponsorlist_mixed[item] = sponsorlist[n]
    exclude.extend([n])


s=0
for m in taplist_mixed:
    f.write(tapdia_dir + taplist_mixed[m] + "\n")
    if m%sponsorrate == 0:
         f.write(sponsordia_dir + sponsorlist_mixed[s%len(sponsorlist)] + "\n")
         f.write(sponsordia_dir + sponsorlist_mixed[s%len(sponsorlist)] + "\n")
         f.write(sponsordia_dir + sponsorlist_mixed[s%len(sponsorlist)] + "\n")
         s = s+1

f.close() 

import os
import random
from random import choice

tapdia_dir = "./pic1"
sponsordia_dir = "./pic2"
sponsorrate = 4
dialist_name = "dialist.lst"


taplist = os.listdir(tapdia_dir)
#print(taplist)

sponsorlist = os.listdir(sponsordia_dir)
#print(sponsorlist)

f= open(dialist_name,"w+")

dialist = {}
taplist_mixed = {}
exclude = []

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
    f.write("./pic1/" + taplist_mixed[m] + "\n")
    if m%sponsorrate == 0:
         f.write("./pic2/" + sponsorlist_mixed[s%len(sponsorlist)] + "\n")
         s= s+1

f.close() 
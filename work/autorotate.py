# ---------------------------------------------------
# File:   autorotate.py
# Descr.: Rotates JPEG Pictures if they are 
#         Portrait Mode for the Dia Screen in tap
# Date:   26.09.2019
# Author: Tobias Disch
# ---------------------------------------------------

# import the Python Image processing Libraryn
from PIL import Image
import glob

# Path to the tap plays
tapdia_dir = "/media/usbstick/Stucke/*.jpg"
# tapdia_dir = "./Stucke_neu/*.jpg"
# Path to the advertising
sponsordia_dir = "/media/usbstick/Werbung/*.jpg"
#sponsordia_dir = "./2/*.jpg"

# List all files in the directorys
piclist = glob.glob(tapdia_dir)
piclist.extend(glob.glob(sponsordia_dir))

# run through all files in folders
for item in piclist:
    # controllfiles with "._" are not processed  
    if not item.startswith("._"):
        # open file from list
        pic = Image.open(item)
        # get pixle size
        width, height = pic.size
        print("File: ", item,"w: ", width," h: ", height)
        # if image is in portrait mode, 
        # the asect ratio is smaller then one,
        # because the width is smaler then the hight
        # --> the Picture is rotated and saved without compession
        if width/height < 1 :
            rotimage = pic.transpose(Image.ROTATE_270)
            rotimage.save(item ,"JPEG",quality=100)

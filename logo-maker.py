import numpy as np
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

h, w          = image.shape[:2]  # get height, weight of image
logo_w        = w / 6            # find logo width ( 6 logos in a row )
total_row     = h / logo_w       # find row number
total_mission = 6 * total_row    # find number of missions

print "\n##### INFO #####\n"
print "img height\t:", h
print "img width\t:", w
print "logo width\t:", logo_w
print "total row\t:", total_row
print "total mission\t:", total_mission
print "\n##### LOG #####\n"

# create ./out folder
newpath = r'./out' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

# generate logo files
for r in range(0, total_row): # loop each row
    for c in range(0, 6):   # loop each column
        # gen filename
        cur_mission = total_mission - (c+6*r)
        cur_fname   = "logo_%03d.jpg" % cur_mission

        # crop & save
        from_y  = logo_w * r
        to_y    = from_y + logo_w - 1
        from_x  = logo_w * c
        to_x    = from_x + logo_w - 1
        cropped = image[from_y:to_y, from_x:to_x]
        cv2.imwrite("./out/%s" % cur_fname, cropped)

        #print cur_fname,
        #print "%s-%s" % ( r, c ),
        print "%s:%s,%s:%s\t" % ( from_y, to_y, from_x, to_x ),
    print
print

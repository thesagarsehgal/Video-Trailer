import cv2
import csv

vidcap = cv2.VideoCapture('../../video1.mp4')
def format(value):
    return "%.3f" % value

import os
if("data" not in os.listdir(".")):
    os.mkdir("data")
if("video1" not in os.listdir("data")):
    os.mkdir("data/video1")
else:
    os.system("rm data/video1/*")


def getFrame(sec,fr):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    
    hasFrames,image = vidcap.read()
    if hasFrames:
        fr.append([str(count),"image"+str(count)+".jpg",format(sec)])
        cv2.imwrite("./data/video1/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames,fr
sec = 0.2
frameRate = 1.0 #//it will capture image in each 0.5 second
count=1
fr = [["S.No","Image name","time"]]
success,fr = getFrame(sec,fr)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success,fr = getFrame(sec,fr)

with open('./data/video1/frames.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(fr)
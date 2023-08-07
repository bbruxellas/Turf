###############################################################################
# RE: Code use to extract individual frames from a UAB video file
# DATE: Aug 2023
# Authors: R. Austin, B.Bruxellas
###############################################################################
import sys, os
import numpy
import cv2

### set the path to the video
video_file = "./video/DJI_202308021504_007_WaypointSandhillsTurf/DJI_20230802152044_0002_WP1.MP4"

### set the frame interval
frame_interval = 30

### Read the video from specified path
vidcap = cv2.VideoCapture(video_file)

### Create a subfolder to store the frames
base_dir = os.path.dirname(video_file)
export_dir = os.path.normpath(os.path.join(base_dir, 'frames'))

if not os.path.exists(export_dir):
    os.makedirs(export_dir)


### set a counter for the frames
frameCount = 0

#### loop through the video pulling frames
success, frame = vidcap.read()
while(success):
    success, frame = vidcap.read()
    frameCount += 1	

    if(frameCount % frame_interval == 0):											# capture ~ 1 frame per second
        ImgName = "F" + str(frameCount) + ".jpg"
        outImgName = os.path.normpath(os.path.join(export_dir, ImgName))
        cv2.imwrite(outImgName, frame) 

        frame_resize = cv2.resize(frame, (500, 282)) 
        cv2.imshow('frame',  frame_resize)
	

    if(frameCount%100 == 0):
        print("FrameCount" + str(frameCount))
	
    ### if you presss the escpe key, exit the program
    if cv2.waitKey(10) == 27:  
    	break

cv2.destroyAllWindows()
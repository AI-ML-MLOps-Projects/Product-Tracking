import cv2
from datetime import timezone
import datetime

'''
    read_video_stream defination
        this function will create instance for a particular video/ RTSP Stream/ Laptop Webcam
        url =0 repersants Webcam of any machine
'''
def read_video_stream(url = 0):
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(url) # static video
    return cap
FRAME_SELECTION = 20
def create_frames():
    # cap = read_video_stream("rtsp://admin:Admin@123@192.168.1.64:554/Streaming/channels/101")
    cap = read_video_stream("D:\Raman\workspace\Product-Tracking\Example_Videos\\20221216_111216.mp4")
    counter  = 0
    while(True):
        ret, frame = cap.read()
        cv2.imshow("Live Video", frame)
        counter += 1

        # if(cv2.waitKey(1) & 0xFF == ord('c')):
        if(counter % FRAME_SELECTION == 0):
            counter = 0
            path = "D:\Raman\workspace\Product-Tracking\\frames\\"
            label = "bag" + str(datetime.datetime.now(timezone.utc).replace(tzinfo=timezone.utc).timestamp() *1000).split('.')[0] + ".JPEG"
            file_name = path + label
            cv2.imwrite(file_name, frame)
            
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            cap.release()
            cv2.destroyAllWindows()

create_frames()


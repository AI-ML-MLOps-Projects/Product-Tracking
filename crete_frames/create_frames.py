import cv2
from datetime import timezone
import datetime

def create_video_instance(url = 0):
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(url) # static video
    return cap

def create_frames():
    cap = create_video_instance("rtsp://admin:Admin@123@192.168.1.64:554/Streaming/channels/101")
    # cap = create_video_instance("./Example Videos/20221216_105329.mp4")
    while(True):
        ret, frame = cap.read()
        cv2.imshow("Live Video", frame)
        
        if(cv2.waitKey(1) & 0xFF == ord('c')):
            path = "frames\\"
            label = "bag" + str(datetime.datetime.now(timezone.utc).replace(tzinfo=timezone.utc).timestamp() *1000).split('.')[0] + ".jpg"
            file_name = path + label
            cv2.imwrite(file_name, frame)
            
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            cap.release()
            cv2.destroyAllWindows()

create_frames()


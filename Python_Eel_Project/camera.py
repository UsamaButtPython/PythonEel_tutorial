import cv2
import os
# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
# ds_factor=0.6

class VideoCamera(object):
    def __init__(self,cam_num):
        self.video = cv2.VideoCapture(cam_num)
    
    def __del__(self):
        self.video.release()

    # def close(self):
    #     self.video.release()
    def get_frame(self):
        # print("I'm Zero")
        success, image = self.video.read()
        key = os.environ.get("cam_key")
        if(key=="1"):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif(key=="2"):
            # Setting parameter values
            t_lower = 50  # Lower Threshold
            t_upper = 150  # Upper threshold
            # Applying the Canny Edge filter
            image = cv2.Canny(image, t_lower, t_upper)
        elif(key=="3"):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        elif(key=="4"):
            image = cv2.GaussianBlur(image, (15,15),0)   
        else:
            pass
        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        # for (x,y,w,h) in face_rects:
        # 	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        # 	break
        # ret, jpeg = cv2.imencode('.jpg', image)
        # return jpeg.tobytes()
        return frame
            

# import eel
# eel.init('web')

# @eel.expose
# def dummy(params):
#     print("I Got it",params)
#     return "Aa gaya Eel ka Sawad"

# eel.start('index.html',size=(1000,600))    


#Import necessary libraries
# from flask import Flask, render_template, Response
# import cv2
# #Initialize the Flask app
# app = Flask(__name__)


# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
# ds_factor=0.6
# # camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture(0)
# '''
# for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
# for local webcam use cv2.VideoCapture(0)
# '''
# def gen_frames():  
#     while True:
#         success, frame = camera.read()  # read the camera frame
#         # cv2.imshow('frame',frame)
#         print("frame,success",frame,success)
#         if not success:
#             print("yahan ha")
#             camera.release()
#             break
#         else:
#             # ret, buffer = cv2.imencode('.jpg', frame)
#             # frame = buffer.tobytes()
#             image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
#             gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#             face_rects=face_cascade.detectMultiScale(gray,1.3,5)
#             for (x,y,w,h) in face_rects:
#                 cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
#                 break
#             ret, jpeg = cv2.imencode('.jpg', image)
#             frame= jpeg.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

import cv2
# cap = cv2.VideoCapture("rtsp://rtsp.stream/pattern")
# # cap2 = cv2.VideoCapture(0)
# while True:

#     ret, frame = cap.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
vcap = cv2.VideoCapture("rtsp://rtsp.stream/pattern")
cap2 = cv2.VideoCapture("rtsp://admin:Sentry_2020!@166.140.230.62:554/cam/realmonitor?channel=9&subtype=1")
# while(1):

#     ret, frame = vcap.read()
#     ret, frame2 = cap2.read()

#     cv2.imshow('VIDEO', frame)
#     cv2.imshow('VIDEO2', frame2)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
while True:
    ret, frame = cap2.read()

    if not ret:
        print("Camera is disconnected!")
        cap2.release()
    # `   return False
        break
    else:
        cv2.imshow('frame', frame)
        # return True # Here You are returning the status.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')    


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True) 

# from flask import Flask, render_template, Response
# from camera import VideoCamera
# import eel
# eel.init('web')

# @eel.expose
# def dummy(params):
#     print("I Got it",params)
#     return "Aa gaya Eel ka Sawad"

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
# eel.start('index.html',size=(1000,600)) 





# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)



# uncomment from here

# import logging
# import os
# import sys
# from tkinter import Tk, messagebox
# import eel
# # from camera import VideoCamera
# import camera
# import base64
# import time
# from user import *
# import cv2
# from sqlalchemy import create_engine
# import requests
# import hashlib

# os.environ["cam_key"]="0"
# stop_key=0
# testvar=0
# engine = create_engine('sqlite:///test.db', echo = True)

# # def Is_login(func):
# #     def inner():
# #         # s = requests.Session()
        
# #         print("I got decorated")
# #         func()
# #     return inner
# def Is_login(func):
#     try:
#         print("I got a function")
#         print(s.auth[0])
#         func()
#     except:
#         return False    
#     # return inner

# def show_error(title, msg):
#     root = Tk()
#     root.withdraw()  # hide main window
#     messagebox.showerror(title, msg)
#     root.destroy()


# def gen(camera):
#     global stop_key
#     while True:
        
#         frame = camera.get_frame()    
#         yield frame
#         if stop_key==1:
#             break
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     camera.__del__()
#     eel.updateImageSrc(" ")()



# # def gen(camera):
# #     while True:
# #         frame = camera.get_frame()
# #         yield (frame)


# @eel.expose

# def video_feed():
#     global stop_key
#     stop_key=0
#     print("Click to Start")

#     x = camera.VideoCamera(0)
#     y = gen(x)
#     for each in y:
#         # Convert bytes to base64 encoded str, as we can only pass json to frontend
#         blob = base64.b64encode(each)
#         blob = blob.decode("utf-8")
#         eel.updateImageSrc(blob)()

# # @eel.expose

# # def video_feed():
# #     Is_login(test)
       
# #         # time.sleep(0.1)
# # def test():
# #     global stop_key
# #     stop_key=0
# #     print("Click to Start")

# #     x = VideoCamera(0)
# #     y = gen(x)
# #     for each in y:
# #         # Convert bytes to base64 encoded str, as we can only pass json to frontend
# #         blob = base64.b64encode(each)
# #         blob = blob.decode("utf-8")
# #         eel.updateImageSrc(blob)()       


# @eel.expose
# def video_stop():
#     print("Click to stop")
#     global stop_key
#     stop_key=1


# @eel.expose
# def filter(cond):
#     os.environ["cam_key"]=str(cond)

# s = requests.Session()

# @eel.expose
# def login(email,password):

#     print(email,password)
#     # hashlib.md5(password.encode('utf-8')).hexdigest()

#     if email=="sdff@wdfw.chn" and password=="1234":
#         s.auth = (email, password)
#         print(s.auth[0])
#         eel.show('index.html')
#         return True
        
#     return False    


# def start_app():
#     # Start the server
#     try:
#         # eel.init('web')
#         # eel.start('index.html',size=(1000,600))
#         global testvar
#         testvar=1
#         print("Run")
#         BASEDIR = os.path.dirname(os.path.abspath(__file__))
#         web_dir = BASEDIR+"/web"
#         # start_html_page = 'index.html'
#         start_html_page = 'templates/login.html'

#         eel.init(web_dir)
#         logging.info("App Started")
#         # by using options its was in v1
#         # options = {'host': 'localhost', 'port': 8000}
#         # eel.start(start_html_page,jinja_templates='templates',options=options,suppress_error=True)
#         # default port is 8000
#         eel.start(start_html_page,jinja_templates='templates',port=8000)

#     except Exception as e:
#         err_msg = 'Could not launch a local server'
#         logging.error('{}\n{}'.format(err_msg, e.args))
#         show_error(title='Failed to initialise server', msg=err_msg)
#         logging.info('Closing App')
#         sys.exit()


# if __name__ == "__main__":
#     # print("testvar = ",testvar)
#     # if testvar==0:
#     #     pass
#     start_app()
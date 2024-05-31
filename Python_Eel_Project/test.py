import cv2
# cap = cv2.VideoCapture()
try:
    video =cv2.VideoCapture("http://166.164.136.158:81/1/viqcam.mjpg")
    if video is None or not video.isOpened():
            print("ksdjfcbdsfbdshfb")   
# cap2 = cv2.VideoCapture(0)
# while True:

#     ret, frame = cap.read()
#     print("frame,success",frame,ret)

#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     if cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) <1:
#         break

# cap.release()
# cv2.destroyAllWindows()
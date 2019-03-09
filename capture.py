import cv2

video = cv2.VideoCapture(0)

while True:
    frame = video.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows
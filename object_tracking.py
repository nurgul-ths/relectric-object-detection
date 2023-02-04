import cv2
import numpy as np
from object_detection import ObjectDetection

od = ObjectDetection()
cap = cv2.VideoCapture("cars_highway.mp4")
while True:
    _, frame = cap.read()
    if not _:
        break
    (class_ids, scores, boxes) = od.detect(frame)

    for box in boxes:
        (x, y, w, h) = box
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

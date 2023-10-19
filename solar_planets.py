import cv2
cv2.imread('solar-system.jpg')
cv2.imshow('output',img)
cv2.waitKey(0)
cv2.putText(img,
             'Sun',
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5
             (225,225,225))
#accuracy of google search engine
'''
fit -  best ,under,over
error = RMSE = sqrt[suma{(obs-act)2}/n]

over = covering training but not testing
under = not covering the training set itset 
best = covers both traing and testing data 

how to get coeff for linear regression, get the slope of line and the intersection(c)?
'''
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                               # detect the face in gray img n take strting point n width n ht

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)                    # draw rect around the face
        roi_gray = gray[y:y + h, x:x + w]                                             # as eye is present inside the face , it take face as roi
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)                                 # detect the eye in gray img n take strting point n width n ht
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)    # draw rect around the eye

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()












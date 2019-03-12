import cv2

capture = cv2.VideoCapture(0)


while True:
    ret, frame = capture.read()

    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

    detected_faces = face_cascade.detectMultiScale(g)

    for (column, row, width, height) in detected_faces:
        cv2.rectangle(frame,(column, row),
        (column + width, row + height),(0, 255, 0),2)
        cv2.putText(frame, "Person", (column, row),
        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), lineType=cv2.LINE_AA) 

    
    cv2.imshow('Image', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()



import cv2 as cv

cap = cv.VideoCapture(1)

if not cap.isOpened():   #если не работает
    print("Камера не работает")
    exit()
while True: #тогда запускаем бесконечный цикл
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Не могу получить файлик")
        break
    
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    #image = cv.imread(frame)

    faces = face_cascade.detectMultiScale(
        frame,
        scaleFactor= 1.1,
        minNeighbors= 5,
        minSize=(10, 10)
    )
    faces_detected = "Лиц обнаружено: " + format(len(faces))
    print(faces_detected)
# Рисуем квадраты вокруг лиц
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('Картинка', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
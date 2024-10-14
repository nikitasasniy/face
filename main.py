import cv2


def detect_faces(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Инициализация каскадного классификатора для детекции лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Преобразование изображения в градации серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск лиц
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Found {len(faces)} face(s)")

    # Рисование прямоугольников вокруг найденных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Изменение размера изображения (например, до 800x600)
    resized_image = cv2.resize(image, (800, 600))

    # Показать уменьшенное изображение с отмеченными лицами
    cv2.imshow("Faces found", resized_image)

    # Сохранить результат
   # cv2.imwrite("faces_detected.jpg", image)

    # Ожидание нажатия клавиши для закрытия окна
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_faces("photo.jpg")

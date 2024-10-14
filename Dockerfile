# Используем официальный образ Python с минимальным размером
FROM python:3.10-slim

# Обновляем пакеты и устанавливаем зависимости для OpenCV
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    python3-opencv \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости из requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
COPY . /app
WORKDIR /app

## Загрузка модели для DNN (в реальном проекте лучше добавить модель в репозиторий)
#RUN curl -o res10_300x300_ssd_iter_140000_fp16.caffemodel https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel?raw=true
#RUN curl -o deploy.prototxt https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt?raw=true

# Запуск скрипта face_detection.py при запуске контейнера
CMD ["python", "face_detection.py"]

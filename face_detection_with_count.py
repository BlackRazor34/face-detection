import cv2


def face_detection(video_source=0):
    # Yüz algılama için Haar Cascade sınıflandırıcısını yükleyin
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Video kaynağını açın (video_source = 0, web kamerasını kullanır, dosya yolu ise video dosyasını kullanır)
    cap = cv2.VideoCapture('https://www.youtube.com/watch?v=uoVUE1OnvoY')
    while cap.isOpened():
        # Videodan bir kare yakalayın
        ret, frame = cap.read()

        # Video bitmişse veya web kamerası açılmazsa çıkış yap
        if not ret:
            print("Video akışı bitti veya cihaz bağlanamadı.")
            break

        # Görüntüyü gri tonlamalıya çevirin
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Yüzleri algılayın
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Algılanan yüzlerin etrafına dikdörtgen çizin

        face_count = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_count += 1

        # Yüz sayısını görüntüye ekleyin
        cv2.putText(frame, f'Yuz Sayisi: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Sonucu ekranda gösterin
        cv2.imshow('Yüz Algılama', frame)

        # 'q' tuşuna basıldığında programdan çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Video kaynağını ve pencereleri serbest bırak
    cap.release()
    cv2.destroyAllWindows()

# Web kamerası için
face_detection(0)

# Video dosyası için (örneğin, 'video.mp4' yerine video dosyanızın yolunu koyun)
# face_detection('video.mp4')

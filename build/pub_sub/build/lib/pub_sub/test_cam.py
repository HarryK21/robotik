import cv2

# Wir erzwingen das MJPEG Backend
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# WICHTIG: Erst das Format auf MJPEG setzen, dann die Auflösung!
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if cap.isOpened():
    print("Kamera ist offen. Warte auf ersten Frame...")
    # Wir geben der Kamera 2 Sekunden Zeit zum "Aufwärmen"
    for _ in range(30):
        ret, frame = cap.read()
        if ret:
            print("BILD ERHALTEN! Auflösung:", frame.shape)
            break
    else:
        print("Timeout: Kamera offen, aber keine Bilder. Versuche USB-Port zu wechseln.")
    cap.release()

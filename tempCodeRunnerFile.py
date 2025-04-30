import cv2
import numpy as np

def show_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = frame[y, x]
        color_text = f"B: {b}, G: {g}, R: {r}"
        print(color_text)

        # Draw a rectangle and display BGR values on the frame
        top_left = (20, 20)
        bottom_right = (300, 60)
        cv2.rectangle(frame, top_left, bottom_right, (b, g, r), -1)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, color_text, (30, 50), font, 0.7, (255-b, 255-g, 255-r), 2)

# Open webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow('Color Detector')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.setMouseCallback('Color Detector', show_color)
    cv2.imshow('Color Detector', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()

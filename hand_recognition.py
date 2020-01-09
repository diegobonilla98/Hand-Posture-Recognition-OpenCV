import cv2
import numpy as np


def draw_contour_outline(img, cnts, color, thickness=1):
    for cnt in cnts:
        cv2.drawContours(img, [cnt], 0, color, thickness)


def draw_contour_points(img, cnts, color):
    for cnt in cnts:
        squeeze = np.squeeze(cnt)
        for p in squeeze:
            pp = tuple(p.reshape(1, -1)[0])
            cv2.circle(img, pp, 3, color, -1)
    return img


video = cv2.VideoCapture(0)
lower_ycrcb = np.array([0, 133, 77], dtype="uint8")
upper_ycrcb = np.array([255, 173, 127], dtype="uint8")
kernel = np.ones((3, 3), np.uint8)
while True:
    state, frame = video.read()

    frame = cv2.flip(frame, 1)
    cut_frame = frame[180:300, 350:480]
    ycrcb_image = cv2.cvtColor(cut_frame.copy(), cv2.COLOR_BGR2YCR_CB)
    skin_region = cv2.inRange(ycrcb_image, lower_ycrcb, upper_ycrcb)
    skin_region = cv2.morphologyEx(skin_region, cv2.MORPH_OPEN, kernel, iterations=3)
    _, contours, _ = cv2.findContours(skin_region, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contour_image = cut_frame.copy()
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 2000:
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            draw_contour_outline(contour_image, [approx], (255, 255, 0), 2)
            draw_contour_points(contour_image, [approx], (255, 0, 255))
    cv2.rectangle(frame, (350, 180), (480, 300), (0, 255, 255), 1)

    cv2.imshow('webcam', frame)
    cv2.imshow('hand contour', contour_image)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
video.release()

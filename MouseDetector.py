import cv2


class MouseDetector:

    x = -1
    y = -1

    @staticmethod
    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            MouseDetector.x = x
            MouseDetector.y = y

    @staticmethod
    def print_coordinates():
        print(MouseDetector.x, MouseDetector.y)

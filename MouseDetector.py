import cv2


class MouseDetector:
    @staticmethod
    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            MouseDetector.x = x
            MouseDetector.y = y

    @staticmethod
    def print_coordinates():
        print(MouseDetector.x, MouseDetector.y)

    @staticmethod
    def get_coordinates():
        return MouseDetector.x, MouseDetector.y

    x, y = -1, -1

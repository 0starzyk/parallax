import cv2
import numpy as np
import matplotlib.pyplot as plt


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)


if __name__ == '__main__':
    img = cv2.imread(cv2.samples.findFile("tree.jpg"))
    cv2.imshow("Window", img)
    cv2.setMouseCallback('Window', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

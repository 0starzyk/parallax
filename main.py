import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    img = cv2.imread("tree.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Window 1", img)
    lower = 0
    higher = 3
    new = cv2.inRange(img, lower, higher)
    cv2.imshow("Window2 ", new)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

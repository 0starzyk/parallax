import cv2
import numpy as np
import matplotlib.pyplot as plt
from MouseDetector import MouseDetector


if __name__ == "__main__":
    original_image = cv2.imread("tree_modified.jpg", cv2.IMREAD_COLOR)

    cv2.imshow("Window 1", original_image)
    cv2.setMouseCallback('Window 1', MouseDetector.click_event)

    # lower_threshold = np.array([0, 0, 170])
    # higher_threshold = np.array([150, 150, 255])
    # thresholded_image = cv2.inRange(original_image, lower_threshold, higher_threshold)
    # cv2.imshow("Window 2", thresholded_image)

    # kernel = np.ones((5, 5))
    # dilated_image = cv2.dilate(thresholded_image, kernel, iterations=1)
    # eroded_image = cv2.erode(dilated_image, kernel, iterations=8)
    # cv2.imshow("Window 3", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    x, y = MouseDetector.get_coordinates()
    MouseDetector.print_coordinates()
    color = original_image[y, x]
    print(color)

import cv2
import numpy as np
import matplotlib.pyplot as plt

import config
from MouseDetector import MouseDetector
import utils


if __name__ == "__main__":
    original_image = cv2.imread("traffic_light.jpg", cv2.IMREAD_COLOR)

    cv2.imshow("Window 1", original_image)
    cv2.setMouseCallback('Window 1', MouseDetector.click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    x, y = MouseDetector.get_coordinates()
    MouseDetector.print_coordinates()
    color = original_image[y, x]
    print(color)

    lower_threshold = np.array(list(map(lambda value: utils.clamp(
        value - config.THRESHOLD_TOLERANCE, config.MINIMUM_RGB_VALUE, config.MAXIMUM_RGB_VALUE), color)))
    higher_threshold = np.array(list(map(lambda value: utils.clamp(
        value + config.THRESHOLD_TOLERANCE, config.MINIMUM_RGB_VALUE, config.MAXIMUM_RGB_VALUE), color)))
    threshold_image = cv2.inRange(original_image, lower_threshold, higher_threshold)

    kernel = np.ones((5, 5))
    dilated_image = cv2.dilate(threshold_image, kernel, iterations=1)

    cv2.imshow("Window 2", dilated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

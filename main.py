import cv2
import numpy as np
import matplotlib.pyplot as plt

from config import *
from MouseDetector import MouseDetector
import utils


if __name__ == "__main__":
    original_image = cv2.imread("images/traffic_light.jpg", cv2.IMREAD_COLOR)

    cv2.imshow("Window 1", original_image)
    cv2.setMouseCallback('Window 1', MouseDetector.click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    x, y = MouseDetector.get_coordinates()
    color = original_image[y, x]

    lower_threshold = np.array(list(map(lambda value: utils.clamp(
        value - ThresholdOperations.THRESHOLD_TOLERANCE, ThresholdOperations.MINIMUM_RGB_VALUE,
        ThresholdOperations.MAXIMUM_RGB_VALUE), color)))
    higher_threshold = np.array(list(map(lambda value: utils.clamp(
        value + ThresholdOperations.THRESHOLD_TOLERANCE, ThresholdOperations.MINIMUM_RGB_VALUE,
        ThresholdOperations.MAXIMUM_RGB_VALUE), color)))
    threshold_image = cv2.inRange(original_image, lower_threshold, higher_threshold)

    kernel = np.ones((5, 5))
    dilated_image = cv2.dilate(threshold_image, kernel, iterations=1)
    contours, hierarchies = cv2.findContours(dilated_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    blank = np.zeros(dilated_image.shape[:2], dtype='uint8')
    cv2.drawContours(blank, contours, -1, (255, 0, 0), 1)

    cv2.imshow("Window 2", blank)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

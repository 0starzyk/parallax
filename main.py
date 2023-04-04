import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    original_image = cv2.imread("traffic_light.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Window 1", original_image)
    # 255, 137, 144 --- 97, 29, 40
    lower_threshold = np.array([40, 29, 120])
    higher_threshold = np.array([144, 137, 255])
    thresholded_image = cv2.inRange(original_image, lower_threshold, higher_threshold)
    cv2.imshow("Window 2", thresholded_image)

    kernel = np.ones((5, 5))
    dilated_image = cv2.dilate(thresholded_image, kernel, iterations=1)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=6)

    cv2.imshow("Window 3", eroded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

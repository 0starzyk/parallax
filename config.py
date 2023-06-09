from enum import Enum


class ThresholdOperations(int, Enum):
    THRESHOLD_TOLERANCE = 50
    MINIMUM_RGB_VALUE = 0
    MAXIMUM_RGB_VALUE = 255

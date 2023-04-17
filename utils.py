def clamp(num: int, min_value: int, max_value: int) -> int:
    return max(min(num, max_value), min_value)


def center_of_shape(image):
    number_of_all_points = sum(sum(image))
    isum, jsum = 0, 0

    for i in range(len(image)):
        for j in range(len(image[i])):
            isum += i if image[i, j] != 0 else 0
            jsum += j if image[i, j] != 0 else 0
            image[i, j] = 0

    # print(int(isum / number_of_all_points))
    # print(int(jsum / number_of_all_points))

    print(isum)
    print(jsum)
    print(number_of_all_points)

    # center_point_position = (int(isum / number_of_all_points), int(jsum / number_of_all_points))
    # image[center_point_position[0], center_point_position[1]] = 1
    #
    # return image

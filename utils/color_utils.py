import numpy as np
import cv2

def count_red_cars(image, boxes):
    red_count = 0
    np_image = np.array(image)

    for (x1, y1, x2, y2) in boxes:
        car_crop = np_image[y1:y2, x1:x2]
        hsv = cv2.cvtColor(car_crop, cv2.COLOR_RGB2HSV)
        red_mask = (
            ((hsv[:, :, 0] < 10) | (hsv[:, :, 0] > 160)) &
            (hsv[:, :, 1] > 100) & (hsv[:, :, 2] > 100)
        )
        red_ratio = red_mask.sum() / (car_crop.shape[0] * car_crop.shape[1])
        if red_ratio > 0.15:  # threshold
            red_count += 1

    return red_count
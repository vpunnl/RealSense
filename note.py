# import cv2

# image = cv2.imread("butterfly.jpg")

# print(image.shape)
# # print(image[:5])
# # print(type(image))
# for i in range(0,10):
#     print(i)

import numpy as np

# Array shape
height, width = 480, 640

# Create a point cloud array
point_cloud = np.zeros((height, width, 3), dtype=np.int8)

# Assign random 3D coordinates
# for y in range(height):
#     for x in range(width):
#         point_cloud[y, x] = [x, y, np.random.uniform(0, 1)]

# print(point_cloud[0])
x_grid,y_grid = np.meshgrid(range(640),range(480))


r = np.stack((x_grid,y_grid),axis=2)
print(r)
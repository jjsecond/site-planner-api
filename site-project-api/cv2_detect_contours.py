import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./temp_site_plans/site-four.png", cv2.IMREAD_COLOR)
img = cv2.resize(img, (1000, 1000)) 


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

edges = cv2.Canny(img_blur, 160,180)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

min_area = 8000 
plot_count = 0

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > min_area: 
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

        print(approx)
        if len(approx) == 4:  # for square houses
            cv2.drawContours(img_rgb, [approx], -1, (0, 255, 0), 2)
            plot_count = plot_count + 1
        if len(approx) > 4 & len(approx) < 8: # for non square houses 
            cv2.drawContours(img_rgb, [approx], -1, (0, 255, 0), 2)
            plot_count = plot_count + 1

    


plt.imshow(img_rgb)
plt.title(f"Housing Plots Detected: {plot_count}")
plt.show()
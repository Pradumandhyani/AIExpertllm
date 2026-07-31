import cv2

image_path = r"D:\Codingal\AIExpertllm\VisionaryAi\Lesson3\abc.png"
image = cv2.imread(image_path)

cv2.imshow('Original Image', image)

cv2.waitKey(0)

cv2.destroyAllWindows()

Filter_Image = image.copy()

Filter_Image[:,:, 0] = 0

Filter_Image[:,:, 1] = 0

cv2.imshow('Filtered Image', Filter_Image)

cv2.waitKey(0)

cv2.destroyAllWindows()


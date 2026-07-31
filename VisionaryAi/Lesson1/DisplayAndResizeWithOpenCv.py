import cv2

image_path = r"D:\Codingal\AIExpertllm\VisionaryAi\Lesson1\abc.png"

image = cv2.imread(image_path)

if image is None:
    print("Image not found. Please check the image path or file name.")
else:
    cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Loaded Image', 300, 100)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
    cv2.imshow('Loaded Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Image Dimensions: {image.shape}")
import cv2

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()

# 0 equal to blue 1 == green and 2 equal to red
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0 
        filtered_image[:, :, 0] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    return filtered_image


image_path = r"D:\Codingal\AIExpertllm\VisionaryAi\Lesson3\abc.png"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:

    # Show original image only once
    cv2.imshow("Original Image", image)
    print("Close the image window to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    while True:
        print("\nChoose a filter:")
        print("r - Red Tint")
        print("b - Blue Tint")
        print("g - Green Tint")
        print("i - Increase Red Intensity")
        print("d - Decrease Blue Intensity")
        print("q - Quit")

        choice = input("Enter your choice: ").lower()

        if choice == "q":
            print("Exiting...")
            break

        elif choice == "r":
            filter_type = "red_tint"
        elif choice == "b":
            filter_type = "blue_tint"
        elif choice == "g":
            filter_type = "green_tint"
        elif choice == "i":
            filter_type = "increase_red"
        elif choice == "d":
            filter_type = "decrease_blue"
        else:
            print("Invalid choice!")
            continue

        filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)
        print("Close the image window to choose another filter.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
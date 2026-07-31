# Import OpenCV library for computer vision and image processing
import cv2

# Import NumPy library for numerical operations and array creation
import numpy as np


# ---------------------------------------------
# Open the default webcam (0 = primary webcam)
# ---------------------------------------------
cap = cv2.VideoCapture(0)

# Check whether the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()  # Stop the program if webcam is not available


# ---------------------------------------------
# Infinite loop to continuously capture frames
# ---------------------------------------------
while True:

    # Capture a single frame from the webcam
    ret, frame = cap.read()

    # If frame is not captured successfully, stop the program
    if not ret:
        print("Error: Failed to capture image.")
        break


    # ------------------------------------------------------
    # Convert the captured frame from BGR color space to HSV
    # BGR = Blue Green Red (default in OpenCV)
    # HSV = Hue Saturation Value
    # HSV makes color detection easier.
    # ------------------------------------------------------
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # ----------------------------------------------------
    # Define lower and upper HSV values for human skin
    #
    # Hue        : Color
    # Saturation : Purity of color
    # Value      : Brightness
    #
    # Pixels lying within this range are considered skin.
    # ----------------------------------------------------
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)


    # ---------------------------------------------------
    # Create a binary mask.
    #
    # Pixels inside skin range become WHITE (255)
    # Pixels outside skin range become BLACK (0)
    # ---------------------------------------------------
    mask = cv2.inRange(hsv, lower_skin, upper_skin)


    # ---------------------------------------------------
    # Apply the mask to the original frame.
    #
    # bitwise_and keeps only skin-colored regions.
    # Everything else becomes black.
    # ---------------------------------------------------
    result = cv2.bitwise_and(frame, frame, mask=mask)


    # ---------------------------------------------------
    # Detect contours in the binary mask.
    #
    # Contours are outlines/boundaries of white objects.
    #
    # RETR_EXTERNAL:
    #     Detect only outermost contours.
    #
    # CHAIN_APPROX_SIMPLE:
    #     Stores only important contour points.
    # ---------------------------------------------------
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    # ---------------------------------------------------
    # Check whether any contour has been detected
    # ---------------------------------------------------
    if contours:

        # Find the contour having the maximum area.
        # This assumes the hand is the largest skin object.
        max_contour = max(contours, key=cv2.contourArea)

        # Ignore very small contours (noise)
        if cv2.contourArea(max_contour) > 500:

            # ------------------------------------------
            # Find the bounding rectangle around hand
            #
            # x = left coordinate
            # y = top coordinate
            # w = width
            # h = height
            # ------------------------------------------
            x, y, w, h = cv2.boundingRect(max_contour)


            # ------------------------------------------
            # Draw a green rectangle around the hand
            #
            # frame = image
            # (x,y) = top-left corner
            # (x+w,y+h) = bottom-right corner
            # (0,255,0) = green color
            # 2 = thickness
            # ------------------------------------------
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )


            # ------------------------------------------
            # Calculate the center of the rectangle
            # ------------------------------------------
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)


            # ------------------------------------------
            # Draw a filled red circle at the center
            #
            # Radius = 5 pixels
            # Color = Red
            # Thickness = -1 means filled circle
            # ------------------------------------------
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )


    # ------------------------------------------
    # Display original webcam frame
    # ------------------------------------------
    cv2.imshow("Original Frame", frame)


    # ------------------------------------------
    # Display only detected skin regions
    # ------------------------------------------
    cv2.imshow("Filtered Frame", result)


    # ------------------------------------------
    # Wait for 1 millisecond for keyboard input
    #
    # If user presses 'q',
    # exit the loop.
    # ------------------------------------------
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# ------------------------------------------
# Release the webcam resource
# ------------------------------------------
cap.release()


# ------------------------------------------
# Close all OpenCV windows
# ------------------------------------------
cv2.destroyAllWindows()
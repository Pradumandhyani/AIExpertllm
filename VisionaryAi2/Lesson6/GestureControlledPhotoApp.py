# ============================
# Import Required Libraries
# ============================
import cv2                  # OpenCV for webcam access and image processing
import time                 # Used for timing gestures (debouncing and capture delay)
import numpy as np          # Used for numerical operations and filter matrices
import mediapipe as mp      # MediaPipe for real-time hand detection

# ============================
# Initialize MediaPipe Hands
# ============================
H = mp.solutions.hands
TIP = H.HandLandmark

# Store fingertip landmark IDs for easy access
ids = {
    "thumb": TIP.THUMB_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP,
}

# Create the hand detector
# min_detection_confidence -> confidence for first-time detection
# min_tracking_confidence  -> confidence for tracking the detected hand
hands = H.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Used to draw hand landmarks on the webcam frame
draw = mp.solutions.drawing_utils

# ====================================================
# Define which finger controls which pair of filters
# ====================================================
pairs = {
    "middle": ("SEPIA", "NEGATIVE"),
    "ring": ("BLUR", "GLITCH"),
    "pinky": ("EDGE", "CARTOON")
}

# Keeps track of which filter is currently active
st = {k: 0 for k in pairs}

# Default filter when the program starts
cur = "SEPIA"

# ====================================================
# Configuration Values
# ====================================================

DEB = 0.6     # Debounce time (prevents multiple filter changes)
CAP = 1.2     # Delay between two captures
TT = 30       # Finger touch threshold (for changing filters)
TP = 20       # Pinch threshold (for taking picture)

# Variables to store last action time
la = 0        # Last filter change time
lc = 0        # Last capture time

# Tracks whether thumb-index pinch is already active
pinch_on = False

# Window names
MAIN = "Gesture-Controlled Photo App"
POP = "Captured (ESC / Close to resume)"

# Pause variables
paused = False
freeze = None

# ====================================================
# Sepia Transformation Matrix
# Used to create vintage effect
# ====================================================
SEPIA_M = np.array([
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]
])

# ====================================================
# Function to Apply Filters
# ====================================================
def apply(img, t):

    # ------------------------
    # SEPIA FILTER
    # ------------------------
    if t == "SEPIA":
        return np.clip(
            cv2.transform(img, SEPIA_M),
            0,
            255
        ).astype(np.uint8)

    # ------------------------
    # NEGATIVE FILTER
    # ------------------------
    if t == "NEGATIVE":
        return cv2.bitwise_not(img)

    # ------------------------
    # BLUR FILTER
    # ------------------------
    if t == "BLUR":
        return cv2.GaussianBlur(img, (15, 15), 0)

    # ------------------------
    # GLITCH FILTER
    # ------------------------
    if t == "GLITCH":

        h, w = img.shape[:2]

        # Split RGB channels
        r = img[:, :, 2]
        g = img[:, :, 1]
        b = img[:, :, 0]

        # Shift Red and Blue channels
        return cv2.merge([
            np.roll(b, -int(0.02 * w), 1),
            g,
            np.roll(r, int(0.04 * w), 1)
        ])

    # ------------------------
    # EDGE DETECTION
    # ------------------------
    if t == "EDGE":

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return cv2.Canny(gray, 80, 160)

    # ------------------------
    # CARTOON FILTER
    # ------------------------
    if t == "CARTOON":

        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Reduce noise
        blur = cv2.medianBlur(gray, 7)

        # Detect edges
        edges = cv2.adaptiveThreshold(
            blur,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            9,
            2
        )

        # Smooth colors
        color = cv2.bilateralFilter(img, 9, 75, 75)

        # Combine edges with smooth colors
        return cv2.bitwise_and(color, color, mask=edges)

    # Return original image if no filter selected
    return img

# ====================================================
# Start Webcam
# ====================================================
cap = cv2.VideoCapture(0)

# Check whether webcam opened successfully
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

# Create resizable window
cv2.namedWindow(MAIN, cv2.WINDOW_NORMAL)

# ====================================================
# Main Program Loop
# ====================================================
while True:

    # ------------------------------------------------
    # If photo has been captured, pause live webcam
    # ------------------------------------------------
    if paused:

        cv2.imshow(MAIN, freeze)

        k = cv2.waitKey(50) & 0xFF

        # Press Q to exit
        if k == ord("q"):
            break

        # Press ESC to resume webcam
        if k == 27:
            paused = False
            pinch_on = False

            try:
                cv2.destroyWindow(POP)
            except:
                pass

            continue

        # Resume if popup window is closed
        try:
            if cv2.getWindowProperty(
                    POP,
                    cv2.WND_PROP_VISIBLE
            ) <= 0:

                paused = False
                pinch_on = False

        except cv2.error:
            paused = False
            pinch_on = False

        continue

    # ------------------------------------------------
    # Read Frame from Webcam
    # ------------------------------------------------
    ok, img = cap.read()

    if not ok:
        break

    # Flip image for mirror effect
    img = cv2.flip(img, 1)

    # Get image dimensions
    h, w = img.shape[:2]

    # Convert image to RGB because MediaPipe uses RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect hand landmarks
    res = hands.process(rgb)

    now = time.time()

    capture = False

    # ------------------------------------------------
    # If Hand Detected
    # ------------------------------------------------
    if res.multi_hand_landmarks:

        # Take only first detected hand
        hand = res.multi_hand_landmarks[0]

        # Draw landmarks on image
        draw.draw_landmarks(
            img,
            hand,
            H.HAND_CONNECTIONS
        )

        lm = hand.landmark

        # Store pixel coordinates of fingertips
        tips = {
            k: (
                int(lm[v].x * w),
                int(lm[v].y * h)
            )
            for k, v in ids.items()
        }

        # Thumb coordinates
        tx, ty = tips["thumb"]

        # Index coordinates
        ix, iy = tips["index"]

        # --------------------------------------------
        # Check Pinch Gesture
        # Thumb + Index Finger
        # --------------------------------------------
        pinch = (
            abs(tx - ix) < TP and
            abs(ty - iy) < TP
        )

        # Capture image only once
        if pinch and not pinch_on and now - lc > CAP:

            pinch_on = True
            capture = True
            lc = now

        # Reset pinch state
        if not pinch and pinch_on:
            pinch_on = False

        # --------------------------------------------
        # Filter Selection
        # Thumb touches another finger
        # --------------------------------------------
        if not pinch:

            t = next(

                (
                    k for k in pairs

                    if abs(tx - tips[k][0]) < TT

                    and abs(ty - tips[k][1]) < TT

                ),

                None

            )

            # Change filter if enough time has passed
            if t and now - la > DEB:

                # Select filter
                cur = pairs[t][st[t]]

                # Toggle between two filters
                st[t] ^= 1

                la = now

                print("Filter:", cur)

    # ------------------------------------------------
    # Apply Selected Filter
    # ------------------------------------------------
    out = apply(img, cur)

    # Edge filter returns grayscale
    # Convert back to BGR for displaying
    if cur == "EDGE":
        out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)

    # ------------------------------------------------
    # Capture Image
    # ------------------------------------------------
    if capture:

        # Generate filename using timestamp
        name = f"picture_{int(now)}.jpg"

        # Save image
        cv2.imwrite(name, out)

        print("Saved:", name)

        # Freeze current image
        paused = True
        freeze = out.copy()

        # Show captured image
        cv2.imshow(POP, freeze)

    # ------------------------------------------------
    # Show Live Webcam
    # ------------------------------------------------
    cv2.imshow(MAIN, out)

    # Quit application
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ====================================================
# Release Resources
# ====================================================
cap.release()          # Release webcam
cv2.destroyAllWindows()# Close all windows
hands.close()          # Release MediaPipe resources
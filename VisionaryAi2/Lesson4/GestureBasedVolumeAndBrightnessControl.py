import sys
print(sys.executable)
import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import screen_brightness_control as sbc

# -------------------- MediaPipe Setup --------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Landmark IDs
THUMB_TIP = mp_hands.HandLandmark.THUMB_TIP
INDEX_TIP = mp_hands.HandLandmark.INDEX_FINGER_TIP

# -------------------- Volume Setup --------------------
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    volume = interface.QueryInterface(IAudioEndpointVolume)

    min_vol, max_vol = volume.GetVolumeRange()[:2]

except Exception as e:
    print("Volume Initialization Error:", e)
    exit()

# -------------------- Webcam --------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access webcam.")
    exit()

WINDOW_NAME = "Hand Gesture Volume & Brightness"

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks and results.multi_handedness:

        for hand_landmarks, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness):

            label = handedness.classification[0].label

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            lm = hand_landmarks.landmark

            thumb = (
                int(lm[THUMB_TIP].x * w),
                int(lm[THUMB_TIP].y * h)
            )

            index = (
                int(lm[INDEX_TIP].x * w),
                int(lm[INDEX_TIP].y * h)
            )

            cv2.circle(frame, thumb, 10, (255, 0, 0), -1)
            cv2.circle(frame, index, 10, (255, 0, 0), -1)

            cv2.line(frame, thumb, index, (0, 255, 0), 3)

            distance = np.hypot(
                index[0] - thumb[0],
                index[1] - thumb[1]
            )

            # Clamp distance
            distance = np.clip(distance, 30, 300)

            # ---------------- Volume ----------------
            if label == "Left":

                vol = np.interp(
                    distance,
                    [30, 300],
                    [min_vol, max_vol]
                )

                volume.SetMasterVolumeLevel(vol, None)

                percent = int(
                    np.interp(distance, [30, 300], [0, 100])
                )

                bar = int(
                    np.interp(distance, [30, 300], [400, 150])
                )

                cv2.rectangle(frame, (50, 150), (85, 400), (255, 0, 0), 2)
                cv2.rectangle(frame, (50, bar), (85, 400), (255, 0, 0), -1)

                cv2.putText(
                    frame,
                    f"Volume {percent}%",
                    (20, 430),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 0, 0),
                    2
                )

            # ---------------- Brightness ----------------
            else:

                brightness = int(
                    np.interp(distance, [30, 300], [0, 100])
                )

                brightness = max(0, min(brightness, 100))

                try:
                    sbc.set_brightness(brightness)
                except Exception:
                    pass

                bar = int(
                    np.interp(distance, [30, 300], [400, 150])
                )

                x1 = w - 85
                x2 = w - 50

                cv2.rectangle(frame, (x1, 150), (x2, 400), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, bar), (x2, 400), (0, 255, 0), -1)

                cv2.putText(
                    frame,
                    f"Bright {brightness}%",
                    (w - 170, 430),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

    cv2.imshow(WINDOW_NAME, frame)

    key = cv2.waitKey(1)

    if key == 27 or key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
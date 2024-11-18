import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Initialize drawing parameters
drawing = False
erasing = False
canvas = np.zeros((480, 640, 3), dtype=np.uint8)
color = (255, 255, 255)  # White color for drawing

def detect_gesture(hand_landmarks):
    # Get relevant finger tip and pip y-coordinates
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    middle_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    ring_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
    pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
    
    # Check for index finger up (drawing)
    if index_tip < index_pip and middle_tip > middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:
        return "draw"
    
    # Check for all fingers up (stop drawing)
    elif index_tip < index_pip and middle_tip < middle_pip and ring_tip < ring_pip and pinky_tip < pinky_pip:
        return "stop"
    
    # Check for fist (erase)
    elif index_tip > index_pip and middle_tip > middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:
        return "erase"
    
    # Check for open palm (erase)
    elif index_tip < index_pip and middle_tip < middle_pip and ring_tip < ring_pip and pinky_tip < pinky_pip:
        return "erase"
    
    return "none"

cap = cv2.VideoCapture(0)

running = True
while running:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesture = detect_gesture(hand_landmarks)
            
            if gesture == "draw":
                drawing = True
                erasing = False
            elif gesture == "stop":
                drawing = False
                erasing = False
            elif gesture == "erase":
                drawing = False
                erasing = True
            
            if drawing or erasing:
                x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
                y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])
                
                if erasing:
                    cv2.circle(canvas, (x, y), 20, (0, 0, 0), -1)
                else:
                    cv2.circle(canvas, (x, y), 5, color, -1)

    # Combine the canvas with the camera frame
    output = cv2.addWeighted(frame, 0.7, canvas, 0.3, 0)

    cv2.imshow('Hand Gesture Drawing', output)

    key = cv2.waitKey(5)
    if key & 0xFF == 27 or key == ord('q'):  # Press 'Esc' or 'q' to exit
        running = False

cap.release()
cv2.destroyAllWindows()
print("Application closed successfully.")
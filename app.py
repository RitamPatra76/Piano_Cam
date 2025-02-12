import cv2
import mediapipe as mp
import pygame
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

pygame.init()
pygame.mixer.init()

piano_notes = {
    "C": pygame.mixer.Sound("C.wav"), "C#": pygame.mixer.Sound("C#.wav"),
    "D": pygame.mixer.Sound("D.wav"), "D#": pygame.mixer.Sound("D#.wav"),
    "E": pygame.mixer.Sound("E.wav"), "F": pygame.mixer.Sound("F.wav"),
    "F#": pygame.mixer.Sound("F#.wav"), "G": pygame.mixer.Sound("G.wav"),
    "G#": pygame.mixer.Sound("G#.wav"), "A": pygame.mixer.Sound("A.wav"),
    "A#": pygame.mixer.Sound("A#.wav"), "B": pygame.mixer.Sound("B.wav")
}


cap = cv2.VideoCapture(0)

def draw_piano(frame):
    h, w = frame.shape[:2]
    white_keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    black_keys = ['C#', 'D#', 'F#', 'G#', 'A#']
    key_rects = {}

    white_w = w // 7
    white_h = h // 3
    black_w = white_w // 2
    black_h = white_h // 2

    for i, key in enumerate(white_keys):
        x1 = i * white_w
        y1 = h - white_h
        x2 = (i + 1) * white_w
        y2 = h
        key_rects[key] = (x1, y1, x2, y2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), -1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
        cv2.putText(frame, key, (x1 + 15, y2 - 15), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    black_positions = {
        'C#': (0.5, 0), 'D#': (1.5, 1),
        'F#': (3.5, 3), 'G#': (4.5, 4),
        'A#': (5.5, 5)
    }
    
    for key, (rel_pos, white_idx) in black_positions.items():
        x_center = int(rel_pos * white_w)
        x1 = x_center - black_w // 2
        y1 = h - white_h - black_h
        x2 = x_center + black_w // 2
        y2 = h - white_h
        key_rects[key] = (x1, y1, x2, y2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
        cv2.putText(frame, key, (x1 + 5, y1 + 25), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

    return key_rects

def get_pressed_key(x, y, key_rects):
    for key, (x1, y1, x2, y2) in key_rects.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            return key
    return None

screen_width = 1920  
screen_height = 1080  

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    key_rects = draw_piano(frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            x = int(hand_landmarks.landmark[8].x * frame.shape[1])
            y = int(hand_landmarks.landmark[8].y * frame.shape[0])
            cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

            key = get_pressed_key(x, y, key_rects)
            if key:
                pygame.mixer.Sound.play(piano_notes[key])

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    window_name = "AI Piano"
    cv2.imshow(window_name, frame)

    
    window_width = frame.shape[1]
    window_height = frame.shape[0]
    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_height - window_height) // 2
    cv2.moveWindow(window_name, x_pos, y_pos)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
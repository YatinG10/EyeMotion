import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_height, frame_width, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = int(landmark.x * screen_width)
                screen_y = int(landmark.y * screen_height)
                pyautogui.moveTo(screen_x, screen_y)
        
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
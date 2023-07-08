import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
face = mp.solutions.face_mesh.FaceMesh()

while True:
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_height, frame_width, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for landmark in landmarks:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

# import pyautogui
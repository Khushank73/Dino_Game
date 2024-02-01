import cv2

from keysoperation import PressKey, ReleaseKey
from keysoperation import space_pressed
import time

from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

space_key_pressed=space_pressed

time.sleep(2.0)
cur_pressed_key=set()

cap=cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fps_start_time = time.time()
fps_counter = 0
fps=0

while True:
    ret, frame = cap.read()
    # fps_counter += 1
    # if time.time() - fps_start_time >= 1.0:
    #     fps = fps_counter / (time.time() - fps_start_time)
    #     print(f"FPS: {fps:.2f}")
    #     fps_start_time = time.time()
    #     fps_counter = 0
    # cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # cv2.imshow("Live Camera Feed", frame)
    KeyPressed=False
    spacePressed=False
    keycount=0
    spacecount=0
    hands, img = detector.findHands(frame)

    cv2.rectangle(img, (0,480), (300,425), (50,50,255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)


    if hands:
        lmList = hands[0]
        # print(lmList)
        fingerUp = detector.fingersUp(lmList)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame, "Finger Count: 0", (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Jumping", (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            PressKey(space_key_pressed)
            spacePressed=True
            cur_pressed_key.add(space_key_pressed)
            key_pressed=space_key_pressed
            KeyPressed=True
            keycount+=1
        if sum(fingerUp)==1:
            cv2.putText(frame, "Finger Count: 1", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, "Running", (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
        if sum(fingerUp)==2:
            cv2.putText(frame, "Finger Count: 2", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, "Running", (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
        if sum(fingerUp)==3:
            cv2.putText(frame, "Finger Count: 3", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, "Running", (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
        if sum(fingerUp)==4:
            cv2.putText(frame, "Finger Count: 4", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, "Running", (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
        if sum(fingerUp)==5:
            cv2.putText(frame, "Finger Count: 5", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, "Running", (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
        if not KeyPressed and len(cur_pressed_key) != 0:
            for key in cur_pressed_key:
                ReleaseKey(key)
            cur_pressed_key = set()
        elif keycount == 1 and len(cur_pressed_key) == 2:
            for key in cur_pressed_key:
                if key_pressed != key:
                    ReleaseKey(key)
            cur_pressed_key = set()
            for key in cur_pressed_key:
                ReleaseKey(key)
            cur_pressed_key = set()





    # print(hands)

    cv2.imshow("DINO GAME", frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroAllWindows()


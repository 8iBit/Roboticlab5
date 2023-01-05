import cv2
import mediapipe as mp
import pyfirmata

Hand = "None"
Fing1 = "Thumb : Off"
Fing2 = "Index  : Off"
Fing3 = "Middle : Off"
Fing4 = "Ring   : Off"
Fing5 = "Little  : Off"
cam = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

board = pyfirmata.Arduino("COM3")
led_1 = board.get_pin('d:13:o')
led_2 = board.get_pin('d:12:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:10:o')
led_5 = board.get_pin('d:9:o')

while cam.isOpened():
    finger = []
    check, frame = cam.read()
    imgG = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgRGB = cv2.cvtColor(imgG, cv2.COLOR_GRAY2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 6:
                    id6 = int(id)
                    cy6 = cy
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 10:
                    id10 = int(id)
                    cy10 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 9:
                    id9 = int(id)
                    cx9 = cx
                if id == 13:
                    id13 = int(id)
                    cx13 = cx
            if cx9 > cx13:
                Hand = "Right"
                if cx4 > cx3:
                    Fing1 = "Thumb : On"
                    led_1.write(1)
                else:
                   Fing1 = "Thumb : Off"
                   led_1.write(0)
                if cy6 > cy8:
                    Fing2 = "Index  : On"
                    led_2.write(1)
                else:
                   Fing2 = "Index  : Off"
                   led_2.write(0)
                if cy10 > cy12:
                    Fing3 = "Middle : On"
                    led_3.write(1)
                else:
                    Fing3 = "Middle : Off"
                    led_3.write(0)
                if cy14 > cy16:
                    Fing4 = "Ring   : On"
                    led_4.write(1)
                else:
                   Fing4 = "Ring   : Off"
                   led_4.write(0)
                if cy18 > cy20:
                    Fing5 = "Little  : On"
                    led_5.write(1)
                else:
                   Fing5 = "Little  : Off"
                   led_5.write(0)
            else:
                Hand = "Left"
                if cx3 > cx4:
                    Fing1 = "Thumb : On"
                    led_1.write(1)
                else:
                   Fing1 = "Thumb : Off"
                   led_1.write(0)
                if cy6 > cy8:
                    Fing2 = "Index  : On"
                    led_2.write(1)
                else:
                   Fing2 = "Index  : Off"
                   led_2.write(0)
                if cy10 > cy12:
                    Fing3 = "Middle : On"
                    led_3.write(1)
                else:
                   Fing3 = "Middle : Off"
                   led_3.write(0)
                if cy14 > cy16:
                    Fing4 = "Ring   : On"
                    led_4.write(1)
                else:
                   Fing4 = "Ring   : Off"
                   led_4.write(0)
                if cy18 > cy20:
                    Fing5 = "Little  : On"
                    led_5.write(1)
                else:
                   Fing5 = "Little  : Off"
                   led_5.write(0)
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            if cx9 > cx13:
                cv2.putText(frame, Hand, (15, 25),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing1, (15, 45),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing2, (15, 65),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing3, (15, 85),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing4, (15, 105),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing5, (15, 125),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
            else:
                cv2.putText(frame, Hand, (525, 25),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing1, (525, 45),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing2, (525, 65),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing3, (525, 85),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing4, (525, 105),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
                cv2.putText(frame, Fing5, (525, 125),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 100), 2)
    cv2.putText(frame, "Press Z to close...", (460, 460),
                cv2.FONT_HERSHEY_PLAIN, 1, (100, 0, 100), 2)

    if check == True:
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('z'):
            break
    else:
        break
import cv2
from datetime import datetime

position = (20, 450)
size = 1
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 255, 0, 1)
thick = 2

videopath = str(datetime.now().date()) + ".avi"
print(videopath)

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(videopath, fourcc, 25.0, (640, 480))

state = False
rec = None

def timeStamp(state):
    if state == False:
        return
    else:
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        cv2.putText(frame, timestamp, position, font, size, color, thick)

def videoRec(rec):
    if rec == "record":
        out.write(frame)
        cv2.putText(frame, "Recording", (450, 30), font, size, (0, 0, 255))
    elif rec == "stop":
        cv2.putText(frame, "Stopped", (450, 30), font, size, (0, 0, 255))
        out.release()

while True:
    ret, frame = cap.read()
    
    if cv2.waitKey(1) == ord('t'):
        state = not state
    if cv2.waitKey(1) == ord('r'):
        rec = "record"
    elif cv2.waitKey(1) == ord('s'):
        rec = "stop"
    elif cv2.waitKey(1) == ord('q'):
        break

    timeStamp(state)
    videoRec(rec)
    cv2.imshow('frame', frame)

cap.release()
out.release()
cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt")


cap = cv2.VideoCapture(0)  


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
 
    ret, frame = cap.read()
    
    if not ret:
        break  

   
    results = model(frame)

    
    annotated_frame = results[0].plot()  


    cv2.imshow("YOLOv8 Video Detection", annotated_frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))

background_frame = None
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Convert the current frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Store the first frame as background
    if background_frame is None:
        background_frame = gray_frame
        print("Background frame captured and stored.")
        continue  # Skip the rest of the loop after storing the background

    abs_diff = cv2.absdiff(background_frame, gray_frame)
    _, thresholded = cv2.threshold(abs_diff, 25, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 500: 
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw a green rectangle around the detected object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Add "UNSAFE" text in red color on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "UNSAFE", (x, y - 10), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        
    out.write(frame)
    cv2.imshow("Motion Detection", frame)

    # Wait for the user to press the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
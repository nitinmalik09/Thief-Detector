# Thief-Detector
The Thief Detection System uses Python and OpenCV to monitor video feeds for unauthorized movement. It compares current frames with a stored background to detect motion, highlighting moving objects with a green bounding box and “UNSAFE” label. The system records and saves the video for security purposes.
Core Features:
	1.	Motion Detection:
The system utilizes a method called frame differencing to detect motion. Initially, it captures a background frame and continuously compares it with the current video frame. The difference between the two frames is computed, and significant changes (such as moving objects) are identified.
	2.	Background Subtraction:
The first frame captured is set as the background frame. As the system processes the incoming video stream, any movement in the scene is detected by comparing each frame with the stored background. This technique allows the system to focus only on moving objects, excluding stationary elements in the environment.
	3.	Thresholding and Contour Detection:
The system applies a threshold to the absolute difference between frames to create a binary image (black and white). Any areas of the frame with significant changes are highlighted. The contours of these areas are detected and analyzed to determine if they represent significant movement, such as a person walking through the frame.
	4.	Bounding Box and Alert:
When motion is detected, the system draws a green bounding box around the moving object. Additionally, it labels the object as “UNSAFE” in red text to alert the user to the potential threat. This visual cue provides immediate feedback to the user, signaling the presence of an intruder or other unusual activity.
	5.	Recording and Saving Video:
The system records the video feed with the detected motion and saves it as an output.avi file. This recorded footage can be reviewed later for investigation or evidence.

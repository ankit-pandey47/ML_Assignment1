# import cv2
# cap = cv2.VideoCapture(0)

# status , photo = cap.read()
# cv2.imwrite("ankit.png" , photo)


# cv2.imshow("ankit.png" , photo)
# cv2.waitKey(100000)

import cv2

# Start video capture from the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture each frame from the camera
    ret, frame = cap.read()

    # If the frame is captured successfully
    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame to the user (camera feed)
    cv2.imshow('Camera Feed', frame)

    # Wait for user to press any key
    key = cv2.waitKey(1)  # Wait for 1 millisecond for key press

    # If the user presses any key (other than ESC)
    if key != -1:
        # Save the current frame as a picture (e.g., "user_image.png")
        cv2.imwrite("user_image.png", frame)
        print("Picture saved as 'user_image.png'")

        # Exit the loop if key is pressed
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()


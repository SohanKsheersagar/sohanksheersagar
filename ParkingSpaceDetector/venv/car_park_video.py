import cv2
import pickle

# Load image
img = cv2.imread('carParImg.jpeg')
img_height, img_width = img.shape[:2]

# Load video
cap = cv2.VideoCapture('carPark.mp4')

# Load positions
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Rectangle size in the image
width, height = 107, 48

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, frame = cap.read()
    if not success:
        break

    # Resize the video frame to match the image resolution
    frame = cv2.resize(frame, (img_width, img_height))

    for pos in posList:
        # Draw rectangles based on the positions in the posList
        cv2.rectangle(frame, pos,
                      (pos[0] + width, pos[1] + height),
                      (255, 0, 255), 2)

    cv2.imshow("image", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

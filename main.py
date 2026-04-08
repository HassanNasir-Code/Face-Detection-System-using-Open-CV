import cv2 #imports open Cv

face_class = cv2.CascadeClassifier( #constructor takes a path to a trained file xml
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

Rec = cv2.VideoCapture(0) #allows acess to device camers

def ID_Face(vid): #detect faces and draw a box around the head
    gray_img = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    face = face_class.detectMultiScale(gray_img, 1.1, 5, minSize= (40, 40))
    for (x, y, w, h) in face:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4 )
        return face
    
while True: #creates a loop allowing for real time detection

    result, video_frame = Rec.read()
    if result is False:
        break

    face = ID_Face(
        video_frame
    )

    cv2.imshow(
        'Detection Proj', video_frame
    )
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Rec.release()
cv2.destroyAllWindows()

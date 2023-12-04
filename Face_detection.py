import cv2
import os
from mtcnn.mtcnn import MTCNN

class Face_detection:
    def __init__(self, dir, outputdir):
        self.dir = dir
        self.outputdir = outputdir
        self.face_detect()
        
    def face_detect(self):
        detector = MTCNN(min_face_size=20)

        for filename in os.listdir(self.dir):
            if filename.endswith(".jpg"):
                frame_path = os.path.join(self.dir, filename)
                frame = cv2.imread(frame_path)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faces = detector.detect_faces(rgb_frame)
                for face in faces:
                    x, y, width, height = face['box']
                    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
                output_frame_path = os.path.join(self.outputdir, f"frame_{filename}")
                cv2.imwrite(output_frame_path, frame)
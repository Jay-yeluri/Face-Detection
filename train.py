import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create() # it recognises the face in camera
path = "Dataset"


def get_images_with_id(path):
    images_paths=[os.path.join(path,f)for f in os.listdir(path)] # set iimages path to os
    faces = []
    ids = []
    for single_image_path in images_paths:
        faceImg = Image.open(single_image_path).convert('L') #image converted int gray color
        faceNp = np.array(faceImg,np.uint8)
        id= int(os.path.split(single_image_path)[-1].split(".")[1].strip())
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)

    return np.array(ids),faces
ids,faces = get_images_with_id(path)
recognizer.train(faces,ids)
recognizer.save("recognizer/training.yml")
cv2.destroyAllWindows()



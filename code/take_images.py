import cv2
import numpy as np

raw = cv2.VideoCapture("/home/mangrich/lab/testes/input/carphone_qcif.y4m")



compressed = cv2.VideoCapture("/home/mangrich/lab/testes/decoded/decoded_fast_carphone_qcif.y4m")




raw_images = []

c = 0
while True:
    sucess_raw, image_raw = raw.read()
    if sucess_raw:
        if c in(0,20,40,60,80,100):
            raw_images.append(image_raw)
            
            if c == 100:
                break
        c+=1

raw.release()
cv2.destroyAllWindows()


compressed_images = []

c = 0
while True:
    sucess_compressed, image_compressed= compressed.read()
    if sucess_compressed:
        if c in (0,20,40,60,80,100):
            compressed_images.append(image_compressed)
            
            if c ==100:
                break
        c+=1
        
compressed.release()
cv2.destroyAllWindows()

for i in range(len(raw_images)):

    new = np.concatenate((raw_images[i],compressed_images[i]), axis=1)

    cv2.imwrite(f'carphone_qcif/{i}.png',new)

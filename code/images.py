import cv2
import numpy as np

def get_frames(input,frames_list):
    video = cv2.VideoCapture(input)
    images_list = []
    c = 0
    while True:
        sucess, image = video.read()
        if sucess:
            if c in frames_list:
                resize = cv2.resize(image,dsize=(1280,960), interpolation=cv2.INTER_CUBIC)
                images_list.append(resize)
                if c == frames_list[-1]:
                    break
            c+=1

    video.release()
    cv2.destroyAllWindows()

    return images_list

def add_border(image,border_thickness=5,color=[255,255,255]):
    new_image = cv2.copyMakeBorder(image, border_thickness, border_thickness, border_thickness, border_thickness, cv2.BORDER_CONSTANT, value=color)
    return new_image


def add_border_and_text(image,text):
    black_border = add_border(image,3,[0,0,0])
    white_border = add_border(black_border,50)
    texted_image =cv2.putText(img=np.copy(white_border), text=text, org=(50,30),fontFace=2, fontScale=1, color=(0,0,0), thickness=2)
    return texted_image


a_frames = get_frames('RAW_files/carphone_qcif.y4m',[0,10,20,30,40,50,60])
b_frames = get_frames('decoded_files/fast_carphone.y4m',[0,10,20,30,40,50,60])

for i in range(len(a_frames)):
    a = add_border_and_text(a_frames[i],'Original')
    b = add_border_and_text(a_frames[i],'Compressed')
    new = np.concatenate((a,b), axis=1)
    cv2.imwrite(f'carphone_qcif/{i}.png',new)


import cv2

from method.Image_Storage import ImageStorage


def img_blanco_negro(img):
    img_bn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_bn


def adaptative_mean(img):
    img = cv2.medianBlur(img, 5)
    img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    return img2

def adaptative_gaussian(img):
    img = cv2.medianBlur(img, 5)
    img3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    return img3

if __name__ == '__main__':
    img = ImageStorage.read_image("images/dave.jpg")
    img_bn = img_blanco_negro(img)
    th2 = adaptative_mean(img_bn)
    th3 = adaptative_gaussian(img_bn)
    ImageStorage.save_img(img=img_bn, name_img="blanco y negro")
    ImageStorage.save_img(img=th2, name_img="adaptative mean")
    ImageStorage.save_img(img=th3, name_img="adaptative gaussian")
    print("El proyecto corrio exitosamente")





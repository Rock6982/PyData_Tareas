import cv2


class ImageStorage:

    @staticmethod
    def read_image(path_img):
        if isinstance(path_img, str):
            img = cv2.imread(path_img)
            img = cv2.medianBlur(img, 5)
            return img
        else:
            print("formato no valido")
            return None

    @staticmethod
    def save_img(img, name_img):
        name_img = name_img + ".jpg"
        cv2.imwrite(name_img, img)


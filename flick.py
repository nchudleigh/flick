import numpy as np
from PIL import ImageGrab, Image
import cv2
import time


def process(screen):
    return cv2.Canny(screen, 25, 25)


def grab_screen():
    box = (0, 0, 2880, 1800)
    return np.array(ImageGrab.grab(box))


def show_screen(screen):
    Image.fromarray(screen).show()


def main():
    screen = grab_screen()
    screen = process(screen)
    show_screen(screen)

    # x1, y1, width, height
    # cv.ShowImage('window', edges)
    #
    # if cv.WaitKey(25) & 0xFF == ord('q'):
    #     cv.destroyAllWindows()
    #     break


print('OpenCV version', cv2.__version__)
main()

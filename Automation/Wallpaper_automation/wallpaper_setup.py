import cv2
import os
import random as rd
import ctypes
from time import sleep

images = []
lst_img = []
for root, _, img in os.walk(r'E:\Wallpaper'):
    for i in img:
        if i.endswith(".jpg"):
            print(i)
            im = cv2.imread(r"E:\Wallpaper\{0}".format(i))
            # os.rename("{0}\{1}".format(root, i), r"E:\a\{0}.jpg".format(seq))
            if os.stat("{0}\{1}".format(root, i)).st_size <= 10000:
                os.remove("{0}\{1}".format(root, i))
            h, w, _ = im.shape
            if h == 1080:
                images.append(i)
                set(images)
wallpaper = rd.choice(images)
# set(wallpaper)
# print(wallpaper)
out_write = open(r'E:\py projects\wallpaper_automation\wallpaper.txt', 'a+')
out_read = open(r'E:\py projects\wallpaper_automation\wallpaper.txt', 'r+')
f_read = out_read.read().split("\n")
if len(images) != len(f_read):
    while True:
        if wallpaper not in f_read[:-1]:
            out_write.write(wallpaper + "\n")
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, "E:\Wallpaper\{0}".format(wallpaper), 0)
            lst_img.append(wallpaper)
            break
        elif wallpaper in f_read[:-1]:
            wallpaper = rd.choice(images)


elif len(images) == len(f_read):
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, r"E:\Wallpaper\{0}".format(wallpaper), 0)
    out_write.truncate(0)

out_write.close()
out_read.close()

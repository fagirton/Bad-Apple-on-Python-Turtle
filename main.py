from turtle import *
import cv2
import time

#ht()
speed(0)
setup(width=480,height=360)
setundobuffer(0)
penup()
goto(-240,180)
print(pos())
delay(0)
tracer(0,0)
for i in range(1, 6577):
    start = time.time()
    f=cv2.imread('img\i'+ str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    clear()
    for y in range(0,len(f)):
        for x in range(0, len(f[y])):
            if f[y][x]==255: penup()
            else: pendown()
            forward(1)
        setx(-240)
        sety(ycor()-1)
    update()
    goto(-240,180)
    end = time.time()
    print(i, end - start)


#f=cv2.imread('img\i'+ str(123) + '.png', cv2.IMREAD_GRAYSCALE)
#for y in range(0,len(f)):
#    for x in range(0, len(f[y])):
#        forward(1)
#        if int(f[y][x])==0:
#            pendown()
#        if int(f[y][x])==255:
#           penup()
#    back(len(f[y]))
#    sety(ycor()-1)
#update()
#goto(-240,180)

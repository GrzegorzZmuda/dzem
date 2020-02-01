import pygame
import numpy as np
import pygame.surfarray as sfr
import time
import random
import math
from sys import exit

def col(map,posx,posy,deg):
    dist=1

    tracex=posx
    tracey=posy
    for i in range(200):
        dist=dist+1
        tracex=tracex+0.02*np.sin(np.deg2rad(deg)+45)
        tracey=tracey+0.02*np.sin(np.deg2rad(deg)+135)

        tmpposx=int(round(tracex))
        tmpposy=int(round(tracey))
        if map[tmpposx][tmpposy]==1:

            break

    return 200 - dist



def newscr(screen,map,posx=6,posy=6,rot=0):


    for i in range(len(screen)):
        deg=int((i)*90/len(screen))+90*rot

        tmp=col(map,posx,posy,deg)
        tmp2=tmp // 10
        for j in range(tmp//10):
            screen[i][30-tmp2+j][2]=tmp



    return 0


def rotl(a):
    if a<3:
        return a+1
    else:
        return 0

def rotr(a):
    if a>0:
        return a-1
    else:
        return 3

def conv(a,b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j][0]=a[int(i//8)][int(j//8)][0]
            b[i][j][1] = a[int(i // 8)][int(j // 8)][1]
            b[i][j][2] = a[int(i // 8)][int(j // 8)][2]

actual = np.ndarray((90,40,3))
scr =np.ndarray((720,320,3))

map=np.ndarray((10,10))
for i in range(len(map)):
    for j in range(len(map[0])):
        if i ==0 or i==9:
            map[i][j]=1
        if j==0 or j==9:
            map[i][j]=1
        if i ==5 and 2<j<8:
            map[i][j]=1

pygame.init()
screen = pygame.display.set_mode((720,320))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


conv(actual,scr)
sfr.make_surface(scr)

rot=1
x=6
y=5
Running=True
while Running:

    actual = np.zeros((90, 40, 3))
    newscr(actual,map,x,y,rot)
    conv(actual, scr)
    surf = pygame.surfarray.make_surface(scr)
    screen.blit(surf, (0, 0))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and x<9 and map[x+1][y]!=1:
                x=x+1
            elif event.key == pygame.K_d and y<9 and map[x][y+1]!=1:
                y=y+1
            elif event.key == pygame.K_w and x>0 and map[x-1][y]!=1:
                x=x-1
            elif event.key == pygame.K_a and y>0 and map[x][y-1]!=1:
                y=y-1
            elif event.key == pygame.K_q :
                rot=rotr(rot)
            elif event.key == pygame.K_e :
                rot=rotl(rot)


sfr.make_surface(scr)


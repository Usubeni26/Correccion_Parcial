import array
import math
import machine

from machine import mem32
LR=array.array("l",[0,0])
P0=array.array("l",[0,0])
P1=array.array("l",[0,0])
P2=array.array("l",[0,0])
P3=array.array("l",[0,0])
P4=array.array("l",[0,0])
a=0
n=4
dir_LR=mem32[a]
dir_P0=mem32[a+8]
dir_P1=mem32[a+16]
dir_P2=mem32[a+24]
dir_P3=mem32[a+32]

def Bezier array.array P0,array.array P1,array.array P2,array.array P3,n
    for j in range(1,4)
        t=j/n
        if j == 1
            dir_LR.mem32(a+32)=dir_P0.mem32(a)*(1-t)*(1-t)*(1-t)
        else
        if j == 2
            dir_LR.mem32(a+40)=dir_P1.mem32(a+8)*3*(1-t)*(1-t)*t
        else
        if j == 3
            dir_LR.mem32(a+48)=dir_P2.mem32(a+24)*3*(1-t)*t*t
        else
        if j == 4
            dir_LR.mem32(a+56)=dir_P2.mem32(a+24)*t*t*t
    for i in range(1,4)
        t=i/n
        if j == 1
            dir_LR.mem32(a+32)=dir_P0.mem32(a+4)*(1-t)*(1-t)*(1-t)
        else
        if j == 2
            dir_LR.mem32(a+40)=dir_P1.mem32(a+12)*3*(1-t)*(1-t)*t
        else
        if j == 3
            dir_LR.mem32(a+48)=dir_P2.mem32(a+20)*3*(1-t)*t*t
        else
        if j == 4
            dir_LR.mem32(a+56)=dir_P2.mem32(a+28)*t*t*t
    LR=lista_retornada
    return LR
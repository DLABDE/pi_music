#_*_coding:utf-8_*_
import os
import glob
import pygame
import eyed3
import time
import random

#获取音乐列表
def getmusic():
    mp='/home/pi/Music'
    hq=glob.glob('{}/*.mp3'.format(mp))
    return hq

#打印音乐列表
def mps(mps):
    n=1
    print('音乐列表')
    for mp in mps:
        print(str(n)+'.'+mp.split('/')[-1])
        n=n+1

#顺序播放
def lplay(musics):
    for music in musics:
        play(music)
    return 0

#播放mp
def play(mp):
    print('正在播放:'+mp.split('/')[-1])
    m_sleep=getmp(mp)
    pygame.mixer.music.load(mp)
    pygame.mixer.music.play()
    time.sleep(m_sleep)
    pygame.mixer.music.stop()
    time.sleep(5)

#获取音频时长
def getmp(mp):
    time=eyed3.load(mp)
    print('时长:{}s'.format(time.info.time_secs))
    return time.info.time_secs

def get():
    a=input('\n0:退出\n1:顺序播放\n2:随机播放\n3:选歌\n4:搜索\n')
    return a

#随机播放
def splay(musics):
    while 1:
        mp=random.choice(musics)
        play(mp)
        
#选歌
def xplay(musics):
    n=0
    dir=fir(musics)
    os.system('clear')
    print('音乐列表:\n')
    for music in musics:
        print(str(n)+'.'+music.split('/')[-1])
        n=n+1
    while 1:
        try:
            m=int(input('播放:'))
        except:
            print('输入错误')
            continue
        if (m>=0) and (m<n):
            mp3=dir[m]
            play(mp3)
        else:
            break
    return 0

#获取音乐字典
def fir(musics):
    n=0
    dir={}
    for music in musics:
        dir[n]=music
        n=n+1
    return dir

#搜索
def sou(musics):
    os.system('clear')
    s=input('搜索:')
    n=0
    sn={}
    for music in musics:
        if s in music.split('/')[-1]:
            sn[n]=music
            n=n+1
    while 1:
        os.system('clear')
        for ss in sn.keys():
            print(str(ss)+'.'+sn[ss].split('/')[-1])
        try:
            a=int(input('播放:'))
        except:
            print('输入错误')
            continue
        if (a>=0) and (a<n):
            play(sn[a])
        else:
            break
    return 0

def main():
    pygame.mixer.init()
    while 1:
        os.system('clear')
        musics=getmusic()
        mps(musics)
        try:
            a=int(get())
        except:
            print('输入错误')
            continue
        if a==1:
            lplay(musics)
        elif a==2:
            splay(musics)
        elif a==3:
            xplay(musics)
        elif a==4:
            sou(musics)
        elif a==0:
            break
        else :
            continue
    return 0
main()
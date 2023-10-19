```python
（1）创建乌龟模块，定义乌龟类
import pygame

class Turtle(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        #生成乌龟图像
        self.image = pygame.image.load("images/turtle.png").convert_alpha()
        #获取位置
        self.rect = self.image.get_rect() 
        self.width, self.height = bg_size[0],bg_size[1]   #用于限制获得范围
        #用于定位
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width)//2, \
                        (self.height - self.rect.height) //2
（2）创建主模块（main.py）
import pygame
import sys
import traceback    #为了更好退出
from pygame.locals import *

import turtle       #导入自己编写的乌龟模块

pygame.init()
pygame.mixer.init()     #混音器初始化（可以省略）

bg_size = width, height = 800,600            #规定窗体大小
screen = pygame.display.set_mode(bg_size)    #创建窗体
pygame.display.set_caption("模拟游戏开发——大龟吃小鱼")    #设置窗体标题
background = pygame.image.load('images/bg_image.jpg').convert_alpha()   #加载背景图片
clock = pygame.time.Clock()

#载入游戏音乐
pygame.mixer.music.load("music/bg_music.ogg")
pygame.mixer.music.set_volume(0.2)
die_sound = pygame.mixer.Sound("music/die.wav")
die_sound.set_volume(0.2)
eat_sound = pygame.mixer.Sound("music/eat.wav")
eat_sound.set_volume(0.3)
warn1_sound = pygame.mixer.Sound("music/warn1.wav")
warn1_sound.set_volume(0.2)
seaWater_sound = pygame.mixer.Sound("music/seaWater.wav")
seaWater_sound.set_volume(0.2)
bigger_sound = pygame.mixer.Sound("music/bigger.wav")
bigger_sound.set_volume(0.2)

def main():
    pygame.mixer.music.play(-1)       #无限循环播放bg_music
 
    tur = turtle.Turtle(bg_size)      #生成乌龟对象
    running = True                    #游戏循环运行条件

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()   #解决关闭窗口不退出问题
                sys.exit()
        #绘制背景图片 
        screen.blit(background,(0,0))
        #绘制乌龟
        screen.blit(tur.image,(tur.rect.left,tur.rect.top))

        pygame.display.flip()   #刷新页面
        clock.tick(60)          #设置帧率为每秒60帧
        
if __name__ == "__main__":
    try:
            main()
    except SystemExit:
            pass
    except:
            traceback.print_exc()
            pygame.quit()
            input()


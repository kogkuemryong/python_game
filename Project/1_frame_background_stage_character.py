import pygame
from random import *
import os
#################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Pang') # 게임 이름

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰드 , 속도 등)
current_path = os.path.dirname(__file__) # 현재파일의 위치를 반환
image_path = os.path.join(current_path, 'images') # image 폴더 위치 반환

# 배경 화면
background = pygame.image.load(os.path.join(image_path,'background.png'))

# 무대
stage = pygame.image.load(os.path.join(image_path,'stage.png'))
stage_size = stage.get_rect().size
stage_heigth = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위함


# 캐릭터
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_heigth


running= True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스 등)

    # 3. 게임 캐릭터 위치 정의

    # 4. 충동 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0, screen_height-stage_heigth))
    screen.blit(character, (character_x_pos, character_y_pos))



    pygame.display.update() # 게임화면을 다시 그르기!

# pygame 종료
pygame.quit()

# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

'''
[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떠어짐, x 좌표는 랜덤으로  설정
3. 캐릭터가 똥을 피하면 다음 똥이다시 떨어짐
4. 캐릭터가 똥과 출동하면 게임 종료
5. FPS 는 30 으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - backgrount.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70 * 70 - enemy.png
'''

import pygame
from random import *

#################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Quiz') # 게임 이름

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰드 , 속도 등)

# 배경
background= pygame.image.load('C:/workspaces/python_game/backgroud.png')

# 캐릭터
character = pygame.image.load('C:/workspaces/python_game/character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

# 정
enemy = pygame.image.load('C:/workspaces/python_game/enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = randint(0,screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10


# 이동 좌표
to_x = 0

# 이동 속도
speed = 0.6

running= True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. 게임 캐릭터 위치 정의
    # 실제 캐릭터의 포지션 값에 다가 넣어둠
    character_x_pos += to_x * dt

    # 화면 밖으로 캐릭터가 나가는 것 방지


    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(0,screen_width - enemy_width)


    # 4. 충동 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print('충돌했습니다.')
        running = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


    pygame.display.update() # 게임화면을 다시 그르기!

# pygame 종료
pygame.quit()

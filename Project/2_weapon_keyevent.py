import pygame
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

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

running= True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed

            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed

            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos <= 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정 - 아래에서 위로 쭉 올라가는 모양
    # 100 , 200 -> x는 그대로 y는 180, 160, 140 ... y는 스피드 만큼 빼줘야 함
    # 500, 200-> 180,160,140...
    weapons = [ [w[0], w[1] - weapon_speed]for w in weapons] # 무기 위치를 위로 올림
    # w[0]-x축 , w[1]-y축 = weapons_speed 한 값을 하나의 리스트로 감쌈

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0 ] # y좌표가 0보다 큰것만

    # 4. 충동 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    for weapon_x_pos , weapon_y_pos in weapons:
        screen.blit (weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage,(0, screen_height-stage_heigth))
    screen.blit(character, (character_x_pos, character_y_pos))




    pygame.display.update() # 게임화면을 다시 그르기!

# pygame 종료
pygame.quit()

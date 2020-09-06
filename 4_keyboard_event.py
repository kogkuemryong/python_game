import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경이미지 불러오기
backgroud = pygame.image.load('C:/workspaces/python_game/backgroud.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('C:/workspaces/python_game/character.png')
character_size = character.get_rect().size # 가로,세로의 크기를 가져옴 : 이미지 크기를 구해옴
charcater_width = character_size[0] # 캐릭터의 가로 크기
charcater_height = character_size[1] # 캐릭터의 세로 크기
charcater_x_pos = (screen_width / 2) - (charcater_width / 2) # 화면 크기 절반 크기에 해당하는 곳에 위치(가로 - 중앙)
charcater_y_pos = screen_height - charcater_height # 화면 세로 키 가장 아래 해당하는 곳에 위치(세로 - 맨밑640)

# 이동할 좌표
to_x = 0
to_y = 0

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game') # 게임 이름

# 이벤트 루프 - 계속 돌아가야지 꺼지지 않도록 대기
running= True # 게임이 진핸중인가?
while running:
    for event in pygame.event.get(): # 이벤트 발생(유무)
        if event.type == pygame.QUIT: # 파일을 끄게 되면 if문 수행 (유무)
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 이동
                to_x -= 5 # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 이동
                to_x += 5 # to_x = to_x + 5
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로 이동
                to_y -= 5
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래쪽으로 이동
                to_y += 5

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 실제 캐릭터의 포지션 값에 다가 넣어줌
    charcater_x_pos += to_x
    charcater_y_pos += to_y

    # 화면 밖으로 캐릭터가 나가는 것 방지

    # 가로 경계값 처리
    if charcater_x_pos < 0:
        charcater_x_pos = 0
    elif charcater_x_pos > screen_width - charcater_width:
        charcater_x_pos = screen_width - charcater_width

    # 해로 경계값 처리
    if charcater_y_pos < 0:
        charcater_y_pos = 0
    elif charcater_y_pos > screen_height - charcater_height:
        charcater_y_pos = screen_height - charcater_height



    screen.blit(backgroud,(0,0)) # 배경 그리기
    screen.blit(character,(charcater_x_pos, charcater_y_pos))

    pygame.display.update() # 게임화면을 다시 그르기!

# pygame 종료
pygame.quit()

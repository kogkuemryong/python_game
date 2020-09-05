import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game') # 게임 이름

# 이벤트 루프 - 계속 돌아가야지 꺼지지 않도록 대기
running= True # 게임이 진핸중인가?
while running:
    for event in pygame.event.get(): # 이벤트 발생(유무)
        if event.type == pygame.QUIT: # 파일을 끄게 되면 if문 수행 (유무)
            running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()

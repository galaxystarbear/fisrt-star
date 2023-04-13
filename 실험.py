
import pygame, sys
import random 
import os
###################################################################
#기본 초기화(반드시 해야할것)
pygame.init()

# 화면 크기 설정
screen_width= 640
screen_height= 900
screen= pygame.display.set_mode((screen_width,screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("운석 피하기 게임")

#FPS
clock= pygame.time.Clock()
################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load("C:\\Users\\goldc\\Desktop\\민준이꺼\\python\\동아리 과제.py\\운석 피하기 게임\\images.jfif")
start_background= pygame.image.load("C:\\Users\\goldc\\Desktop\\민준이꺼\\python\\동아리 과제.py\\운석 피하기 게임\\start_background.png")
game_font= pygame.font.Font(None, 40)
#이름 쓰기
base_font= pygame.font.Font(None,32)
user_text = ''

ddong="C:\\Users\\goldc\\Desktop\\민준이꺼\\python\\동아리 과제.py\\운석 피하기 게임\\운석.png"

input_rect= pygame.Rect(110,200,140,20)
color= pygame.Color('lightskyblue3')
white= (255,255,255)
green=(63,53,153)
# 학번=game_font.render(("Student ID:"), True, (227,222,30))
# 설명=game_font.render(("control : "), True, (10,10,10))

#함수 정의
def display_start_screen():
    screen.blit(start_background,(0,0))
    text_surface = base_font.render(user_text, True, white)
    screen.blit(text_surface,(input_rect.x + 10, input_rect.y + 5))
    input_rect.w = max(20,text_surface.get_width() +10)

def creating_enemy(name):
    name.name_size = name.get_rect().size 
    name.name_width = name.name_size[0] 
    name.name_height = name.name_size[1]
    name.name_x_pos = random.randint(0, screen_width-name.name_width)
    name.name_y_pos =-name.name_height
    return name.name_size, name.name_width, name.name_height, name.name_x_pos, name.name_y_pos
    
     



# 캐릭터 만들기
character=pygame.image.load("C:\\Users\\goldc\\Desktop\\민준이꺼\\python\\동아리 과제.py\\운석 피하기 게임\\character1.png")
character_size = character.get_rect().size 
character_width = character_size[1] 
character_height = character_size[1] 
character_x_pos = (screen_width /2) - (character_width/2) 
character_y_pos = screen_height-character_height 



# 이동 위치
to_x=0
to_y =0
character_speed= 0.1

#적 만들기

enemy1=pygame.image.load(ddong)
creating_enemy(enemy1)
enemy1_speed=0.6

enemy2=pygame.image.load(ddong)
creating_enemy(enemy2)
enemy2_speed=0.6

enemy3=pygame.image.load(ddong)
creating_enemy(enemy3)
enemy3_speed=0.6

enemy4=pygame.image.load(ddong)
creating_enemy(enemy4)
enemy4_speed=0.6



 #적1 만들기




#하트 만들기
heart_image= "C:\\Users\\goldc\\Desktop\\민준이꺼\\python\\동아리 과제.py\\운석 피하기 게임\\하트.png"
heart= pygame.image.load(heart_image)
heart1=pygame.image.load(heart_image)
heart2=pygame.image.load(heart_image)
heart_score=3



#아이템
item=pygame.image.load("C:\\Users\\goldc\\Desktop\\민준이꺼\\python\\동아리 과제.py\\운석 피하기 게임\\item.png")
item_size = item.get_rect().size 
item_width = item_size[0] 
item_height = item_size[1] 
item_x_pos = random.randint(0, screen_width-item_width)
item_y_pos = 0
item_speed=0.7


#점수
game_font= pygame.font.Font(None, 40)
game_font1= pygame.font.Font(None, 80)
player_font= pygame.font.Font(None,65)
score= 0
start_ticks = pygame.time.get_ticks()
score1 =game_font.render(("score:"), True, (100,100,100))


start= False
running= True
starting=False
######################################################################
#게임 진행
while running:
   
    dt= clock.tick(60)
    #게임 전에
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if start== False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text =user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(user_text)
                    start = True
                else:
                    user_text += event.unicode
        
                
  
    if start == True:
        starting=True
        
    else:
       display_start_screen()

    pygame.display.flip()
    
    
    
#게임 시작    
    if starting == True:
    #점수
    #경과 시간 경과
        elpased_score =(pygame.time.get_ticks() - start_ticks)/ 60
        total_score =game_font.render(str(int(score + elpased_score)), True, (200,100,150))
        last_score= game_font.render ("Score : + {0}".format(total_score), True, (200,100,190))
        
        item_percent= random.randrange(1,100)
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
            #이동 키
        if event.type == pygame.KEYDOWN:
             pressed=pygame.key.get_pressed()
             if event.key == pygame.K_LEFT:
                 to_x -= character_speed
             elif event.key == pygame.K_RIGHT:
                 to_x += character_speed
             elif event.key== pygame.K_UP:
                 to_y -= character_speed
             elif event.key == pygame.K_DOWN:
                 to_y += character_speed 
             elif event.key==pygame.K_q:
                    heart_score +=1
            
        if event.type == pygame.KEYUP:   
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 to_x = 0
             elif event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                 to_y =0
    
    
    #게임 캐릭터 위치 정의
        character_x_pos += to_x *dt
        character_y_pos += to_y *dt
    
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width/2:
            character_x_pos = screen_width - character_width/2

        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height



    
    
    
        if enemy1_y_pos> screen_height:
            enemy1_y_pos= 0
            enemy1_x_pos = random.randint(0, screen_width-enemy1.enemy1_width)
    
        if enemy2_y_pos> screen_height:
            enemy2_y_pos= 0
            enemy2_x_pos = random.randint(0, screen_width-enemy2.enemy2_width)

        if enemy3_y_pos> screen_height:
            enemy3_y_pos= 0
            enemy3_x_pos = random.randint(0, screen_width-enemy3.enemy3_width)

        if enemy4_y_pos> screen_height:
            enemy4_y_pos= 0
            enemy4_x_pos = random.randint(0, screen_width-enemy4.enemy4_width)
    
        if item_y_pos> screen_height:
            item_y_pos= 0
            item_x_pos = random.randint(0, screen_width-item_width)
    
        if score + elpased_score >= 0:
           enemy1_y_pos+= enemy1_speed*dt
        
        if score + elpased_score >= 100:
           enemy1_y_pos+= enemy2_speed*dt
    
        if score + elpased_score >= 300:
            enemy2_y_pos+= enemy3_speed*dt

        if score + elpased_score >= 500:
            enemy3_y_pos += enemy4_speed*dt


    
        if item_percent >=90:
            item_y_pos+=item_speed*dt

    
         #4. 충돌처리

    
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos
    
    
        enemy1_rect = enemy1.get_rect()
        enemy1_rect.left = enemy1_x_pos
        enemy1_rect.top = enemy1_y_pos
    
        enemy2_rect = enemy2.get_rect()
        enemy2_rect.left = enemy2_x_pos
        enemy2_rect.top = enemy2_y_pos

        enemy3_rect = enemy3.get_rect()
        enemy3_rect.left = enemy3_x_pos
        enemy3_rect.top = enemy3_y_pos

        enemy4_rect = enemy4.get_rect()
        enemy4_rect.left = enemy4_x_pos
        enemy4_rect.top = enemy4_y_pos

    
        item_rect = item.get_rect()
        item_rect.left = item_x_pos
        item_rect.top = item_y_pos



    
        if character_rect.colliderect(enemy1_rect):
            heart_score -=1
            enemy1_y_pos= 0
            enemy1_x_pos = random.randint(0, screen_width-enemy1.enemy1_width)

        elif character_rect.colliderect(enemy2_rect):
            heart_score -=1
            enemy2_y_pos= 0
            enemy2_x_pos = random.randint(0, screen_width-enemy1.enemy2_width)

        elif character_rect.colliderect(enemy3_rect):
            heart_score -=1
            enemy3_y_pos= 0
            enemy3_x_pos = random.randint(0, screen_width-enemy3.enemy3_width)

        elif character_rect.colliderect(enemy4_rect):
            heart_score -=1
            enemy4_y_pos= 0
            enemy4_x_pos = random.randint(0, screen_width-enemy4.enemy4_width)
        

        elif character_rect.colliderect(item_rect):
            heart_score +=1
            item_y_pos= 0
            item_x_pos = random.randint(0, screen_width-item_width)
            
    
    #생명
        if heart_score > 3:
            heart_score=3
    
        if heart_score == 0:
            game_result= 'Game Over' 
            game_result1= 'Score : {0}'.format(int(score + elpased_score))
            running= False
    
    
   
    #5.화면에 그리기
        screen.blit(background, (0, 0)) 
        screen.blit(character, (character_x_pos, character_y_pos)) 
        screen.blit(enemy1, (enemy1_x_pos, enemy1_y_pos))
        screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))
        screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos))
        screen.blit(enemy4, (enemy4_x_pos, enemy4_y_pos))

        screen.blit(total_score, (92,13))
        screen.blit(score1,(0,10))
        screen.blit(item, (item_x_pos, item_y_pos))


        if heart_score >= 3:
            screen.blit(heart,(-150, -350))
            screen.blit(heart1, ( -90,-350))
            screen.blit(heart1, ( -30,-350))
            pygame.display.update()

        elif heart_score == 2:
            screen.blit(heart1, ( -90,-350))
            screen.blit(heart1, ( -30,-350))
            pygame.display.update()

        elif heart_score == 1:
            screen.blit(heart1, ( -30,-350))
            pygame.display.update()
    
        pygame.display.update()
######################################################################################################################
# 마무리   
ending_background= pygame.image.load("C:\\Users\\goldc\\Desktop\\민준이꺼\\python\\동아리 과제.py\\운석 피하기 게임\\ending_background.png")
screen.blit(ending_background, (0,0))
pygame.display.update()
#점수 표시
user_name= "player : {0}".format(str(user_text))
msg = game_font1.render(game_result, True, (25,25,112))
msg1 = game_font1.render(game_result1, True, (25,25,112))
player = player_font.render(user_name,True,(25,25,112))
msg_rect= msg.get_rect(center=(int(screen_width /2), int(screen_height /2 - 50)))
msg_rect1= msg1.get_rect(center=(int(screen_width /2), int(screen_height /2 )))
user_name_rect= player.get_rect(center=(int(screen_width /2), int(screen_height /2 - 90)))

#마지막 화면에 표시(Game Over)
screen.blit(msg, msg_rect)

pygame.display.update()
pygame.time.delay(1500)

#마지막 화면에 표시(플레이어, 점수)
screen.blit(ending_background, (0,0))
screen.blit(msg1, msg_rect1)
screen.blit(player, user_name_rect)
print(game_result1)
pygame.display.update()
pygame.time.delay(1500)


pygame.quit

f = open("기록.txt",'a')

결과 ="{0}님의 점수 : {1}\n".format(user_text,int(score + elpased_score))
f.write(결과)
f.close()

os.system('기록.txt')



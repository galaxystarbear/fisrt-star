import pygame,sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([480,640])
base_font= pygame.font.Font(None,32)
user_text = ''

def display_start_screen():
     screen.fill(black) 
     

def display_game_screen():
    screen.blit(background, (0, 0)) 
background = pygame.image.load("C:\\Users\\goldc\\Desktop\\민준이꺼\\background1.jpg")   


input_rect= pygame.Rect(140,200,140,30)
color= pygame.Color('lightskyblue3')
white= (255,255,255)
black=(0,0,0)
start= False
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if start== False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                   user_text =user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    start = True
                else:
                     user_text += event.unicode
     
    if start == True:
        display_game_screen()
        
    else:
        screen.fill(black)
        text_surface = base_font.render(user_text, True, (255,255,255))
        screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(20,text_surface.get_width() +10)
        pygame.draw.rect(screen,color,input_rect,2)

    pygame.display.flip()
    clock.tick(60)

    


pygame.quit
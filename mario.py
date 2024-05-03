import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


character = pygame.image.load('p3_stand.png')
ground = pygame.image.load('grassMid.png')
grass = pygame.image.load('grassHalfMid.png')
grass_1 = pygame.image.load('grassHalfLeft.png')
grass_2 = pygame.image.load('grassHalfRight.png')
background = pygame.image.load('gory_reka_solntse_143529_1280x720.jpg')

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ground_witdh = 70
character_height = 92
screen_size_1 = 720
screen_size_2 = 1280
grass_x = [450, 850, 600]
grass_y = [550, 470, 300]
## Здесь писать начальные значения для переменных
dy = 0
vy = 0
g = 225
rest = False
a = 3

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    ## Здесь писать физику объектов
    min_y = screen_size_1 - ground_witdh
    for i in range(len(grass_x)):
        if player_pos.x + 33 >= grass_x[i] - ground_witdh and player_pos.x - 33 <= grass_x[i] + ground_witdh:
            if player_pos.y + character_height <= grass_y[i]:
                if min_y > grass_y[i]:
                    min_y = grass_y[i]
    min_y -= character_height


    if rest == False:
        vy += g * dt
        dy = vy * dt * a
        if player_pos.y + dy < min_y:
            player_pos.y += dy
        else:
            player_pos.y += dy
            rest = True
            vy = 0
            if player_pos.y > min_y:
                player_pos.y = min_y



    # fill the screen with a color to wipe away anything from last frame

    screen.blit(background, (0, 0))
    screen.blit(character, player_pos)
    k = 0
    for i in range(19):
        screen.blit(ground, (k, screen_size_1-ground_witdh))
        k += ground_witdh


    
    for i in range(3):
        screen.blit(grass, (grass_x[i], grass_y[i]) ) 
        screen.blit(grass_1, (grass_x[i] - ground_witdh, grass_y[i]) )
        screen.blit(grass_2, (grass_x[i] + ground_witdh, grass_y[i]) )
    
    ## Здесь писать реакции на кнопки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if rest == True:
            vy = -150
            rest = False
        
      
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


import pygame, random

def drawSquares():
    width = 300
    height = 300
    
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Test")
    
    clock = pygame.time.Clock()
    

    run = True

    while run:
        print(clock.tick(10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0))
        for x in range(int(width / 2)):
            for y in range(int(height / 2)):
                pygame.draw.rect(win,
                                (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255)),
                                 (x, y, 1, 1))
                pygame.draw.rect(win,
                                 (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255)),
                                 (x + int(width / 2), y, 1, 1))
                pygame.draw.rect(win,
                                 (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255)),
                                 (x, y + (height / 2), 1, 1))
                pygame.draw.rect(win,
                                 (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255)),
                                 (x + int(width / 2), y + (height / 2), 1, 1))
                
        pygame.display.update()




def movingSquare():
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Game Test")
    
    clock = pygame.time.Clock()
    
    x = 50
    y = 50
    width = 40
    height = 60
    vel = 5
    

    run = True

    while run:
        print(clock.tick(30))
        # Milliseconds
        #pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        if keys[pygame.K_RIGHT] and (x + width) < 500:
            x += vel
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and (y + height) < 500:
            y += vel
        
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255,0, 0), (x, y, width, height))
        pygame.display.update()
    
    

 
def main():
    # Have to initialize first
    pygame.init()

    drawSquares()
    
    pygame.quit()
        

if __name__=="__main__":
    main()

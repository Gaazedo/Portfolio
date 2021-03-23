import pygame

pygame.init()

larg, alt = 800, 500
cor_fundo = (255, 255, 255)

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Exercício 2")
tela.fill(cor_fundo)

walkLeft = [
    pygame.image.load("L1.png"),
    pygame.image.load("L2.png"),
    pygame.image.load("L3.png"),
    pygame.image.load("L4.png"),
    pygame.image.load("L5.png"),
    pygame.image.load("L6.png"),
    pygame.image.load("L7.png"),
    pygame.image.load("L8.png"),
    pygame.image.load("L9.png"),
]
walkRight = [
    pygame.image.load("R1.png"),
    pygame.image.load("R2.png"),
    pygame.image.load("R3.png"),
    pygame.image.load("R4.png"),
    pygame.image.load("R5.png"),
    pygame.image.load("R6.png"),
    pygame.image.load("R7.png"),
    pygame.image.load("R8.png"),
    pygame.image.load("R9.png"),
]

run = True
x = 100
y = 100
while run:
    tela.blit(walkRight[1],(x,y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i = 0 
                while i<9:
                    tela.blit(walkLeft[i], (x,y))
                    pygame.time.delay(50)
                    pygame.display.update()
                    tela.fill(cor_fundo)
                    i+=1
                    x-=10
            if event.key == pygame.K_RIGHT:
                for i in range(len(walkRight)):
                    mov = walkRight[i].get_rect()
                    tela.blit(walkRight[i],(x,y))
                    x+=10
                    pygame.time.delay(50)
                    pygame.display.update()
                    tela.fill(cor_fundo)
pygame.quit()

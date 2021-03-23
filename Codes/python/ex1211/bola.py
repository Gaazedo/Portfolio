import pygame, time

pygame.init()
width, height = 800, 600
BolaVelocidade = [1, 1]
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Exercício 1")

bola = pygame.image.load('bolafut.png')
bolaRect = bola.get_rect()

while True:
    screen.fill(backgroundColor)

    screen.blit(bola, bolaRect)
    bolaRect = bolaRect.move(BolaVelocidade)

    pygame.display.flip()
    time.sleep(10 / 1000)
    if bolaRect.left < 0  or bolaRect.right > width:
        BolaVelocidade[0] = -BolaVelocidade[0]
    
    if bolaRect.top < 0  or bolaRect.bottom > height:
        BolaVelocidade[1] = -BolaVelocidade[1]

pygame.quit()

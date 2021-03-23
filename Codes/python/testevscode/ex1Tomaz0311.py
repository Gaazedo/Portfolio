import pygame
pygame.init()
screen=pygame.display.set_mode((400, 400))
screen_rect=screen.get_rect()
player=pygame.Rect(180, 180, 20, 20)
pygame.display.set_caption("Não sair da tela")
sair = False

while not sair:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sair = True
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.move_ip(0, -1)
    if keys[pygame.K_a]: player.move_ip(-1, 0)
    if keys[pygame.K_s]: player.move_ip(0, 1)
    if keys[pygame.K_d]: player.move_ip(1, 0)
    player.clamp_ip(screen_rect) 
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), player)
    pygame.display.flip()

pygame.quit()

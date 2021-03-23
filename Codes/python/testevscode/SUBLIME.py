import pygame
pygame.init()
screen = pygame.display.set_mode((600,450))
pygame.display.set_caption("Brincando com as cores em Pygame")
i=0
while i< 255:
	red = i
	green = i//4
	blue = i
	screen.fill((red, green, blue))
	pygame.display.flip()
	pygame.time.wait(500)
	i=i+20
pygame.quit()
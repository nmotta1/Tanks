import pygame

width = 800
height = 600
margin = 20
size = [width, height]
image1 = pygame.image.load("missile.png")
screen = pygame.display.set_mode(size)


class Missile(pygame.sprite.Sprite):
	def __init__(self, speed, rebounds):
		super().__init__()
		self.speed = speed
		self.rebounds = rebounds
		
	def load(self):
		image1 = pygame.image.load(self.image)
		imagerect = image1.get_rect(center = (self.x, self.y))
		screen.blit(image1, imagerect)
	
	def explode(self):
		pygame.sprite.Sprite.remove(self)


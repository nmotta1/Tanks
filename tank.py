
import pygame
import os
from missile import Missile

width = 800
height = 600
margin = 20
size = [width, height]
image1 = pygame.image.load("goodtank.png")
screen = pygame.display.set_mode(size)


class Tank(pygame.sprite.Sprite):

	def __init__(self, image, x, y, lives, speed):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.speed = speed
		self.lives = lives
		self.x = x
		self.y = y
		self.colorkey = [0, 0, 0]
		self.alpha = 255
		
	def move(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			print("move")
			self.x += self.speed
			print(self.y)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:	
			print("move")		
			self.x -= self.speed
		if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			self.y -= self.speed		
		if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			self.y += self.speed

			
	def load(self):
		image1 = pygame.image.load(self.image)
		imagerect = image1.get_rect(center = (self.x, self.y))
		screen.blit(image1, imagerect)
		

##  	def draw(self, image1):
	# 	
	# 	self.img.set_colorkey(self.colorkey)
	# 	self.img.set_alpha(self.alpha)
	# 	screen.blit(image1, self.pos)
	# 	pygame.display.flip()


	def shootMissile():
		Missile.load(self)
	def bomb(): pass

class PlayerTank(Tank):
	def __init__(self, speed, lives, x, y):
		super().__init__(speed, lives, x, y) 
		self.color = "green"
		self.lives = 3
	

class EnemyTank(Tank):
	def __init__(self, speed):
		super().__init__() 
		self.color = "green"

# player1 = PlayerTank(10, 3)
# PlayerTank.draw(player1, myimage, 300, 300)
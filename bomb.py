
import pygame

class Bomb(pygame.sprite.Sprite):
	def __init__(self, damage):
		self.damage = damage
		
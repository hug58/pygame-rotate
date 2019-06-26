import pygame as pg 
import math 

SCREEN = pg.display.set_mode((400,400))
pg.display.set_caption("Rotate")

class Torre(pg.sprite.Sprite):
	def __init__(self,x,y):
		self.torreta = pg.image.load("torreta.png")
		self.torreta = pg.transform.scale(self.torreta,(100,120))

		self.image = self.torreta

		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y

		self.angle = 0

		self.pos = [self.rect.centerx,self.rect.centery]
		
		self.vlx = 3
		self.vly = 3

	def update(self):
		self.move()
		SCREEN.blit(self.image,self.rect)

		

		self.vlx = 0
		self.vly = 0

	def move(self):
		key = pg.key.get_pressed()

		if key[pg.K_RIGHT]:
			self.rotate(1)
		if key[pg.K_LEFT]:
			self.rotate(-1)

		if key[pg.K_UP]:

			radians = math.radians(self.angle)
			self.vlx = 5 * - math.sin(radians)
			self.vly = 5 * - math.cos(radians)

			if  1 >  self.vlx > 0:
				self.vlx = 1

			if  1 >  self.vly > 0:
				self.vly = 1


			self.rect.centerx += self.vlx	
			self.rect.centery += self.vly

			self.pos[0] = self.rect.centerx 
			self.pos[1] = self.rect.centery



	def rotate(self,xbool):

		if xbool == 1:
			self.angle += 3
			if self.angle >= 360: self.angle = 0
		else:
			self.angle -= 3
			if self.angle <= -360: self.angle = 0
		
		#self.image = pg.transform.rotozoom(self.torreta,self.angle,1)

		self.image = pg.transform.rotate(self.torreta,self.angle)
		self.rect = self.image.get_rect()
		
		self.rect.centerx = self.pos[0]
		self.rect.centery = self.pos[1]



def main():
	torreta = Torre(200,200)
	clock = pg.time.Clock()
	exit = False

	while exit != True:
		clock.tick(40)
		for e in pg.event.get():
			if e.type == pg.QUIT:
				exit = True



		SCREEN.fill((0,0,0))
		torreta.update()

		pg.display.flip()

main()
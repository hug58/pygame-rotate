import pygame as pg 

SCREEN = pg.display.set_mode((400,400))
pg.display.set_caption(" old rotate")

class Torre(pg.sprite.Sprite):
	def __init__(self,x,y):
		self.torreta = pg.image.load("torreta.png")
		self.image = self.torreta
		self.image = pg.transform.scale(self.image,(100,100))

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.angle = 0

	def update(self):
		self.move()
		SCREEN.blit(self.image,self.rect)

	def move(self):
		key = pg.key.get_pressed()

		if key[pg.K_RIGHT]:
			self.rotate(1)
		if key[pg.K_LEFT]:
			self.rotate(-1)


	def rotate(self,xbool):

		if xbool == 1:
			self.angle += 4
			if self.angle >= 360: self.angle = 0
		else:
			self.angle -= 4
			if self.angle <= -360: self.angle = 0
		
		self.image = pg.transform.rotate(self.torreta,self.angle)
		self.image = pg.transform.scale(self.image,(100,120))



def main():
	torreta = Torre(200,200)
	clock = pg.time.Clock()
	exit = False

	while exit != True:
		clock.tick(60)
		for e in pg.event.get():
			if e.type == pg.QUIT:
				exit = True



		SCREEN.fill((0,0,0))
		torreta.update()

		pg.display.flip()

main()
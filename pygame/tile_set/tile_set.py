import pygame as pg

archivo = open('map_0.txt','r')
map_0 = archivo.readlines()
archivo.close()


def quitar_ultimo_elemento(string):
	if string[-1] == '\n':
		return string[:-1]
	else:
		return string


map_0 = map(quitar_ultimo_elemento,map_0) #De esta forma quito todo los espacios '\n' de cada string
map_0 = list(map_0)

SPACEMAP = 20 #espacio del tile
"""total de columnas multiplicado por el espacio en cada tile, cada fila tiene la misma 
	cantidad de columna, da igual si se usa cualquiera de las filas"""
WIDTH = len(map_0[0])*SPACEMAP    
HEIGHT = len(map_0)*SPACEMAP #total de filas x sizemap
SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Tiles')
BACKGROUND = (100,200,100)

def tile(color):
    image = pg.Surface((20,20))
    image.fill(color)
    return image

class Tile_set:


	def __init__(self):
		self.map = map_0 

	def make_map(self):

		BLUE = (80,0,200)
		RED = (255,0,0)			

		tmp_surface = pg.Surface((WIDTH,HEIGHT))
		tmp_surface.fill(BACKGROUND)

		#Devuelve una fila[string] y numero de la fila actual
		for i,lista in enumerate(self.map):
			#Devuelve una columna[Caracter] y numero de la columna actual[Posicion del elemento]
			for j,tile_str in enumerate(lista):

				pos = (j*SPACEMAP,i*SPACEMAP)
				tile_str = tile_str.upper()
				

				if tile_str == 'X':
					tile_baldosa = tile(RED)
					tmp_surface.blit(tile_baldosa,pos)

				elif tile_str == 'Y':
					tile_baldosa = tile(BLUE)
					tmp_surface.blit(tile_baldosa,pos)


		return tmp_surface


def main():

	tile_set = Tile_set()
	surface = tile_set.make_map()

	exit = False
	while  exit != True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit = True


		SCREEN.blit(surface,(0,0))
		pg.display.flip()
		

	pg.quit()

if __name__ == '__main__':
	main()
	
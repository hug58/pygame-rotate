"""
Aveces es necesario pasar un elemento de la lista pero a su vez la posición, por
ejemplo, en un tileset
"""


lista = ['uno','dos','tres']
    

#LISTAR POSICIÓN CON ELEMENTO DE LA LISTA

#----------------recomendada forma

#Enumerate devuelve un objeto que a su vez se puede convertir en una lista

print("\nPrimera forma\n")
for i,j in enumerate(lista):
    print(i,j)
    
#----------------La misma pero la version larga
    
#ejemplo de enumerate paso a paso

lista_pos = enumerate(lista) #objeto
lista_pos = list(lista_pos) #convertir a lista
print("\nSegunda forma\n")
for i,j in lista_pos:
    print(i,j)

#----------------la forma novata

print("\nTercera forma\n")
for i in range(len(lista)):
    print(i,lista[i])

#----------------La peor peor forma

print("\nCuarta forma\n")
cont = 0
for i in lista:
    print(cont,i)
    cont +=1

#----------------Esta si es la PEOR forma

print("\nQuinta forma\n")
lista_5 = [(1,'uno'),(2,'dos'),(3,'tres')]

for i,j in lista_5:
    print(i,j)
    

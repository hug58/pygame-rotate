import socket
import threading as th
import json
import sys 
import os 

from time import sleep

class Server:

	def __init__(self,ip,port):

		self.clients = []

		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.s.bind((ip,port))
		self.s.listen(10)
		self.s.setblocking(False)

		ac = th.Thread(target= self.accept_client,daemon= True)
		ac.start()

		rc = th.Thread(target = self.recive,daemon = True)
		rc.start()

		while 1:
			data = input(">")
			if data == 'exit':

				self.s.close()
				sys.exit()
				break

	def recive(self):
	
		while True:

			if len(self.clients) > 0:


				for conn,addr in self.clients:            

					try:
						data =  conn.recv(1024)

						if data:
							
							print("")
							data = json.loads(data)
							
							print("Msj de {addr} :{data}".format(addr = addr,data = data))
							
							if data == "exit": 
								break
							
							self.msg_client(data,conn)                        


					except:
						pass

		#self.s.close()

	def msg_client(self,data,client):
			

		for conn,addr in self.clients:


			try:

				data = json.dumps(data)
				msg_decode = bytes(data,"utf-8")
					
				if client != conn:
					conn.send(msg_decode)

			except:
				self.clients.remove(client)

	def accept_client(self):

		print("Esperando conexión...")

		while 1:

			try:
				if len(self.clients) < 10:

					conn,addr = self.s.accept()
					conn.setblocking(False)
					print( "Conexión establecida con: {}".format(addr))
					self.clients.append((conn,addr))

				else:
					break

			except:
				pass





if __name__ == "__main__":

	
	if os.name != 'posix':
		host_name = s.gethostname()
		host_ip = s.gethostbyname(host_name)
		
	else:
		host_ip = input('INTRODUCE IP: ')

	
	port = input('INTRODUCE PORT: ')
	port = int(port)

	server = Server(host_ip,port)
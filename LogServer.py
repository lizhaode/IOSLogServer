from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
import time


class IOSLogServer(Protocol):
	def connectionMade(self):
		clientIP = str(self.transport.client[0]) + ':' + str(self.transport.client[1])
		print('Connection from', clientIP)

	def connectionLost(self, reason):
		clientIP = str(self.transport.client[0]) + ':' + str(self.transport.client[1])
		print(clientIP, 'disconnected!')

	def dataReceived(self, data):
		logdata = data.decode()
		self.writelog(self.transport.client[0], logdata)
		# print(logdata)
		# if logdata[24:30] == 'RENDER':
		#     filename = self.transport.client[0] + '_RENDER'
		#     self.writelog(filename,logdata)
		# elif logdata[24:29] == 'AUDIO':
		#     filename = self.transport.client[0] + '_AUDIO'
		#     self.writelog(filename,logdata)
		# elif logdata[24:32] == 'ESTORAGE':
		#     filename = self.transport.client[0] + '_ESTORAGE'
		#     self.writelog(filename,logdata)
		# elif logdata[24:30] == 'CAMERA':
		#     filename = self.transport.client[0] + '_CAMERA'
		#     self.writelog(filename,logdata)
		# elif logdata[24:27] == 'GPS':
		#     filename = self.transport.client[0] + '_GPS'
		#     self.writelog(filename,logdata)
		# elif logdata[24:30] == 'NOTIFY':
		#     filename = self.transport.client[0] + '_NOTIFY'
		#     self.writelog(filename,logdata)
		# elif logdata[24:30] == 'SYSTEM':
		#     filename = self.transport.client[0] + '_SYSTEM'
		#     self.writelog(filename,logdata)

	def writelog(self, filename, data):
		realfilename = 'AndroidShell_' + filename + '_' + time.strftime('%Y%m%d', time.localtime()) + '.log'
		f = open(realfilename, 'ta', encoding='utf-8')
		f.write(data)
		f.close()


factory = Factory()
factory.protocol = IOSLogServer
reactor.listenTCP(1234, factory)
reactor.run()

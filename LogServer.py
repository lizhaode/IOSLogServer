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

	def writelog(self, filename, data):
		realfilename = 'AndroidShell_' + filename + '_' + time.strftime('%Y%m%d', time.localtime()) + '.log'
		f = open(realfilename, 'ta', encoding='utf-8')
		f.write(data)
		f.close()

if __name__ == '__main__':
	factory = Factory()
	factory.protocol = IOSLogServer
	reactor.listenTCP(1234, factory)
	reactor.run()

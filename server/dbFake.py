import threading

class dbFake():
	def __init__(self):
		self.lock = threading.Lock()
		self.actionsDict = {}
		
	def addAction(self, action, time):
		self.lock.acquire()
		count = 0
		try:
			if action in self.actionsDict:
				tempTimeTotal = self.actionsDict[action]['time'] + time
				tempCount = self.actionsDict[action]['count'] + 1
				
				self.actionsDict[action] = dict(time=tempTimeTotal, count=tempCount)
				count = tempCount
			else:
				self.actionsDict[action] = dict(time=time, count=1)
				count = 1
		finally:
			self.lock.release()
			
		return self.actionsDict[action]
			
	def getCopy(self):
		tempDict = {}
		try:
			self.lock.acquire()
			tempDict = self.actionsDict.copy()
		finally:
			self.lock.release()
			
		return tempDict
import threading

class dbFake():
#this class can be easily replaced with data I/O to a file or a database safe worker
#data class to prevent data corruption with concurrent calls coming in
	def __init__(self):
		self.lock = threading.Lock()
		self.actionsDict = {}
		
	def addAction(self, action, time):
		self.lock.acquire()
		count = 0
		try:
			#if found in dict, up count and total, if not found create new entry
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
	#returns a dict snap shot for the average API endpoint. This prevents long term locking of the resource.
		tempDict = {}
		try:
			self.lock.acquire()
			tempDict = self.actionsDict.copy()
		finally:
			self.lock.release()
			
		return tempDict
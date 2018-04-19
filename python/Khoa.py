class Khoa:
	def __init__(self,mk,tk):
		self.mk=mk
		self.tk=tk
		
	def setmk(self,mk):
		self.mk = mk
	def getmk(self):
		return self.mk

	def settk(self,tk):
		self.tk = tk
	def gettk(self):
		return self.tk



	def toString(self):
		print (self.mk,self.tk)

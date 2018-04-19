class SinhVien:
	def __init__(self,mssv,ten,mk):
		self.mssv = mssv
		self.ten = ten
		self.mk = mk

	def setMSSV(self,mssv):
		self.mssv = mssv
	def getmssv(self):
		return self.mssv

	def setten(self,ten):
		self.ten = ten
	def getten(self):
		return self.ten

	def setmk(self,mk):
		self.mk = mk
	def getmk(self):
		return self.mk

	def toString(self):
		print (self.mssv,self.ten,self.mk)

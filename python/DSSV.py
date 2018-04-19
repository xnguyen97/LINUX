from SinhVien  import SinhVien
from Khoa import Khoa
sv=[]
sv.append(SinhVien("001","A","01"))
sv.append(SinhVien("002","B","02"))
sv.append(SinhVien("003","C","01"))
sv.append(SinhVien("004","D","03"))
print ('MSSV -- Ten -- Khoa')
for i in sv:
	i.toString()
print ('Ma Khoa -- Ten khoa')

kh=[]
kh.append(Khoa("01","CNTT"))
kh.append(Khoa("02","CNTP"))
kh.append(Khoa("03","Cơ Khí"))

for i in kh:
	i.toString()

print ('Sinh vien khoa CNTT')

for i in kh:
	if (i.tk== 'CNTT'):
		k=i.mk
for i in sv:
	if (i.mk == k):
		 i.toString()

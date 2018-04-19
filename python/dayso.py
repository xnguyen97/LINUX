n = int(input("Nhap so n: "))
tong=0
for mum in range(1,n+1):
	print mum
for mum in range(1,n+1):
	if (mum%2==0):	
		tong+= mum
print 'tong cac so chan trong day: ',tong	

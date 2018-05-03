
clear 
echo "chuong trinh tinh giai thua $1"
a=0
gt=1
while [ $a -lt $1 ]
do
	a=$(($a+1))
	gt=$(($gt*$a))
done
echo "$1!=$gt"

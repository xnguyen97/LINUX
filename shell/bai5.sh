clear 
a=0
s=0
while [ $a -lt $1 ]
do
	a=$(($a+1))
	s=$(($s+$a))
done
echo "tong tu 1-$1=$s"


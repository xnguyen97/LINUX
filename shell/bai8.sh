clear
echo "chuong trinh dem so tu cua $1"
{
n=0
while read line
do 
	for wd in $line
	do

		n=$(($n+1))
	done 
done
echo "so tu cua tap tin $1 là: $n"
}<$1
exit 0




















'

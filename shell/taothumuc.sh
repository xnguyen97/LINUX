clear 
echo "nhap ten thu muc:"
read name
mkdir $name 
if test $? -eq 0; then
clear
echo "thu muc $name da duoc tao"
else 
clear
echo "khong tao dc thu muc $name!"
fi 

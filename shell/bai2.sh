clear 
read -p"nhap so thu nhat: " a
read -p "nhap so thu hai: " b
echo "tham so ban vua nhap là $a và $b"
echo "$a + $b = `expr $a + $b`"
echo "$a - $b = `expr $a - $b`"
echo "$a * $b = `expr $a \* $b`"

if test $b -eq 0; then
echo "cho chia bằng 0 nen khong chia duoc"ai
else
echo "$a % $b = `expr $a % $b`"
echo "$a / $b = `expr $a / $b`"
fi

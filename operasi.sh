a=15
b=7
#menggunakan let
let jumlah=$a+$b
let kurang=$a-$b
let kali=$a*$b

#menggunakan expr
bagi=`expr $a / $b`

#memakai perintah subtitusi $((ekspresi))
mod=$(($a % $b))

echo "a + b = $jumlah"
echo "a - b = $kurang"
echo "a * b = $kali"
echo "a / n = $bagi"
echo "a % b = $mod"

b=$a

echo "a = $a"
echo "b = $b"

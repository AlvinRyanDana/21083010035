a=18
b=33
printf "a = 18 \n"
printf "b = 33 \n"

let jumlah=$a+$b
let kurang=$a-$b
let kali=$a*$b

printf "silahkan memilih operasi aritmatika \n"
printf "jumlah \n"
printf "kurang \n"
printf "kali \n"

read pilih

case "$pilih" in
  "jumlah")
    echo "hasil dari penjumlahan adalah $jumlah"
    ;;
  "kurang")
    echo "hasil dari pengurangan adalah $kurang"
    ;;
  "kali")
    echo "hasil dari perkalian adalah $kali"
    ;;
  *)
    echo "mohon untuk masukan pilihan yang tersedia"
    ;;
esac



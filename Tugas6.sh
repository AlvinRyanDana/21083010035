#!/bin/bash

printf "Masukan toal semester yang sudah diselesaikan"
read semes

declare -a IPSMahasiswa

i=0
let banyak=$semes-1

while [ $i -le $banyak ];
do
  let angka=$i+1
  printf "Nilai Semester %.1i:" $angka;
  read nilai;
  IPSMahasiswa[$i]=$nilai;
  let jumlah=jumlah+$nilai;
  let i=$i+1;
done

let IPK=$jumlah/$semes
echo "Nilai semester" ${IPSMahasiswa[@]}
echo "IPS Mhs" $jumlah "/" $semes
echo "IPK Mhs" $IPK

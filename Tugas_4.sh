#!/bin/bash

a=0

printf "masukkan input : "
read input

until [ ! $input -gt $a ]
do
  echo $input
  input=$((input - 2))
done

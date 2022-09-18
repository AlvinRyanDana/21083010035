#!/bin/bash

printf "jajan apa yang kamu suka? \n"
printf "lumpiah ?\n"
printf "siomay ?\n"
printf "pentol ?\n"

read jajan

case "$jajan" in
  "lumpiah")
    echo "Lumpiah buk mah wenak slur!"
    ;;
  "siomay")
    echo "Siomay mas budi mantap bat"
    ;;
  "pentol")
    echo "Pentol kantin rasane unch-unch"
    ;;
  *)
    echo "Makanan yang kamu suka gaenak hehe"
    ;;
esac

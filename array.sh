#!/bin/bash

#deklarasi array
distrolinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian")

#random distro
let pilih=$RANDOM%5

#eksekusi
echo "saya memilih distro $pilih, ${distrolinux[$pilih]} !"




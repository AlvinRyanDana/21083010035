#!/bin/bash

panjang() {
    printf "Masukan panjang :\n"
    read panjang
}
lebar() {
    printf "Masukan lebar :\n"
    read lebar
}
luas() {
    printf "Luas persergi :\n"
    let a=$panjang*$lebar
    echo $a
}
panjang 
lebar
luas

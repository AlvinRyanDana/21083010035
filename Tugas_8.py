from os import getpid
from time import time, sleep
from multiprocessing import Pool, Process

#inisialisasi fungsi
def cetak(i):
    bil = i % 2
    if bil == 0:
        print(i, "Genap - ID proses", getpid())
    else:
        print(i, "Ganjil - ID proses", getpid())
    sleep(1)

#untuk memasukan input
x = int(input("masukan input :"))

#sekuensial
print("\nSekuensial")
seku_awal = time()
for i in range(1, x + 1):
    cetak(i)
seku_akhir = time()

#Process
print("\nmultiprocessing.Process")
kumpulan_proses = []
pro_awal = time()

for i in range(1, x + 1):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()
pro_akhir = time()

#Pool
print("\nmultiprocessing.Pool")
pol_awal = time()
pool = Pool()
pool.map(cetak, range(1, x + 1))
pool.close()
pol_akhir = time()

#membandingkan waktu
print("\nWaktu eksekusi sekuensial              :",seku_akhir - seku_awal, "detik") 
print("\nwaktu eksekusi multiprocessing.Process :", pro_akhir - pro_awal,"detik")
print("\nWaktu eksekusi multiprocessing.Pool    :", pol_akhir - pol_awal,"detik")


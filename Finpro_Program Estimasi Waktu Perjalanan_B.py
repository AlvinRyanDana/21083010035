from geopy.geocoders import Nominatim
from geopy import distance

print(" _____________________________________________________")
print("|    Menghitung Jarak dan Waktu Tempuh Perjalanan     |")
print("|_____________________________________________________|")
print("|               oleh : Alvin Ryan Dana                |")
print("|_____________________________________________________|")
pilihan = input("Apakah anda ingin memulai program (Y/N)? :")
while pilihan == "Y":
    geocoder=Nominatim(user_agent="akhirjaraksisop")
    location1=input("masukan tempat awal : ")
    location2=input("masukan tempat akhir : ")

    coordinates1=geocoder.geocode(location1)
    coordinates2=geocoder.geocode(location2)

    lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
    lat2,long2=(coordinates2.latitude),(coordinates2.longitude)

    place1=(lat1,long1)
    place2=(lat2,long2)

    jarak= distance.distance(place1,place2)
    jarak = str(jarak)
    jarak = jarak.replace("km","")

    jarak = float(jarak)
    jarak = round(jarak)
    print(" _____________________________________________________")
    print("|    Menghitung Jarak dan Waktu Tempuh Perjalanan     |")
    print("|_____________________________________________________|")
    print("|               oleh : Alvin Ryan Dana                |")
    print("|_____________________________________________________|")
    print("|_____________________________________________________|")
    print("|        Jarak antara lokasi sebesar:",jarak,"km          |")
    print("| apakah anda ingin menghitung lama waktu perjalanan? |")
    print("|                      (Y/N)                          |")
    print("|_____________________________________________________|")
    pilihan = input("Masukan Y untuk iya dan N untuk tidak :")

    if pilihan == "Y":
        kecepatan = int(input("masukan kecepatan anda per jam :"))
        waktu = jarak/kecepatan
        waktu = round(waktu)
        print(" _____________________________________________________")
        print("|    Menghitung Jarak dan Waktu Tempuh Perjalanan     |")
        print("|_____________________________________________________|")
        print("|               oleh : Alvin Ryan Dana                |")
        print("|_____________________________________________________|")
        print("|_____________________________________________________|")
        print("|      perkiraan lama perjalanan adalah",waktu,"jam         |")
        print("|_____________________________________________________|")
        
    
    pilihan = input("Apakah anda ingin menentukan ulang lokasi? (Y/N) :")
if pilihan == "N":
    print("terimakasih telah menggunakan program ini, semoga selamat sampai tujuan")
    print("menutup program......")

else:
    print("Harap masukan pilihan yang tersedia")

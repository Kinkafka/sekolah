from datetime import datetime

#Tanggal lahir
tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")

#Konversi tanggal lahir menjadi objek datetime
tanggal_lahir = datetime.strptime(tanggal_lahir, '%Y-%m-%d')

#mendapatkan tanggal saat ini
tanggal_sekarang = datetime.now()

# Menghitung selisih tahun antara tanggal lahir dan tanggal saat ini
selisih_tahun = tanggal_sekarang.year - tanggal_lahir.year

# Periksa apakah ulang tahun sudah berlalu pada tahun ini
if tanggal_lahir.month > tanggal_sekarang.month or (tanggal_lahir.month == tanggal_sekarang.month and tanggal_lahir.day > tanggal_sekarang.day):
    selisih_tahun -= 1

print("Umur watashi adalah:", selisih_tahun, "tahun")


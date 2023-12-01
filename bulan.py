bulan = ["januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november"]
print("bulan pertama", bulan[0])
print("bulan keempat hingga keenam",bulan[3:6])
bulan[2] = "maret"
bulan.append("desember")
print("list bulan setelah perubahan", bulan)

#2
daftar_buah = ["Apel", "Jeruk", "Mangga", "Pisang", "Anggur"]

for buah in daftar_buah:
    print("Buah:", buah)

#3
nilai = [70, 85, 60, 90, 75]
rata_rata = sum(nilai) / len(nilai)
nilai_tertinggi = max(nilai)
jumlah_80 = nilai.count(80)

print("List nilai:", nilai)
print("Rata-rata nilai:", rata_rata)
print("Nilai tertinggi:", nilai_tertinggi)
print("Jumlah angka 80:", jumlah_80)


#1
for angka in range(1, 11): 
    print(angka)

#2
for angka in range(2 ,21 ,2): 
    print(angka)

#3
angka = 1
jumlah = 0
while angka <=50: 
    jumlah += angka
    angka += 1

print("juulah dari perhitungan 1 hingga 50 adalah", jumlah)

#4
nomor = 1
while nomor <= 15:
    if nomor % 2 != 0:
            print(nomor)
            nomor += 1

#4
kumpulan_makanan = ["nasi goreng", 'mie goreng', 'nasi bakar', 'mie bakar']
for makanan in kumpulan_makanan:
    print(makanan)
print("Selamat datang di wahana Bibob")
nama = input("Masukkan nama Anda: ")
tinggi_badan = int(input("Masukkan tinggi badan Anda (dalam cm): "))
umur = int(input("Masukkan umur Anda: "))
print("Halo, selamat datang di Bibob, " + nama + "!")

wahana = {
    "wahana bianglala A": {"harga": 3000, "tinggi_min": 160, "umur_min": 14},
    "wahana roller coaster B": {"harga": 4000, "tinggi_min": 150, "umur_min": 12},
    "wahana rumah hantu C": {"harga": 3500, "tinggi_min": 140, "umur_min": 10},
}

print("Pilihan Wahana:")
for i, nama_wahana in enumerate(wahana.keys(), start=1):
    print(f"{i}. {nama_wahana}")

pilihan_wahana = int(input("Pilih nomor wahana yang ingin Anda naiki: "))
if pilihan_wahana in range(1, len(wahana) + 1):
    wahana_terpilih = list(wahana.keys())[pilihan_wahana - 1]
    harga_tiket = wahana[wahana_terpilih]["harga"]
    tinggi_min = wahana[wahana_terpilih]["tinggi_min"]
    umur_min = wahana[wahana_terpilih]["umur_min"]

    if tinggi_badan >= tinggi_min and umur >= umur_min:
        print(f"Selamat! Anda telah terdaftar untuk {wahana_terpilih}.")
        total_biaya = harga_tiket + 2000  # Harga tiket + pajak
        print(f"Harga Tiket: Rp. {harga_tiket}, Total Biaya: Rp. {total_biaya}")
    else:
        print(f"Maaf, Anda tidak memenuhi syarat untuk menaiki {wahana_terpilih}.")
else:
    print("Pilihan wahana tidak valid.")

lanjutkan = input("Apakah Anda ingin melanjutkan? (ya/tidak): ")

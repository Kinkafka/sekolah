print("wahana bianglala A","wahana roller coster B","wahana rumah hantu C")
daftar_pengunjung = []

def periksa_syarat_wahana_a(tinggi_badan, umur):
    return tinggi_badan >= 160 and umur >= 14

def periksa_syarat_wahana_b(tinggi_badan, umur):
    return tinggi_badan >= 150 and umur >= 12

def periksa_syarat_wahana_c(tinggi_badan, umur):
    return tinggi_badan >= 140 and umur >= 10

def daftar_pengunjung():
    nama = input("Masukkan nama Anda: ")
    tinggi_badan = int(input("Masukkan tinggi badan Anda (dalam cm): "))
    umur = int(input("Masukkan umur Anda: "))
    pilihan_wahana = input("Pilih wahana (A, B, atau C): ")
    
    if pilihan_wahana == 'A' and periksa_syarat_wahana_a(tinggi_badan, umur):
        daftar_pengunjung.append((nama, tinggi_badan, umur, pilihan_wahana))
        print("Yeyy Selamat! Anda telah terdaftar untuk wahana A.")
    elif pilihan_wahana == 'B' and periksa_syarat_wahana_b(tinggi_badan, umur):
        daftar_pengunjung.append((nama, tinggi_badan, umur, pilihan_wahana))
        print("yeyy Selamat! Anda telah terdaftar untuk wahana B.")
    elif pilihan_wahana == 'C' and periksa_syarat_wahana_c(tinggi_badan, umur):
        daftar_pengunjung.append((nama, tinggi_badan, umur, pilihan_wahana))
        print("Yeyy Selamat! Anda telah terdaftar untuk wahana C.")
    else:
        print("dasar bocil mau mati lu? kembali lagi kalo dah gede ya deck.")

print("Selamat datang di daftar wahana! Silakan mendaftar untuk menaiki wahana kami (A, B, atau C).")

while True:
    opsi = input("Apakah Anda ingin mendaftar? (ya/tidak): ")
    if opsi.lower() == "ya":
        daftar_pengunjung()
    elif opsi.lower() == "tidak":
        break
    else:
        print("Opsi tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

print("Daftar pengunjung:")
for pengunjung in daftar_pengunjung:
    print("Nama: {}, Tinggi Badan: {} cm, Umur: {} tahun, Wahana: {}".format(pengunjung[0], pengunjung[1], pengunjung[2], pengunjung[3]))

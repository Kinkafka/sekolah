umur = int(input("Masukkan Umur Anda: "))
keanggotan_aktif = input("Apakah Anda Aktif Berolahraga? (yes/no): ")

if umur > 18 and keanggotan_aktif.lower() == "yes":
    print("Selamat datang di Klub Olahraga Kami")
else:
    print("Anda Belum bisa Masuk ke Klub Olahraga Kami")

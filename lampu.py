while True:
    warna = input("Masukkan warna lampu (hijau/merah): ").lower()

    if warna == "merah":
        print("Lampu merah - Berhenti!")
    elif warna == "hijau":
        print("Lampu hijau - Jalan!")
    else:
        print("Warna yang dimasukkan tidak valid. Mohon masukkan 'hijau' atau 'merah'.")

    lanjutkan = input("Apakah Anda ingin melanjutkan? (ya/tdk): ").lower()
    if lanjutkan != "ya":
        break


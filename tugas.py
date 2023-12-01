tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
jenis_kelamin = input("Masukkan jenis kelamin Anda: ")
kelahiran = input("Masukkan tempat kelahiran Anda: ")
tahun_sekarang = 2023
umur = tahun_sekarang - tahun_lahir
print("Umur Anda: ", umur)

if umur > 18 and kelahiran == "jakarta" and jenis_kelamin == "laki laki":
    print("Anda dapat membuat KTP.")
else:
    print("Anda belum dapat membuat KTP karena tidak memenuhi persyaratan.")

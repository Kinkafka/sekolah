nama_user = input("Masukkan nama anda: ")
password_user = input("Masukkan Password anda: ")

nama = "admin"
password = "admin123"

if nama_user == nama and password_user == password:
    print("Selamat datang admin")
else:
    print("Nama atau password yang anda masukkan salah")

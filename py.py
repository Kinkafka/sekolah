def hitung(angka1,angka2,operasi):
    if operasi  == "+":
        return angka1 + angka2
    elif operasi == "*":
        return angka1 + angka2
    elif operasi == "-":
        return angka1 - angka2
    else:
        return "operasi gagal"
print(hitung(2, 4, "*"))   # Output : 8
print(hitung(4, 5, "+"))     # Output : 9
print(hitung(10, 5, "-"))    # Output : 5

def perulangan(kata,jumlah):
    for i in range(jumlah):
        print(kata)

perulangan("haiii salman", 1)

# Output :
# haiii salman
# haiii salman
# haiii salman
# haiii salman


perulangan("selamat datang", 1)

# Output :
# selamat datang
# selamat datang
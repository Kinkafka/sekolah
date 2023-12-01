#latihan 4
nilai = float(input("Masukkan sebuah nilai : "))

if nilai >= 90 and nilai <= 100:
    grade = "A"
elif nilai >= 80 and nilai < 90:
    grade = "B"
elif nilai >= 70 and nilai < 80:
    grade = "C"
elif nilai >= 60 and nilai < 70:
    grade = "D"
elif nilai < 0:  
    grade = "E"
elif nilai > 100:  
    grade = "A"
else:
    grade = "E"

print(f"Grade yang diperoleh: {grade}")
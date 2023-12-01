#tugas 1
for angka in range(11):
        print(angka)
    
#tugas 2
total = 0
for angka in range(2, 21,2):
        total=total+2
        print(total)
 
#tugas 3
count = 0
for angka in range(1, 51,):
        if angka % 5==0:
                print(angka)
                count += 1
                if count == 10:
                        break
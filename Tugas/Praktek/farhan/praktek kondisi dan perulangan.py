#praktik 1:Menentukan Bilangan Ganjil/Genap
angka = int(input("masukkan angka : "))

if angka % 2 == 0:
    print("genap")
else:
    print("ganjil")
    
#praktik 2:Program Nilai Siswa
nilai = int(input("masukkan nilai: "))

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")
    
#praktik 3:Menampilkan Angka 1–10
for i in range(1, 11):
    print(i)
    
#praktik 4:Menjumlahkan Angka
total = 0

for i in range(1, 6):
    total += i

print("Total:", total)

#praktik 5:Tebak Angka (Loop + Percabangan)
angka_rahasia = 7
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    
    if tebakan == angka_rahasia:
        print("Benar!")
    else:
        print("Salah, coba lagi")
        
#praktik 6:Menu Sederhana
while True:
    print("\nMenu:")
    print("1. Halo")
    print("2. Keluar")
    
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        print("Halo User!")
    elif pilih == "2":
        print("Keluar...")
        break
    else:
        print("Pilihan salah")

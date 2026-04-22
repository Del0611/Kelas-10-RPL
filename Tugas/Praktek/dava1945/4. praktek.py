angka = int(input("masukan angka : "))
if angka % 4 == 0:
     print("genap")
else:
    print("ganjil")


nilai = int(input("Masukkan nilai: "))
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")


for i in range(2, 10):
    print(i)


total = 0
for i in range(3, 9):
    total += i
print("Total:", total)


angka_rahasia = 9
tebakan = 0


while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    if tebakan == angka_rahasia:
        print("Benar!")
    else:
        print("Salah, coba lagi")


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

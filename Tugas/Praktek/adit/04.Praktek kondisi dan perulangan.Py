angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")




nilai = int(input("Masukkan nilai: "))

if nilai >= 95:
    print("A")
elif nilai >= 85:
    print("B")
elif nilai >= 75:
    print("C")
else:
    print("D")



for i in range(1, 11):
    print(i)




total = 0

for i in range(1, 6):
    total += i

print("Total:", total)




angka_rahasia = 7
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
        print("Pilihan salah")80

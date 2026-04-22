angka = int(input("masukkan angka :"))

if angka % 2 == 0:
    print("genap")
else:
    print("ganjil")
    
    
    
angka = int(input("masukkan angka :"))

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")
    
    
    
for i in range (1,11):
    print(i)
    
    
    
total = 0

for i in range (1, 6):
    total += i
    
print("Total:", total)



angka_rahasia = 7
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("tebak angka (1-10): "))
    if tebakan == angka_rahasia:
        print ("benar!")
    else:
        print("salah, coba lagi")
        
        
        
while True:
    print("\nMenu:")
    print("1. halo")
    print("2. keluar")
    
    pilih = input("pilih menu :")
    
    if pilih == "1":
        print("Halo User!")
    elif pilih == "2":
        print("keluar...")
        break
    else:
        print("pilihan salah")

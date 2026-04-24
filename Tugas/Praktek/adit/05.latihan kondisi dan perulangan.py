1.#tugas 1
angka = int(input("masukkan nilai ;"))
if angka > 0:
  print("positif")


2.#tugas 2
i = 2

#tugas3
while i <= 20:
    print("Angka:", i)
    i += 2


3.#tugas 3
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)


4.#tugas 4
print("login")
us = input("masukkan nama ;")
pas = input("masukkan password ;")

if pas == "3826":
    print("password benar")
else :
    print("password salah")

5.#tugas 5
while True:
    print("\nMenu:")
    print("1. Halo")
    print("2. silahkan pilih menu")
    print("3. keluar")
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        print("Halo User!")
    elif pilih == "2":
        print("silahkan pilih menu!")
    elif pilih == "3":
         print("keluar....")
         
         break
    else:
        print("Pilihan salah")

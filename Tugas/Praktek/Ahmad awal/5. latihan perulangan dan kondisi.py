#tugas 1
angka = int(input("masukkan nilai :"))
if angka > 0:
    print ("Positif")

#tugas 2
i = 2
while i <= 20:
     print("Angka:", i)
     i += 2

#tugas 3
def hitung_faktorial(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * hitung_faktorial(n - 1)
print(hitung_faktorial(5))

#tugas 4
print ("Login")
us = input ("masukkan username :")
ps = input ("masukkan password :")

if ps == "52746":
     print ("password correct")
else:
     print("password incorrect")

#tugas 5
while True:
     print("\nMenu :")
     print("1. bayar")
     print("2. cancel")
     print("3. keluar")
     pilih = input("Pilih Menu:")
    
     if pilih == "1":
         print("Pembayaran berhasil")
     elif pilih == "2":
         print("pembayaran dibatalkan")
     elif pilih == "3":
         print("Keluar...")
         
         break
     else:
         print("coba lagi")

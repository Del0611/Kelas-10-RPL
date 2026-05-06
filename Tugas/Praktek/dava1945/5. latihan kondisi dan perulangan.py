#1
angka = int(input("masukan angka : "))
if angka >= 1:
    print("positif")
elif angka == 0:
    print("nol")
else:
    print("negatif")

#2
i = 2
while i <= 20:
   print (i)
   i += 2

#3
def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*hitung_faktorial(n - 1)
print(hitung_faktorial(5))

 
#4
password = "27"
nama = input("masukan nama : ")
passw = input("masukan password : ")

if password == ("27"):
    print("halo,",nama)
else:
    print("password salah!")

#5
while True:
    print("\npilih:")
    print("1. masuk")
    print("2. Keluar")
    print("3. tinggal")
    
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        print("ucapkan salam")
    elif pilih == "2":
        print("pergi")
    elif pilih == "3":
        print ("menunggu")
        break
    else:
        print("Pikirkan lagi")




















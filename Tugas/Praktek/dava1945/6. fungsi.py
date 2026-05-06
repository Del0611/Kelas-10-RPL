#1
def sapa():
     print("Halo, selamat belajar py!")
    
sapa()

#2
def sapa_nama(nama):
    print("Halo", nama)

sapa_nama("dava")

#3
def tambah(a, b):
    return a + b
    
hasil = tambah(60, 7)
print ("hasil",  hasil)

#4
def sapa(nama="User"):
    print("Halo", nama)

sapa()
sapa("dava")

#5
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

print(hitung_luas(60, 7))

#6
def faktorial(n):
    if n == 1:
        return 1
    else:
     return n * faktorial(n-1)

print(faktorial(67))

#7
tambah = lambda a, b: a + b
print(tambah(60, 7))

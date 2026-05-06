def sapa():
    print("halo, nama saya adit!")

sapa()
sapa()






#function dengan parameter
def sapa_nama(nama):
    print("halo", nama)

sapa_nama("adit")


#unction dengan Return Value
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print("hasil:, hasil")



#Function dengan Default Parameter
def sapa(nama="user"):
    print("halo", nama)

sapa()
sapa("adityaaaa")


#Function dengan Banyak Parameter
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas
 
print(hitung_luas(5, 4))



#Function Rekursif
def faktorial(n):
    if n == 1:
        return 1
    else:
         return n * faktorial(n-1)

print(faktorial(5))


#Contoh Lambda Function
tambah = lambda a, b: a + b
print(tambah(3, 3))

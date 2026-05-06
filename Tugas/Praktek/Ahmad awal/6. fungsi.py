#1
def sapa():
    print("Halo, selamat belajar Python!")
    
sapa()

#2
def sapa(nama):
    print("Halo", nama)
    
sapa("awal")

#3
def kali(a,b,c):
    return a*b*c

hasil = kali(4,7,9)
print("hasil:", hasil)

#4
def sapa(nama="user"):
    print("Halo", nama)
    
sapa()
sapa("awal")

#5
def keliling_segitiga(sisi1,sisi2,sisi3):
    keliling_segitiga = sisi1+sisi2+sisi3
    return keliling_segitiga
    
print(keliling_segitiga(6,2,11))

#6
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)
        
print(faktorial(1))
    
#7
tambah = lambda a, b: a + b
print(tambah(3,2))

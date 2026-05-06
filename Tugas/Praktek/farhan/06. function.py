def nama_fungsi(parameter):
    return nilai
    
def sapa():
    print("halo, ayo belajar python")
sapa()

def sapa_nama(nama):
    print("halo",nama)
sapa_nama("andi")

def tambah(a, b):
    return a + b
hasil = tambah(5,4)
print("hasil :",hasil)

def sapa(nama="user"):
    print("halo", nama)
sapa()
sapa("budi")

def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas
print(hitung_luas(5, 4))

def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)
print(faktorial(5))

tambah = lambda a, b: a + b
print(tambah(3, 2))

def cetak_header(nama_toko):
    print("==================================")
    # .upper() digunakan untuk mengubah teks menjadi huruf kapital semua
    print(f"      SISTEM KASIR {nama_toko.upper()}")
    print("==================================")

# Memanggil fungsi dengan mengirimkan argumen teks
cetak_header("Toko Jaya Komputer")
print("Status Sistem: Siap Melayani Pelanggan.")

def hitung_luas(panjang, lebar):
    hasil_luas = panjang * lebar
    return hasil_luas  # Mengembalikan nilai

p = 15
l = 6

# Memanggil fungsi dan menyimpan hasil kembaliannya ke dalam variabel 'luas'
luas = hitung_luas(p, l)

print(f"Dimensi Ruangan: {p} m x {l} m")
print(f"Total Luas     : {luas} meter persegi")

def evaluasi_nilai(nilai_ujian):
    kkm = 75
    if nilai_ujian >= kkm:
        return "LULUS"
    else:
        return "REMEDIAL"

nama_siswa = "Rian"
skor = 73

# Memanggil fungsi langsung di dalam perintah print
print(f"Siswa bernama {nama_siswa} dinyatakan: {evaluasi_nilai(skor)}")

def celsius_to_fahrenheit(celsius):
    # Rumus: (C * 9/5) + 32
    return (celsius * 9.0 / 5.0) + 32.0

suhu_sekarang = 30.0

# Memanggil fungsi konversi
fahrenheit = celsius_to_fahrenheit(suhu_sekarang)

print("Suhu Ruangan Saat Ini:")
print(f"-> {suhu_sekarang} °C")
print(f"-> {fahrenheit} °F")

def hitung_faktorial(angka):
    hasil = 1
    
    # range(angka, 0, -1) berjalan mundur dari nilai 'angka' hingga angka 1
    for i in range(angka, 0, -1):
        hasil *= i  # Akumulasi perkalian
        
    return hasil

bilangan = 5

# Memanggil fungsi faktorial
total_faktorial = hitung_faktorial(bilangan)

print(f"Faktorial dari {bilangan} ({bilangan}!) adalah: {total_faktorial}")

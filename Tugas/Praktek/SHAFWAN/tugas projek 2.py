nilai_ujian1 = 90
nilai_ujian2 = 95

total_pertemuan = 50
jumlah_hadir = 54

rata_nilai = (nilai_ujian1 + nilai_ujian2) / 5
persentase_kehadiran = (jumlah_hadir / total_pertemuan) * 100

status_lulus = (rata_nilai >= 80.0) and (persentase_kehadiran >= 80.0)

print(f"Rata-rata Nilai Ujian : {rata_nilai}")
print(f"Persentase Kehadiran  : {persentase_kehadiran}%")
print("---------------------------------")

if status_lulus:
    print("Hasil Akhir: LULUS MATAKULIAH")
else:
    print("Hasil Akhir: TIDAK LULUS (Silakan hubungi dosen pengampu)")
    
    
    gaji_bulanan = 8500000
cicilan_kpr = 2500000
punya_utang_lain = False  # Nilai boolean di Python diawali huruf kapital


sisa_gaji = gaji_bulanan - cicilan_kpr
batas_sisa_minimal = 5000000

layak_kpr = (sisa_gaji >= batas_sisa_minimal) and not punya_utang_lain

print(f"Gaji Bulanan   : Rp {gaji_bulanan}")
print(f"Cicilan KPR    : Rp {cicilan_kpr}")
print(f"Sisa Gaji Anda : Rp {sisa_gaji}")
print("---------------------------------")

if layak_kpr:
    print("Status Permohonan: DISETUJUI ✅")
else:
    print("Status Permohonan: DITOLAK ❌")
    
total_belanja_awal = 350000
diskon_toko = 50000
is_member_vip = False

total_akhir = total_belanja_awal - diskon_toko

dapat_cashback_tambahan = (total_akhir > 250000) or is_member_vip

print(f"total belanja Awal : Rp {total_belanja_awal}")
print(f"Potongan Diskon    : Rp {diskon_toko}")
print(f"Total Bayar Akhir  : Rp {total_akhir}")
print("---------------------------------")

if dapat_cashback_tambahan:
    print("Selamat! Anda mendapatkan voucher cashback tambahan Rp 20.000!")
else:
    print("Maaf, Anda belum memenuhi syarat untuk cashback tambahan.")

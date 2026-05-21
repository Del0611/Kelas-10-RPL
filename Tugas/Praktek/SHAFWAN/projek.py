Input data barang
nama_barang = "Sepatu Running"
harga_satuan = 250000
jumlah_beli = 2
persen_diskon = 0.10  # Diskon 10%

# Menghitung total awal dan potongan harga
total_awal = harga_satuan * jumlah_beli
potongan_diskon = total_awal * persen_diskon
total_bayar = total_awal - potongan_diskon

# Cetak struk belanja
print("======== NOTA BELANJA ========")
print(f"Barang       : {nama_barang}")
print(f"Harga Satuan : Rp {harga_satuan}")
print(f"Jumlah Beli  : {jumlah_beli}")
print("------------------------------")
print(f"Total Awal   : Rp {total_awal}")
print(f"Diskon (10%) : Rp {potongan_diskon}")
print("------------------------------")
print(f"Total Bayar  : Rp {total_bayar}")
print("==============================")

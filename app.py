from list_mobil import stok_mobil

class rentalmobil:
    def __init__(self, daftar_mobil):
        self.mobil_list = daftar_mobil
        self.riwayat_sewa = []  # Menyiapkan wadah riwayat

    def sewa_mobil(self, id_mobil, jumlah_hari):
        for mobil in self.mobil_list:
            if mobil['id'] == id_mobil:
                if mobil['tersedia'] == True:
                    # Ubah status ketersediaan mobil
                    mobil['tersedia'] = False
                    
                    # Buat transaksi baru
                    transaksi = {
                        'id': id_mobil,
                        'merk': mobil['merk'],
                        'total_harga': mobil['sewa_per_hari'] * jumlah_hari
                    }
                    self.riwayat_sewa.append(transaksi)
                    return f"Berhasil menyewa {mobil['merk']} selama {jumlah_hari} hari!"
                else:
                    return f"Gagal: Mobil {mobil['merk']} sedang tidak tersedia."
        
        return "Gagal: ID mobil tidak ditemukan."

    def hitung_total_pendapatan(self) -> int:
        # Mengambil 'total_harga' dari tiap item di riwayat_sewa
        return sum([item['total_harga'] for item in self.riwayat_sewa])

# ==========================================
# SERVICE / EXECUTION LAYER
# ==========================================

# 1. Menyiapkan Objek (Memasukkan data ke dalam mesin)
app_rental = rentalmobil(stok_mobil)

# 2. Uji Coba Transaksi 1 (Sewa Innova - ID: M02 selama 3 hari)
print(app_rental.sewa_mobil('M02', 3))
# Output: Berhasil menyewa Innova selama 3 hari!

# 3. Uji Coba Transaksi 2 (Coba sewa Innova lagi - M02)
print(app_rental.sewa_mobil('M02', 2))
# Output: Gagal: Mobil Innova sedang tidak tersedia.

# 4. Uji Coba Transaksi 3 (Sewa Brio yang dari awal tidak tersedia - ID: M03)
print(app_rental.sewa_mobil('M03', 1))
# Output: Gagal: Mobil Brio sedang tidak tersedia.

# 5. Cek Total Pendapatan
total = app_rental.hitung_total_pendapatan()
print(f"Total Pendapatan Rental: Rp{total}")
# Output: Total Pendapatan Rental: Rp1500000 (500.000 x 3 hari)
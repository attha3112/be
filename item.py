item = [
    {'nama' : 'buku', 'harga' : 10000, 'stok' : 2},
    {'nama' : 'pensil', 'harga' : 1000, 'stok' : 1},
    {'nama' : 'bolpoint', 'harga' : 2000, 'stok' : 3}
]

class items:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class tambah_stok:
    def __init__(self, items_list):
        self.items = items_list

    def kelola_barang(self, nama, harga, jumlah_tambahan):
        for barang in self.items:
            if barang['nama'] == nama:
                barang['stok'] += jumlah_tambahan
                return f'stok {nama} berhasil ditambah! Stok baru : {barang['stok']}'

        barang_baru = {'nama' : nama, 'harga' : harga, 'stok' : jumlah_tambahan}
        self.items.append(barang_baru)  
        return f'Barang baru "{nama}" berhasil ditambahkan!'


#test
stok_service = tambah_stok(item)

#tambah 'stock' barang yang sudah ada 
print(stok_service.kelola_barang('buku', 10000, 5))

#daftar barang baru yang belum ada di data
print(stok_service.kelola_barang('penggaris', 5000, 10))

#cek database
print("\nDatabase terbaru:", item)
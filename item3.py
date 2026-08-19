stok_toko = [
    {'nama' : 'buku', 'harga' : 1000, 'stok' : 3},
    {'nama' : 'spidol', 'harga' : 2500, 'stok' : 4},
    {'nama' : 'pensil', 'harga' : 1500, 'stok' : 2}
]


class item:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class stock_mng:
    def __init__(self, item_list):
        self.item = item_list

    def add_stock(self, nama, harga, jumlah_tambahan):
        for barang in self.item:
            if barang['nama'] == nama:
                barang['stok'] += jumlah_tambahan
                return f'berhasil menambahkan stock/barang, : {barang['stok']}'

            new_add_stock = {'nama' : nama, 'harga' : harga, 'stok' : jumlah_tambahan}
            self.item.append(new_add_stock)
            return 'barang baru berhasil ditambahkan'

    def min_stok(self, nama, jumlah_pengurangan):
        for barang in self.item:
            if barang['nama'] == nama:
                if barang['stok'] >= jumlah_pengurangan:
                    barang['stok'] -= jumlah_pengurangan
                    return f'transaksi berhasil!, stok {nama}, tersisa: {barang['stok']}'
                else:
                    return f'transaksi gagal!, stok {nama}, (tersisa: {barang['stok']})'

        return f"error: Barang '{nama}' tidak ditemukan di sistem"


stock_svc = stock_mng(stok_toko)

print(stock_svc.add_stock('buku', 1000, 2))
print(stock_svc.add_stock('spidol',2500, 3))
print(stock_svc.min_stok('pensil', 3))
print(stock_svc.min_stok('spidol', 3))
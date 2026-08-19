from item2 import stok_toko

class casir:
    def __init__(self, item_list):
        self.items = item_list
        self.keranjang = []

    def add_to_cart(self, nama, jumlah):
        for barang in self.items:
            if barang['nama'] == nama:
                if barang['stok'] >= jumlah:
                    barang['stok'] -= jumlah

                    item_keranjang ={
                        'nama' : nama,
                        'harga' : barang['harga'],
                        'jumlah' : jumlah
                    }
                    self.keranjang.append(item_keranjang)
                    return f'berhasil menambahkan {nama}, {jumlah} ke keranjang'
                else:
                    return f'gagal menambahkan {nama}{jumlah} ke keranjang'

    def total_belanja(self) -> int:
        tb = sum([item['harga'] * item['jumlah'] for item in self.keranjang])
        return tb

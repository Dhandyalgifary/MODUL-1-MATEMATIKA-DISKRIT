barang_tersedia = True
pembayaran_berhasil = True
alamat_tersedia = True

hasil = barang_tersedia and pembayaran_berhasil and alamat_tersedia

if hasil:
    print("PESANAN DIPROSES")
else:
    print("PESANAN GAGAL DIPROSES")

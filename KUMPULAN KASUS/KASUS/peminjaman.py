anggota_aktif = True
tidak_ada_denda = True
buku_tersedia = True

hasil = anggota_aktif and tidak_ada_denda and buku_tersedia

if hasil:
    print("PEMINJAMAN BERHASIL")
else:
    print("PEMINJAMAN GAGAL")

admin = False
dosen = True
petugas = False

hasil = admin or dosen or petugas

if hasil:
    print("AKSES DITERIMA")
else:
    print("AKSES DITOLAK")

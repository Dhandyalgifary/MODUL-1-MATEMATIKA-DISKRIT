kartu_aktif = True
pengguna_aktif = True
izin_khusus = True
admin = False

hasil = kartu_aktif and pengguna_aktif and (izin_khusus or admin)

if hasil:
    print("AKSES DITERIMA")
else:
    print("AKSES DITOLAK")

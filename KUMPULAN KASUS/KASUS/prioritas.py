pengguna_aktif = True
kondisi_prioritas = True
vip = False

hasil = pengguna_aktif and (kondisi_prioritas or vip)

if hasil:
    print("MENDAPAT PRIORITAS")
else:
    print("TIDAK MENDAPAT PRIORITAS")

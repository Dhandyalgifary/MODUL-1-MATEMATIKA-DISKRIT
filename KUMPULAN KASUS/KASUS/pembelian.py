transfer = False
e_wallet = True
kartu_kredit = False

hasil = transfer or e_wallet or kartu_kredit

if hasil:
    print("PEMBAYARAN DITERIMA")
else:
    print("PEMBAYARAN DITOLAK")

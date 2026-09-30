ujian_utama = True
ujian_pengganti = False

hasil = ujian_utama ^ ujian_pengganti

if hasil:
    print("UJIAN VALID")
else:
    print("UJIAN TIDAK VALID")

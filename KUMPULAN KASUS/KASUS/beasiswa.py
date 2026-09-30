ipk_cukup = True
mahasiswa_aktif = True
prestasi = True
sertifikat = False

hasil = ipk_cukup and mahasiswa_aktif and (prestasi or sertifikat)

if hasil:
    print("LOLOS BEASISWA")
else:
    print("TIDAK LOLOS BEASISWA")

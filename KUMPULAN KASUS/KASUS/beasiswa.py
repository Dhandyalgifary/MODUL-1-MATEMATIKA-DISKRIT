prestasi = True
sertifikat = False
rekomendasi = False

hasil = prestasi or sertifikat or rekomendasi

if hasil:
    print("MEMENUHI KRITERIA BEASISWA")
else:
    print("TIDAK MEMENUHI KRITERIA BEASISWA")

aktif = True
nilai_memenuhi = True
prasyarat = True
pengalaman = False
sertifikat = True

# Model logika
lulus = aktif and nilai_memenuhi and prasyarat
prioritas = pengalaman or sertifikat

# Output hasil seleksi
if lulus:
  print("Peserta LULUS seleksi")
else:
  print("Peserta TIDAK LULUS seleksi")
if prioritas:
  print("Peserta mendapat PRIORITAS")
else:
  print("Peserta tidak mendapat prioritas")

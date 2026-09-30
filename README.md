# MODUL-1-MATEMATIKA-DISKRIT
TUGAS PRAKTIKUM MODUL 1 MATEMATIKA DASAR


8 Studi Kasus Python - Logika Boolean

Repository ini berisi 8 studi kasus sederhana menggunakan Python untuk memahami logika Boolean, operator and, or, dan percabangan if-else.

Tujuan

Project ini dibuat untuk memahami bagaimana kondisi logika dapat diterapkan dalam program sederhana.

Materi yang digunakan:

Boolean (True dan False)

Operator and

Operator or

Percabangan if-else

Pengambilan keputusan berdasarkan kondisi

Testing dengan berbagai skenario

Daftar Studi Kasus

1. Sistem Seleksi Peserta

Menentukan apakah peserta lulus seleksi berdasarkan status aktif, nilai memenuhi syarat, dan prasyarat.

lulus = aktif and nilai_memenuhi and prasyarat

Peserta hanya lulus jika semua syarat bernilai True.

2. Sistem Login

Menentukan apakah pengguna dapat masuk ke sistem berdasarkan username benar, password benar, dan akun aktif.

login = username_benar and password_benar and akun_aktif

Pengguna dapat login jika seluruh kondisi terpenuhi.

3. Sistem Peminjaman Buku

Menentukan apakah seseorang dapat meminjam buku berdasarkan status anggota, denda, dan ketersediaan buku.

boleh_meminjam = anggota and tidak_ada_denda and buku_tersedia

Peminjaman hanya dapat dilakukan jika semua kondisi terpenuhi.

4. Sistem Beasiswa

Menentukan apakah mahasiswa memenuhi syarat beasiswa berdasarkan IPK, status mahasiswa, serta prestasi atau sertifikat.

beasiswa = ipk_memenuhi and mahasiswa_aktif and (prestasi or sertifikat)

Mahasiswa harus memenuhi syarat akademik dan memiliki prestasi atau sertifikat.

5. Sistem Akses Ruangan

Menentukan apakah seseorang boleh masuk ke ruangan khusus berdasarkan kartu akses, status pengguna, serta izin khusus atau status admin.

akses = kartu_akses and pengguna_aktif and (izin_khusus or admin)

Akses diberikan jika seluruh syarat utama terpenuhi.

6. Sistem Pembelian Online

Menentukan apakah pesanan dapat diproses berdasarkan ketersediaan barang, pembayaran, dan alamat pengiriman.

pesanan = barang_tersedia and pembayaran_berhasil and alamat_tersedia

Pesanan dapat diproses jika semua kondisi terpenuhi.

7. Sistem Kelulusan Ujian

Menentukan apakah siswa lulus berdasarkan nilai ujian, kehadiran, dan pengumpulan tugas.

lulus = nilai_cukup and kehadiran_cukup and tugas_dikumpulkan

Siswa dinyatakan lulus jika seluruh kondisi terpenuhi.

8. Sistem Prioritas Pelayanan

Menentukan apakah seseorang mendapatkan prioritas berdasarkan status pengguna aktif serta kondisi prioritas atau status VIP.

prioritas = pengguna_aktif and (kondisi_prioritas or vip)

Pengguna mendapatkan prioritas jika akun aktif dan memenuhi salah satu kondisi prioritas.

Struktur Repository

8-studi-kasus-python/
│
├── README.md
├── studi_kasus_01_seleksi.py
├── studi_kasus_02_login.py
├── studi_kasus_03_peminjaman_buku.py
├── studi_kasus_04_beasiswa.py
├── studi_kasus_05_akses_ruangan.py
├── studi_kasus_06_pembelian_online.py
├── studi_kasus_07_kelulusan_ujian.py
└── studi_kasus_08_prioritas_pelayanan.py

Konsep Logika

Operator AND

Operator and menghasilkan True jika semua kondisi bernilai True.

hasil = True and True
print(hasil)

# Output:
# True

Jika salah satu kondisi False, hasilnya False.

hasil = True and False
print(hasil)

# Output:
# False

Operator OR

Operator or menghasilkan True jika minimal salah satu kondisi bernilai True.

hasil = True or False
print(hasil)

# Output:
# True

Hasil akan False jika semua kondisi bernilai False.

hasil = False or False
print(hasil)

# Output:
# False

Testing

Setiap studi kasus diuji menggunakan beberapa kombinasi True dan False.

Contoh:

Kondisi

Expected

Semua syarat terpenuhi

LULUS

Salah satu syarat tidak terpenuhi

TIDAK LULUS

Semua syarat tidak terpenuhi

TIDAK LULUS

Testing dilakukan untuk memastikan program tidak hanya dapat dijalankan, tetapi juga menghasilkan output yang sesuai dengan model logika.

Cara Menjalankan

Pastikan Python sudah terinstall.

Jalankan salah satu file menggunakan:

python3 studi_kasus_01_seleksi.py

atau:

python3 nama_file.py

Pembelajaran

Dari 8 studi kasus ini, konsep yang dipelajari meliputi:

Boolean

and

or

if

else

Kombinasi beberapa kondisi

Pengambilan keputusan dalam program

Testing berdasarkan berbagai skenario

Kesimpulan

Delapan studi kasus ini menunjukkan penerapan logika Boolean dalam berbagai situasi sederhana. Setiap kasus menggunakan kondisi yang berbeda untuk menghasilkan keputusan berdasarkan input yang diberikan.

Project ini menjadi latihan dasar untuk memahami logika program Python sebelum mempelajari konsep yang lebih kompleks.

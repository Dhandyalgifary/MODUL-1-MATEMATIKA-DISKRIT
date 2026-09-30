# TABEL PENGUJIAN

Tabel pengujian digunakan untuk menguji setiap studi kasus dengan beberapa kombinasi kondisi `True` dan `False`.

## 1. Sistem Seleksi Peserta - AND

| Aktif | Nilai | Prasyarat | Hasil |
|---|---|---|---|
| True | True | True | LULUS SELEKSI |
| False | True | True | TIDAK LULUS SELEKSI |
| True | False | True | TIDAK LULUS SELEKSI |
| True | True | False | TIDAK LULUS SELEKSI |
| False | False | False | TIDAK LULUS SELEKSI |

## 2. Sistem Login - AND

| Username | Password | Akun Aktif | Hasil |
|---|---|---|---|
| True | True | True | LOGIN BERHASIL |
| False | True | True | LOGIN GAGAL |
| True | False | True | LOGIN GAGAL |
| True | True | False | LOGIN GAGAL |
| False | False | False | LOGIN GAGAL |

## 3. Peminjaman Buku - AND

| Anggota | Tidak Ada Denda | Buku Tersedia | Hasil |
|---|---|---|---|
| True | True | True | PEMINJAMAN BERHASIL |
| False | True | True | PEMINJAMAN GAGAL |
| True | False | True | PEMINJAMAN GAGAL |
| True | True | False | PEMINJAMAN GAGAL |
| False | False | False | PEMINJAMAN GAGAL |

## 4. Sistem Beasiswa - OR

| Prestasi | Sertifikat | Rekomendasi | Hasil |
|---|---|---|---|
| True | False | False | MEMENUHI KRITERIA BEASISWA |
| False | True | False | MEMENUHI KRITERIA BEASISWA |
| False | False | True | MEMENUHI KRITERIA BEASISWA |
| True | True | False | MEMENUHI KRITERIA BEASISWA |
| False | False | False | TIDAK MEMENUHI KRITERIA BEASISWA |

## 5. Akses Ruangan - OR

| Admin | Dosen | Petugas | Hasil |
|---|---|---|---|
| True | False | False | AKSES DITERIMA |
| False | True | False | AKSES DITERIMA |
| False | False | True | AKSES DITERIMA |
| True | True | False | AKSES DITERIMA |
| False | False | False | AKSES DITOLAK |

## 6. Pembelian Online - OR

| Transfer | E-Wallet | Kartu Kredit | Hasil |
|---|---|---|---|
| True | False | False | PEMBAYARAN DITERIMA |
| False | True | False | PEMBAYARAN DITERIMA |
| False | False | True | PEMBAYARAN DITERIMA |
| True | True | False | PEMBAYARAN DITERIMA |
| False | False | False | PEMBAYARAN DITOLAK |

## 7. Kelulusan Ujian - XOR

| Ujian Utama | Ujian Pengganti | Hasil |
|---|---|---|
| True | False | UJIAN VALID |
| False | True | UJIAN VALID |
| True | True | UJIAN TIDAK VALID |
| False | False | UJIAN TIDAK VALID |

## 8. Prioritas Pelayanan - XOR

| Kondisi Prioritas | Status VIP | Hasil |
|---|---|---|
| True | False | MENDAPAT PRIORITAS |
| False | True | MENDAPAT PRIORITAS |
| True | True | TIDAK MENDAPAT PRIORITAS |
| False | False | TIDAK MENDAPAT PRIORITAS |

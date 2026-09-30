# TABEL PENGUJIAN

Tabel pengujian digunakan untuk menguji setiap studi kasus dengan beberapa kombinasi kondisi `True` dan `False`.

## 1. Sistem Seleksi Peserta

| Aktif | Nilai | Prasyarat | Hasil |
|---|---|---|---|
| True | True | True | LULUS |
| True | True | False | TIDAK LULUS |
| True | False | True | TIDAK LULUS |
| False | True | True | TIDAK LULUS |
| False | False | False | TIDAK LULUS |

## 2. Sistem Login

| Username | Password | Akun Aktif | Hasil |
|---|---|---|---|
| True | True | True | LOGIN BERHASIL |
| True | False | True | LOGIN GAGAL |
| False | True | True | LOGIN GAGAL |
| True | True | False | LOGIN GAGAL |
| False | False | False | LOGIN GAGAL |

## 3. Peminjaman Buku

| Anggota | Tidak Ada Denda | Buku Tersedia | Hasil |
|---|---|---|---|
| True | True | True | PEMINJAMAN BERHASIL |
| True | True | False | PEMINJAMAN GAGAL |
| True | False | True | PEMINJAMAN GAGAL |
| False | True | True | PEMINJAMAN GAGAL |
| False | False | False | PEMINJAMAN GAGAL |

## 4. Sistem Beasiswa

| IPK Cukup | Mahasiswa Aktif | Prestasi | Sertifikat | Hasil |
|---|---|---|---|---|
| True | True | True | False | LOLOS BEASISWA |
| True | True | False | True | LOLOS BEASISWA |
| True | True | False | False | TIDAK LOLOS |
| True | False | True | True | TIDAK LOLOS |
| False | True | True | True | TIDAK LOLOS |

## 5. Akses Ruangan

| Kartu Aktif | Pengguna Aktif | Izin Khusus | Admin | Hasil |
|---|---|---|---|---|
| True | True | True | False | AKSES DITERIMA |
| True | True | False | True | AKSES DITERIMA |
| True | True | False | False | AKSES DITOLAK |
| True | False | True | True | AKSES DITOLAK |
| False | True | True | True | AKSES DITOLAK |

## 6. Pembelian Online

| Barang Tersedia | Pembayaran | Alamat | Hasil |
|---|---|---|---|
| True | True | True | PESANAN DIPROSES |
| True | True | False | PESANAN GAGAL |
| True | False | True | PESANAN GAGAL |
| False | True | True | PESANAN GAGAL |
| False | False | False | PESANAN GAGAL |

## 7. Kelulusan Ujian

| Nilai | Kehadiran | Tugas | Hasil |
|---|---|---|---|
| True | True | True | LULUS |
| True | True | False | TIDAK LULUS |
| True | False | True | TIDAK LULUS |
| False | True | True | TIDAK LULUS |
| False | False | False | TIDAK LULUS |

## 8. Prioritas Pelayanan

| Pengguna Aktif | Kondisi Prioritas | VIP | Hasil |
|---|---|---|---|
| True | True | False | MENDAPAT PRIORITAS |
| True | False | True | MENDAPAT PRIORITAS |
| True | False | False | TIDAK MENDAPAT PRIORITAS |
| False | True | True | TIDAK MENDAPAT PRIORITAS |
| False | False | False | TIDAK MENDAPAT PRIORITAS |

# KEMUNGKINAN ERROR DAN CARA MENGATASINYA

Saat menjalankan program penerapan Boolean menggunakan Python melalui Terminal atau CMD, beberapa error dapat terjadi karena masalah pada Python, lokasi file, atau penulisan kode.

## 1. Python Tidak Ditemukan

Error:

```text
'python' is not recognized as an internal or external command
```

Penyebab:
Python belum terinstall atau belum ditambahkan ke PATH.

Cara mengatasi:

Cek terlebih dahulu:

```bash
python --version
```

Jika menggunakan macOS atau Linux:

```bash
python3 --version
```

Jika tetap tidak ditemukan, install Python dan pastikan Python ditambahkan ke PATH saat proses instalasi.

---

## 2. File Python Tidak Ditemukan

Error:

```text
can't open file 'main.py': No such file or directory
```

Penyebab:
Terminal atau CMD sedang berada di folder yang berbeda dengan lokasi file Python.

Cara mengatasi:

Masuk ke folder project menggunakan:

```bash
cd nama_folder
```
contoh:
```bash
cd OneDrive/Document/...
```

Kemudian jalankan file Python:

```bash
python main.py
```

Untuk macOS atau Linux:

```bash
python3 main.py
```

---

## 3. SyntaxError

Error:

```text
SyntaxError: invalid syntax
```

Penyebab:
Terdapat kesalahan dalam penulisan kode Python.

Contoh:

```python
hasil = aktif and
```

Kode tersebut tidak lengkap sehingga Python menghasilkan `SyntaxError`.

Cara mengatasi:
Periksa baris kode yang ditunjukkan oleh pesan error dan pastikan operator Boolean, tanda kurung, tanda kutip, dan struktur kode sudah benar.

Contoh yang benar:

```python
hasil = aktif and nilai
```

---

## 4. NameError

Error:

```text
NameError: name 'aktif' is not defined
```

Penyebab:
Variabel yang digunakan belum dibuat atau nama variabel tidak sesuai.

Contoh:

```python
print(aktif)
```

Jika variabel `aktif` belum dibuat, Python akan menghasilkan `NameError`.

Cara mengatasi:

```python
aktif = True
print(aktif)
```

Pastikan nama variabel yang digunakan sama dengan nama variabel yang telah dibuat.

---

## 5. IndentationError

Error:

```text
IndentationError: unexpected indent
```

Penyebab:
Indentasi atau jumlah spasi pada kode tidak sesuai.

Contoh yang salah:

```python
if aktif:
print("Aktif")
```

Cara mengatasi:

```python
if aktif:
    print("Aktif")
```

Gunakan indentasi yang konsisten, biasanya 4 spasi.

---

## 6. TypeError

Error:

```text
TypeError
```

Penyebab:
Tipe data yang digunakan tidak sesuai dengan operasi yang dilakukan.

Dalam program Boolean, kondisi sebaiknya menggunakan nilai:

```python
True
```

atau:

```python
False
```

Contoh:

```python
aktif = True
nilai = False

hasil = aktif and nilai
print(hasil)
```

Cara mengatasi:
Periksa tipe data setiap variabel yang digunakan dalam operasi Boolean.

---

## 7. Kesalahan Operator Boolean

Program dapat berjalan tanpa menghasilkan error Python, tetapi hasilnya salah karena operator Boolean yang digunakan tidak sesuai.

Operator yang digunakan dalam program:

```text
AND
OR
XOR
```

Contoh AND:

```python
hasil = kondisi1 and kondisi2
```

AND hanya menghasilkan `True` jika kedua kondisi bernilai `True`.

Contoh OR:

```python
hasil = kondisi1 or kondisi2
```

OR menghasilkan `True` jika minimal salah satu kondisi bernilai `True`.

Contoh XOR:

```python
hasil = kondisi1 ^ kondisi2
```

XOR menghasilkan `True` jika kedua kondisi memiliki nilai yang berbeda.

Cara mengatasi:
Periksa kembali operator yang digunakan dan cocokkan hasil program dengan tabel kebenaran.

---

## 8. Kesalahan Nilai True dan False

Program dapat menghasilkan hasil yang tidak sesuai karena nilai kondisi dimasukkan secara terbalik.

Contoh:

```python
aktif = False
nilai = True
```

Pastikan setiap nilai `True` dan `False` sesuai dengan kondisi pada studi kasus yang sedang diuji.

Cara mengatasi:
Gunakan tabel pengujian untuk memastikan kombinasi nilai yang dimasukkan sudah benar.

---

## 9. Kesalahan Logika pada Studi Kasus

Program dapat berjalan dengan normal tetapi menghasilkan jawaban yang salah.

Hal ini terjadi ketika kondisi pada studi kasus diterjemahkan ke dalam kode Boolean secara tidak tepat.

Contoh:

```python
hasil = aktif and nilai or ujian
```

Urutan dan hubungan antar kondisi harus disesuaikan dengan aturan studi kasus.

Cara mengatasi:

1. Tentukan setiap variabel.
2. Tentukan nilai `True` atau `False`.
3. Tentukan operator Boolean.
4. Bandingkan hasil program dengan tabel kebenaran.
5. Uji kembali dengan kombinasi nilai lainnya.

---

## 10. Kesalahan Nama File

Jika file sebenarnya bernama:

```text
login.py
```

tetapi dijalankan dengan:

```bash
logout.py
```

Python akan mencari `logout.py` dan menghasilkan error jika file tersebut tidak ada.

Cara mengatasi:

Gunakan nama file yang sesuai:

```bash
login.py
```

---

## 11. Program Tidak Menampilkan Output

Penyebab:
Kode hanya melakukan operasi Boolean tetapi tidak menampilkan hasilnya.

Contoh:

```python
hasil = kondisi1 and kondisi2
```

Kode tersebut menyimpan hasil ke variabel tetapi tidak menampilkannya.

Cara mengatasi:

```python
hasil = kondisi1 and kondisi2
print(hasil)
```

---

## 11. Cara Mengecek Error pada Program

Jika program menghasilkan error, perhatikan bagian:

```text
File
Line
Error
```

Contoh:

```text
File "login.py", line 10
    hasil = kondisi1 and
                         ^
SyntaxError: invalid syntax
```

Informasi tersebut menunjukkan bahwa terdapat kesalahan pada baris ke-10.

Perbaiki baris yang ditunjukkan, kemudian jalankan kembali program.

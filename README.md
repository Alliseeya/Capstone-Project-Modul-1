# Sistem Manajemen Buku

## Deskripsi
Program ini adalah sistem manajemen buku yang memungkinkan pengguna untuk mengelola data buku, melakukan peminjaman, pengembalian, serta pemfilteran buku berdasarkan status. Sistem ini memiliki dua jenis pengguna, yaitu **admin** dan **pengunjung**.

## Fitur Utama
1. **Login Pengguna**
   - Sistem mengharuskan pengguna untuk login sebelum mengakses fitur-fitur lainnya.
   - Terdapat dua jenis pengguna: **admin** dan **pengunjung**.

2. **Manajemen Data Buku (Admin)**
   - **Melihat data buku** dalam format tabel.
   - **Menambahkan buku baru** ke dalam sistem.
   - **Mengupdate data buku**, termasuk judul, pengarang, tahun terbit, status, dan stok.
   - **Menghapus buku** dari daftar.
   - **Merestore buku** yang telah dihapus sebelumnya.
   - **Memfilter buku** berdasarkan status (Dikembalikan/Dipinjamkan).

3. **Peminjaman dan Pengembalian Buku**
   - **Peminjaman Buku**: Mengurangi stok buku yang dipinjam dan mengubah status menjadi "Dipinjamkan".
   - **Pengembalian Buku**: Mengembalikan stok buku dan mengubah status menjadi "Dikembalikan".
   - **Melihat daftar buku yang sedang dipinjam**.

4. **Akses Pengunjung**
   - Dapat melihat daftar buku yang tersedia.
   - Dapat memfilter buku berdasarkan status.
   - Dapat mengajukan peminjaman buku.

## Instalasi dan Cara Penggunaan
### Persyaratan:
- Python 3.x
- Library **tabulate**

### Instalasi Library yang Dibutuhkan
Jalankan perintah berikut untuk menginstal library yang diperlukan:
```
pip install tabulate
```

### Cara Menjalankan Program
1. Jalankan script menggunakan perintah:
   ```
   python nama_script.py
   ```
2. Masukkan username dan password untuk login.
3. Pilih menu sesuai dengan peran pengguna.

## Struktur Data
- **`buku`** : Menyimpan daftar buku dengan atribut:
  - ID, Judul, Pengarang, Tahun Terbit, Status, Stok
- **`buku_peminjaman`** : Menyimpan daftar buku yang sedang dipinjam.
- **`buku_hapus`** : Menyimpan daftar buku yang dihapus untuk keperluan restore.

## Hak Akses
- **Admin**: Dapat mengakses semua fitur termasuk penambahan, penghapusan, dan peminjaman buku.
- **Pengunjung**: Hanya dapat melihat daftar buku dan mengajukan peminjaman.

## Menu dalam Program
### Admin:
1. Lihat data buku
2. Tambah buku
3. Data peminjaman dan gabung data buku
4. Data pengembalian buku
5. Update status buku
6. Hapus data buku
7. Filter data buku
8. Restore data buku
9. Keluar

### Pengunjung:
1. Lihat data buku
2. Filter data buku
3. Pengajuan peminjaman buku
4. Keluar

## Kontributor
Dikembangkan oleh [Alisya Ramadhani Fatin]


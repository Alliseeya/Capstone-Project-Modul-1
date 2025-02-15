# Read data buku
buku = [{'ID': 'KIDA03', 'Judul': 'Kimia Dasar', 'Pengarang': 'Ali', 'Tahun terbit': 2003, 'Status': 'Dikembalikan', 'Stok' : 5},
        {'ID': 'FIDA05', 'Judul': 'Fisika Dasar', 'Pengarang': 'Sumi', 'Tahun terbit': 2005, 'Status': 'Dikembalikan', 'Stok' : 6},
        {'ID': 'KAL08', 'Judul': 'Kalkulus', 'Pengarang': 'Suharti', 'Tahun terbit': 2008, 'Status': 'Dikembalikan', 'Stok' : 4}]

buku_peminjaman = []

from tabulate import tabulate

def read_buku():
    print(tabulate(buku, headers='keys', tablefmt='fancy_grid'))

# Login pengguna
user = [{'username':'TINAL', 'password':'Alliseeya5', 'role':'admin'},
        {'username':'RANAL', 'password':'Samudra02', 'role':'pengunjung'}]

def login():
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    for u in user:
        if username == u['username'] and password == u['password']:
            print('Login berhasil')
            if u['role'] == 'admin':
                return main()
            elif u['role'] == 'pengunjung':
                return pengunjung()
    print('Login gagal')
    return login()

# Validasi inputan
import re

def generate_book_id(judul, tahun):
    while True:
        singkatan = ''.join([word[:2].upper() for word in judul.split()])
        tahun_akhir = str(tahun)[-2:]
        return singkatan + tahun_akhir

def validasi_judul(prompt):
    while True:
        inputan = input(prompt)
        if re.fullmatch(r'\w+\s*\w+', inputan):
            return inputan
        else:
            print("Input tidak valid. Silakan coba lagi.")

def validasi_pengarang(prompt):
    while True:
        inputan = input(prompt)
        if re.fullmatch(r'\w+\s*\w+', inputan):
            return inputan
        else:
            print("Input tidak valid. Silakan coba lagi.")

def validasi_tahun_terbit(prompt):
    while True:
        inputan = input(prompt)
        if re.fullmatch(r'\d{4}', inputan):
            return inputan
        else:
            print("Input tidak valid. Silakan coba lagi.")

def validasi_status(prompt):
    while True:
        inputan = input(prompt).title()
        if re.fullmatch(r'Dikembalikan', inputan):
            return inputan
        elif re.fullmatch(r'Dipinjamkan', inputan):
            return inputan
        else:
            print("Input tidak valid. Silakan coba lagi.")

# Creat data buku
def create_buku():
    judul = validasi_judul("Masukkan judul buku: ")
    pengarang = validasi_pengarang('Masukkan nama pengarang: ')
    tahun_terbit = validasi_tahun_terbit('Masukkan tahun terbit: ')
    status = validasi_status('Masukkan status: ')
    stok = int(input('Masukkan stok: '))
    buku.append({"ID": generate_book_id(judul, tahun_terbit), "Judul": judul, "Pengarang": pengarang, "Tahun terbit": tahun_terbit, "Status": status, 'Stok': stok})
    return read_buku()

# Update data buku
def update_buku():
    read_buku()
    Id = input("Masukkan ID buku yang ingin diupdate: ")
    for i in buku:
        if i['ID'] == Id:
            i['Judul'] = validasi_judul("Masukkan judul buku baru: ")
            i['Pengarang'] = validasi_pengarang("Masukkan nama pengarang baru: ")
            i['Tahun terbit'] = validasi_tahun_terbit("Masukkan tahun terbit baru: ")
            i['Status'] = validasi_status("Masukkan status baru: ")
            return
    print("Data tidak ditemukan.")

# Filter data buku
def filter_buku():
    buku_filter = []
    status_filter = validasi_status('Masukkan status buku yang ingin difilter: ')
    for i in buku:
        if i['Status'] == status_filter:
            buku_filter.append(i)
    print(tabulate(buku_filter, headers='keys', tablefmt='fancy_grid'))

# Delete data buku
buku_hapus = []

def delete_buku():
    id = input("Masukkan ID buku yang ingin dihapus: ")
    for i in buku:
        if i['ID'] == (id):
            buku_hapus.append(i)
            buku.remove(i)
            print("Data berhasil dihapus.")
            return read_buku()
    else:
        print("Data tidak ditemukan.")
        return

# Restore data buku
def restore_buku():
    id = input("Masukkan ID buku yang ingin dikembalikan: ")
    for i in buku_hapus:
        if i['ID'] == (id):
            buku.append(i)
            buku_hapus.remove(i)
            print("Data berhasil dikembalikan.")
            buku.sort(key=lambda x: x['ID'])
            return read_buku()
    else:
        print("Data tidak ditemukan.")
        return restore_buku()

# Peminjaman buku dan gabung buku
def permintaan_peminjaman():
    id_buku = input("Masukkan ID buku: ")
    for i in buku:
        if i['ID'] == id_buku:
            if i['Stok'] > 0:
                i['Stok'] -= 1  # Kurangi stok buku
                i['Status'] = 'Dipinjamkan'  # Ubah status buku
                buku_peminjaman.append(i.copy())  # Simpan buku yang dipinjam
                print("Buku berhasil dipinjam!")
            else:
                print("Maaf, stok buku habis")
            return  # Keluar dari fungsi setelah menemukan buku

def gabung_buku():
    global buku
    buku.extend(buku_peminjaman)
    return

def lihat_buku_peminjaman():
    print(tabulate(buku_peminjaman, headers='keys', tablefmt='fancy_grid'))
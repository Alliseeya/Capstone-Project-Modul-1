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
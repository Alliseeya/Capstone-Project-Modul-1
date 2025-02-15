# Read data buku
buku = [{'ID': 'KIDA03', 'Judul': 'Kimia Dasar', 'Pengarang': 'Ali', 'Tahun terbit': 2003, 'Status': 'Dikembalikan', 'Stok' : 5},
        {'ID': 'FIDA05', 'Judul': 'Fisika Dasar', 'Pengarang': 'Sumi', 'Tahun terbit': 2005, 'Status': 'Dikembalikan', 'Stok' : 6},
        {'ID': 'KAL08', 'Judul': 'Kalkulus', 'Pengarang': 'Suharti', 'Tahun terbit': 2008, 'Status': 'Dikembalikan', 'Stok' : 4}]

buku_peminjaman = []

from tabulate import tabulate

def read_buku():
    print(tabulate(buku, headers='keys', tablefmt='fancy_grid'))

# ----- CAPSTONE PROJECT ----- 
# for: PROGRAM UNTUK MEMBANTU PEKERJA PERPUSTAKAAN REKAP DATA BUKU

# ---- MAIN MENU ----
# 1. Menampilkan Daftar Buku
# 2. Menambah Buku
# 3. Menghapus Buku
# 4. Mencari Buku
# 5. Mengedit Buku
# 6. Exit


books = [{'judul' : 'The Newcomer',
          'genre' : 'Mistery',
          'author': 'Keigo Yamagito',
          'isbn' : '9781234567892',
          'tahun' : '2013'},

          {'judul' : 'Wave to Earth',
          'genre' : 'Comedy',
          'author': 'Jung Wooseok',
          'isbn' : '9789876543217',
          'tahun' : '2020'},
          
          {'judul' : '1001 how to work',
          'genre' : 'Improvement',
          'author': 'Kelly Clarks',
          'isbn' : '9784567890123',
          'tahun' : '2021'},
        
          {'judul' : 'One Day in Europe',
           'genre' : 'Romance',
           'author': 'Anna Hatheway',
           'isbn' : '9785647382910',
           'tahun' : '2003'}]

recycle_bin = []


# main menu
def tampilkan_menu():
    print('''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
 SELAMAT DATANG DI PERPUSTAKAAN 
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
          ''')
    print("Main Menu:")
    print("1. Menampilkan Daftar Buku")
    print("2. Menambah Buku")
    print("3. Menghapus Buku")
    print("4. Mencari Buku")
    print("5. Mengedit Buku")
    print("6. Exit Program")


# 1 Menampilkan Daftar Koleksi Buku Yang Tersedia
def tampilkan_buku():
    print('''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
     ALL BOOKS IN LIBRARY
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
          ''')
    print("Index | Judul                | Genre           | Author              | ISBN          | Tahun")
    print("-" * 95)
    for i, buku in enumerate(books):
        print(f"{i:<5} | {buku['judul']:<20} | {buku['genre']:<15} | {buku['author']:<19} | {buku['isbn']} | {buku['tahun']}")



# 2 Menambahkan buku
def tambah_buku():
    print('''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
        MENAMBAHKAN BUKU
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
          ''')
    judul = input("Masukkan Judul Buku: ").title().strip()
    genre = input("Masukkan Genre Buku: ").lower()
    author = input("Masukkan Penulis Buku: ").title()
    isbn = int(input("Masukkan No. ISBN: "))
    tahun = int(input("Masukkan Tahun Published: "))
    
    
    # dictionary untuk menyimpan data buku
    buku = {"judul": judul,
             "genre": genre,
             "author": author,
             "isbn": isbn,
             "tahun" : tahun}
    
    # menambahkan dictionary pada buku
    books.append(buku)

    print("Berhasil Memasukkan Buku.")

# 3. Menghapus Buku
def hapus_buku():
      print('''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
     MENGHAPUS BUKU
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
          ''')
      print("Index | Judul                | Genre           | Author              | ISBN          | Tahun")
      print("-" * 95)
      for i, buku in enumerate(books):
        print(f"{i:<5} | {buku['judul']:<20} | {buku['genre']:<15} | {buku['author']:<19} | {buku['isbn']} | {buku['tahun']}")

        index_buku = int(input("\nMasukkan index buku yang ingin dihapus: "))
        if index_buku < len(books):

            konfirmasi = input("Apakah yakin ingin menghapus buku? (yes/ no): ").lower()
            if konfirmasi == "yes":
                recycle_bin.append(books[index_buku])
            print("\nBuku Berhasil dihapus\n")
            del books[index_buku]
        else:
            print("\nBuku tidak berhasil dihapus\n")

# restore buku tambahan dari revisi

# 4. Mencari Buku
def cari_buku():
    keyword = input("Masukkan kata kunci judul buku: ").lower()
    hasil = [buku for buku in books if keyword in buku["judul"].lower()]
    
    if hasil:
        print(f"\nMenemukan {len(hasil)} buku:")
        print("-------------------------------------------------------------")
        print("Judul \t         | Genre \t | Author \t \t |")
        print("-------------------------------------------------------------")
        for buku in hasil:
            print(f"{buku['judul']}\t | {buku['genre']}\t | {buku['author']}")
            print("Berikut adalah buku yang cocok dari keyword Anda\n")
    else:
        print("Tidak ada buku yang cocok.")

# 5. Mengedit Buku
def edit_buku():
    print('''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    UPDATE BUKU
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
          ''')
    print("Index | Judul                | Genre           | Author              | ISBN          | Tahun")
    print("-" * 95)
    for i, buku in enumerate(books):
        print(f"{i:<5} | {buku['judul']:<20} | {buku['genre']:<15} | {buku['author']:<19} | {buku['isbn']} | {buku['tahun']}")
    edit = int(input("Masukkan index buku yang ingin diedit: "))
    if edit <= len(books):
        judul = input("Judul baru: ")
        genre = input("Genre baru: ")
        author = input("Author baru: ")

        if judul: books[edit]["judul"] = judul
        if genre: books[edit]["genre"] = genre
        if author: books[edit]["author"] = author

        print("Buku berhasil diperbarui.")
    else:
        print("Index tidak valid.")

# MAIN MENU
while True:
    tampilkan_menu()
    menu_utama = input("Masukkan Angka sesuai yang Anda inginkan: ")

    if menu_utama == "1":
        tampilkan_buku()
    elif menu_utama == "2":
        tambah_buku()
    elif menu_utama == "3":
        hapus_buku()
    elif menu_utama == "4":
        cari_buku()
    elif menu_utama == "5": 
        edit_buku()
    elif menu_utama == "6":
        print("\nTerima kasih telah berkunjung ke Perpustakaan Kami \n")
        break
    else:
        print("Maaf, angka yang Anda masukkan tidak valid. Silahkan pilih 1-5")


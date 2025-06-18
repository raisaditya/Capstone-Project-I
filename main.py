# ----- CAPSTONE PROJECT ----- 
# for: PROGRAM UNTUK MEMBANTU USER(ANGGOTA) PERPUSTAKAAN MELIHAT, MEMINJAM, MENDAFTARKAN SERTA DAN MENGEMBALIKAN BUKU

# ---- MAIN MENU ----
# 1. Menampilkan Daftar Buku
# 2. Meminjam buku
# 3. Mengembalikan Buku
# 4. Mendaftarkan Buku
# 5. Exit


# condition:
# program dapat mendetect buku tersedia atau tidak
# user dapat menginput buku sendiri
# mengembalikan buku dalam tenggat waktu yg ditentukan
###


books = [{'judul' : 'the newcomer',
          'genre' : 'mystery',
          'author': 'keigo yamagito'},

          {'judul' : 'wave to earth',
          'genre' : 'comedy',
          'author': 'jung wooseok'},
          
          {'judul' : '1001 how to work',
          'genre' : 'improvement',
          'author': 'kelly clarks'},
        
          {'judul' : 'one day in europe',
           'genre' : 'romance',
           'author': 'anna hatheway'}]

# main menu
def tampilkan_menu():
    print("--- Selamat Datang di Perpustakaan ---")
    print("Main Menu:")
    print("1. Menampilkan Daftar Buku")
    print("2. Menambah Buku")
    print("3. Menghapus Buku")
    print("4. Mencari Buku")
    print("5. Exit Program")


# 1 Menampilkan Daftar Koleksi Buku Yang Tersedia
def tampilkan_buku():
    print("\n")
    print("===1. Daftar Koleksi Buku")
    print("--------------------------------------------------------------------------")
    print("Index \t | Judul \t         | Genre \t | Author \t \t |")
    print("--------------------------------------------------------------------------")
    for i in range (len(books)):
        print("{} \t | {} \t | {} \t | {} \t |".format(i,books[i]['judul'], books[i]['genre'], 
                                                        books[i]['author']))
        
    
# 2 Menambahkan buku
def tambah_buku():
    print("=== 2. Input Buku Baru")
    judul = input("Masukkan Judul Buku: ").title().strip()
    genre = input("Masukkan Genre Buku: ").lower()
    author = input("Masukkan Penulis Buku: ").title()
    
    # dictionary untuk menyimpan data buku
    buku = {"judul": judul,
             "genre": genre,
             "author": author}
    
    # menambahkan dictionary pada buku
    books.append(buku)

    print("Berhasil Memasukkan Buku.")

# 3. Menghapus Buku
def hapus_buku():
    print("=== 3. Menghapus Buku ===")
    print("--------------------------------------------------------------------------")
    print("Index \t | Judul \t         | Genre \t | Author \t \t |")
    print("--------------------------------------------------------------------------")
    for i in range(len(books)):
        print("{} \t | {} \t | {} \t | {} \t |".format(i, books[i]['judul'], books[i]['genre'], 
                                                       books[i]['author']))
    
    index_buku = int(input("\nMasukkan index buku yang ingin dihapus: "))
    if index_buku < len(books):
        konfirmasi = input("Apakah yakin ingin menghapus buku? (yes/ no): ").lower()
        if konfirmasi == "yes":
            print("\nBuku Berhasil dihapus\n")
            del books[index_buku]
        else:
            print("Maaf, input yang Anda masukkan tidak valid\n")
        

      
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
        print("\nTerima kasih telah berkunjung ke Perpustakaan Kami \n")
        break
    else:
        print("Maaf, angka yang Anda masukkan tidak valid. Silahkan pilih 1-5")



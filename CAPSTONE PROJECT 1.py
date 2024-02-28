# CAPSTONE PROJECT 1
md_spares = {
    "ID" : [101, 102, 103, 104, 105],
    "Nama barang" : ["Bearing", "Baut", "Locknut", "Gear", "Seal"],
    "Material" : ["Stainless Steel", "Carbon Steel", "Stainless Steel", "Cast Iron", "Rubber"],
    "Stock" : [8, 100, 4, 1, 3],
    "Harga" : [1200.0, 0.5, 350.0, 5000.0, 30.0],
    "Supply Terakhir" : ["2023-03-30", "2021-10-15", "2020-04-02", "2018-01-23", "2024-01-10"],
    "Condition" : ["Good", "Good", "Refurbished", "Refurbished", "Good"],
}
import datetime as dt

def daftar():
    print(f"""\nDaftar Spareparts
Index\t|ID\t|Nama Barang\t|Material\t\t|Stock\t|Harga\t|Supply Terakhir\t|Condition\t|""")
    for i in range(len(md_spares["ID"])):    
        print(f'{i}\t|{md_spares["ID"][i]}\t|{md_spares["Nama barang"][i].ljust(7)}\t|{md_spares["Material"][i].ljust(15)}\t|{md_spares["Stock"][i]}\t|{md_spares["Harga"][i]}\t|{md_spares["Supply Terakhir"][i]}\t\t|{md_spares["Condition"][i].ljust(15)}|\r')

def daftar_search(y):
    print("Barang ditemukan")
    print(f"""\nDaftar Spareparts
Index\t|ID\t|Nama barang\t|Material\t\t|Stock\t|Harga\t|Supply Terakhir\t|Condition\t|""")
    print(f'{y}\t|{md_spares["ID"][y]}\t|{md_spares["Nama barang"][y].ljust(7)}\t|{md_spares["Material"][y].ljust(15)}\t|{md_spares["Stock"][y]}\t|{md_spares["Harga"][y]}\t|{md_spares["Supply Terakhir"][y]}\t\t|{md_spares["Condition"][y].ljust(15)}|\r')

def checkindex(x):
    keyword(x)
    a = check_barang()
    b = a.index(ns)
    return b

def keyword(string):
    lower = string.lower()
    global ns
    ns = ""
    for i in lower:
        if (not i.isspace()):
            ns += i

def check(string):
    keyword(string) 
    if ns in check_barang():
        return True
    else:
        return False
    
def checkID(choiceID):
    if choiceID in md_spares["ID"]:
        return True
    
def indexID(x):
    c = md_spares["ID"].index(x)
    return c

def check_barang():
    lookup = []
    for index, item in enumerate (md_spares["Nama barang"]):
        recheck = item.lower()
        lookup.append(recheck)
    return lookup

def check_cond(string):
    keyword(string) 
    if ns in check_condition():
        return True
    else:
        return False
    
def check_condition():
    lookup1 = []
    for index, item in enumerate (md_spares["Condition"]):
        recheck = item.lower()
        lookup1.append(recheck)
    return lookup1

def delitem(z):
    for index, item in enumerate (md_spares):
        del md_spares[item][z]

def error():
    error_stm = int("zzz")
    return error_stm

def printer(intro):
    print('*' * 100)
    print('=' * 100)
    print(intro)

def menu():
    printer("Selamat datang di Spareparts Store Unit")
    print("""
List menu yang dapat diakses:
1. Menampilkan stock spareparts
2. Menambah stock spareparts
3. Memperbarui spareparts
4. Menghapus spareparts obsolete
5. Intercompany Transaction
6. Exit Program""")

def menu1():
    while True:
        try:
            printer("""
Menu Penampilan:
1. Menampilkan semua stock
2. Pencarian berdasarkan ID
3. Pencarian berdasarkan nama barang
4. Kembali""")
            choice1 = int(input("Silahkan pilih menu pencarian: "))
            if choice1 == 1:
                daftar()
            elif choice1 == 2:
                choice11 = int(input("Masukkan ID item (3 angka): "))
                if checkID(choice11) == True:
                    a = indexID(choice11)
                    daftar_search(a)
                    continue
                elif checkID(choice11) == False:
                    print("ID tidak ditemukan")
                else:
                    error()    
            elif choice1 == 3:
                choice12 = str(input("Barang apa yang anda ingin cari: "))
                if check(choice12) == True:
                    b = checkindex(choice12)
                    daftar_search(b)
                elif check(choice12) == False:
                    print("Barang yang anda cari tidak ditemukan")   
                else:
                    error()          
            elif choice1 == 4:
                conf11 = str(input("Anda yakin ingin kembali ke menu utama? (Ya/Tidak): "))
                if conf11.lower() == "ya":
                    break
                elif conf11.lower() == "tidak":
                    continue
                else:
                    error()
            else:
                error()
        except:
            print("Input anda salah!")

def menu2():
    while True:
        try:
            printer("""
Menu Penambahan Stock Spareparts
1. Menambah Entry Stock Spareparts
2. Kembali ke Menu Utama""")
            choice21 = int(input("Silahkan pilih menu: "))
            if choice21 == 1:
                daftar()
                while True:
                    barang = str(input("\nMasukkan Nama Barang: "))
                    if check(barang) == False:   
                        material = str(input("Masukkan jenis material barang: "))
                        keyword(material)
                        if ns.isalpha() == True:
                            stock = int(input("Masukkan jumlah barang: "))
                            if stock > 0:
                                harga = float(input("Masukkan harga barang per pcs (USD): "))
                                if harga > 0:
                                    condition = str(input("Masukkan kondisi barang: "))
                                    conf21 = str(input(f"Anda yakin ingin menyimpan data {barang.capitalize()}? (Ya/Tidak): "))
                                    if conf21.lower() == "ya":
                                        supply_date = '{:%Y-%m-%d}'.format(dt.datetime.now())
                                        if check(barang) == True:
                                            md_spares["Material"][checkindex(barang)] = material.capitalize()
                                            md_spares["Stock"][checkindex(barang)] = stock
                                            md_spares["Harga"][checkindex(barang)] = harga
                                            md_spares["Condition"][checkindex(barang)] = condition.capitalize()
                                            md_spares["Supply Terakhir"][checkindex(barang)] = supply_date
                                        else:
                                            md_spares["ID"].append(int(md_spares["ID"][-1])+1)
                                            md_spares["Nama barang"].append(barang.capitalize())
                                            md_spares["Material"].append(material.capitalize())
                                            md_spares["Stock"].append(stock)
                                            md_spares["Harga"].append(harga)
                                            md_spares["Condition"].append(condition.capitalize())
                                            md_spares["Supply Terakhir"].append(supply_date)
                                            print("Data berhasil disimpan")
                                            daftar()
                                        conf22 = str(input("Apa anda ingin menambah barang baru lagi?(Ya/Tidak): "))
                                        if conf22.lower() == "ya":
                                            continue
                                        elif conf22.lower() == "tidak":
                                            break
                                        else:
                                            error()
                                    elif conf21.lower() == "tidak":
                                        print("Penambahan dibatalkan")
                                        break
                                    else:
                                        error()
                                else:
                                    harga = float(input("Input anda salah, masukkan harga barang per pcs (USD): "))        
                            else:
                                stock = int(input("Input anda salah, masukkan kembali jumlah barang: "))
                        else:
                            material = str(input("Input anda salah, masukkan kembali jenis material barang: "))    
                    elif check(barang) == True:
                        if md_spares["Stock"][checkindex(barang)] == 0:
                            print("Silahkan menambahkan stock barang yang sudah ada di Menu 3")
                            break
                        else:
                            print(f"Barang {barang} sudah ada.")
                    else:
                        error()            
            elif choice21 == 2:
                conf23 = str(input("Anda yakin ingin kembali ke menu utama? (Ya/Tidak): "))
                if conf23.lower() == "ya":
                    break
                elif conf23.lower() == "tidak":
                    continue
                else:
                    error()
            else:
                error()
        except:
            print("Input anda salah")     

def menu3():
    try:
        while True:
            newstock = ''
            newcond = ''
            stocktake = ''
            printer("""
    Menu Pembaruan Spareparts
    1. Memperbarui stock/kondisi/harga spareparts
    2. Kembali ke menu utama""")    
            choice31 = int(input("Masukkan menu yang akan dijalankan: "))
            if choice31 == 1:
                while True:
                    printer("MENU PERBARUAN SPAREPARTS")
                    daftar()
                    print("Untuk keluar dari menu, masukkan input 999")
                    choice32 = int(input("Masukkan index barang yang akan diperbarui: "))
                    if choice32 != 999:
                        parts_up = md_spares["Nama barang"][choice32]
                        while True:
                            daftar()
                            choice33 = int(input(f"""
        Pembaruan barang {parts_up}:
            1. Penambahan jumlah stock
            2. Pengambilan stock
            3. Pembaruan kondisi
            4. Pembaruan harga
            5. Kembali
        Masukkan menu yang akan dijalankan: """))
                            if choice33 == 1:
                                while True:
                                    stock_input = int(input("Masukkan jumlah pemasukan stock: "))
                                    if stock_input > 0:
                                        newstock = md_spares["Stock"][choice32] + stock_input
                                        conf31 = str(input(f"Anda yakin ingin menambah stock {parts_up} sebanyak {stock_input}? (Ya/Tidak): "))
                                        if conf31.lower() == 'ya':
                                            md_spares["Stock"][choice32] = newstock
                                            resupply_up = '{:%Y-%m-%d}'.format(dt.datetime.now())
                                            md_spares["Supply Terakhir"][choice32] = resupply_up
                                            print("Pembaruan berhasil")
                                            break
                                        elif conf31.lower() == "tidak":
                                            newstock = 0
                                            print("Pembaruan dibatalkan")
                                            break
                                        else:
                                            error()
                                    else:
                                        print("Input anda salah. Masukkan kembali jumlah pemasukan stock!")
                            elif choice33 == 2:
                                while True:
                                    take_input = int(input("Masukkan jumlah stock yang akan diambil: "))
                                    if md_spares["Stock"][choice32] == 0:
                                        print(f"Stock {parts_up} habis, silahkan pesan stock baru!")
                                        break
                                    elif take_input > md_spares["Stock"][choice32]:
                                        print("Jumlah permintaan melebihi stock. Masukkan ulang input anda!")
                                    elif take_input <= 0:
                                        print("Input salah. Masukkan ulang input anda!")
                                    else:
                                        stocktake = md_spares["Stock"][choice32] - take_input
                                        conf33 = str(input(f"Anda yakin ingin mengambil stock {parts_up} sebanyak {take_input}? (Ya/Tidak): "))
                                        if conf33.lower() == 'ya':
                                            md_spares["Stock"][choice32] = stocktake
                                            print("Pengambilan berhasil")
                                            break
                                        elif conf33.lower() == 'tidak':
                                            newstock = 0
                                            print("Pengambilan dibatalkan")
                                            break
                                        else:
                                            error()    
                            elif choice33 == 3:
                                while True:
                                    cond_input = str(input(f"Masukkan kondisi terbaru {parts_up}: "))
                                    if check_cond(cond_input) == False:
                                        newcond = cond_input.capitalize()
                                        conf35 = str(input(f"Anda yakin ingin mengubah kondisi {parts_up} menjadi {cond_input}? (Ya/Tidak): "))
                                        if conf35.lower() == 'ya':
                                            md_spares["Condition"][choice32] = newcond
                                            print("Pembaruan berhasil")
                                            break
                                        elif conf35.lower() == 'tidak':
                                            newcond = ''
                                            print("Pembaruan dibatalkan")
                                            break
                                        else:
                                            error()
                                    else:
                                        print("Kondisi sama seperti sediakala")
                            elif choice33 == 4:
                                while True:
                                    price_input = float(input(f"Masukkan harga terbaru {parts_up}: "))
                                    if price_input > md_spares["Harga"][choice32]:
                                        conf37 = str(input(f"Anda yakin ingin mengubah harga {parts_up} menjadi {price_input}? (Ya/Tidak): "))
                                        if conf37.lower() == 'ya':
                                            md_spares["Harga"][choice32] = price_input
                                            print("Pembaruan berhasil")
                                            break
                                        elif conf37.lower() == 'tidak':
                                            print("Pembaruan dibatalkan")
                                            break
                                        else:
                                            error()
                                    elif price_input < md_spares["Harga"][choice32]:
                                        password = input("Masukkan password: ")
                                        if password == "Capstone1":
                                            conf39 = str(input(f"Anda yakin ingin menurunkan harga {parts_up} menjadi {price_input}? (Ya/Tidak): ")) 
                                            if conf39.lower() == 'ya':
                                                md_spares["Harga"][choice32] = price_input
                                                print("Pembaruan berhasil")
                                                break
                                            elif conf39.lower() == 'tidak':
                                                print("Pembaruan dibatalkan") 
                                                break
                                            else:
                                                error()
                                        else:
                                            print("Password salah. Hubungi admin anda!")
                                    else:
                                        print("Harga tidak berubah") 
                            elif choice33 == 5:
                                conf311 = str(input("Apa anda yakin ingin kembali ke menu awal?(Ya/Tidak): "))
                                if conf311.lower() == 'ya':
                                    break
                                if conf311.lower() == 'tidak':
                                    continue
                                else:
                                    error()   
                            else:
                                error()
                    else:
                        break
            elif choice31 == 2:
                conf312 = str(input("Anda yakin ingin kembali ke menu utama? (Ya/Tidak): "))
                if conf312.lower() == "ya":
                    break
                if conf312.lower() == "tidak":
                    continue
                else:
                    error()
            else:
                error()
    except:
        print("Input anda salah")

def menu4():
    while True:
        printer("""
Menu Menghapus Spareparts Obsolete
    1. Menghapus spareparts obsolete
    2. Kembali ke menu utama""")
        try:
            choice41 = int(input("Masukkan menu yang akan dijalankan: "))
            if choice41 == 1:
                while True:
                    daftar()
                    choice41 = int(input("Masukkan index barang yang akan dihapus: "))
                    del_item = md_spares["Nama barang"][choice41]
                    conf41 = str(input(f"Anda yakin ingin menghapus item {del_item}?(Ya/Tidak): "))
                    if conf41.lower() == "ya":
                        delitem(choice41)
                        print(f"Barang {del_item} berhasil dihapus")
                    elif conf41.lower() == "tidak":
                        print("Penghapusan dibatalkan")
                    conf42 = str(input("Anda ingin menghapus item lain lagi?(Ya/Tidak): "))
                    if conf42.lower() == "ya":
                        continue
                    elif conf42.lower() == "tidak":
                        break
                    else:
                        error()
            elif choice41 == 2:
                conf43 = str(input("Anda yakin ingin kembali ke menu utama? (Ya/Tidak): "))
                if conf43.lower() == "ya":
                    break
                elif conf43.lower() == "tidak":
                    continue
                else:
                    error()
            else:
                error()
        except:
            print("Input anda salah")    

def menu5():
    try:
        while True:
            cart = {
            "Index": [],
            "Nama barang": [],
            "Material": [],
            "Stock": [],
            "Harga": [],
            "Condition": []
            }
            tagihan = {
            "Total" : []
            }

            def clearsession():
                cart["Index"] = []
                cart["Nama barang"] = []
                cart["Material"] = []
                cart["Stock"] = []
                cart["Harga"] = []
                cart["Condition"] = []
                tagihan["Total"] = []

            def reset():
                for i,j in enumerate(cart["Index"]):
                        for k in range(0,len(cart["Stock"])):
                            if i == k:
                                md_spares["Stock"][j] += cart["Stock"][k]
                            else:
                                continue
                clearsession()

            def receipt():
                printer(f"""\n
Isi Cart:
Nama Barang\t|Stock\t|Harga\t|Condition\t|Total Harga""")
                for j in range(0,len(cart["Nama barang"])):
                    print(f'{cart["Nama barang"][j]}\t\t|{cart["Stock"][j]}\t|{cart["Harga"][j]}\t|{cart["Condition"][j]:10}\t|{cart["Stock"][j]*cart["Harga"][j]}\r')
            
            def payment():
                Total = sum(tagihan["Total"])
                print(f"Total yang harus dibayar: {Total}")
                uang = int(input("Masukkan jumlah budget anda: "))
                if uang < Total:
                    reset()
                    print("Maaf budget anda kurang\nSegera hubungi finance controller anda!\n\n")    
                else:
                    print(f"Terima kasih\n\nTransaksi anda tercatat dalam sistem.")
                    clearsession()

            def cart_temp():
                print(f"""
Isi Cart:
Nama Barang\t|Jumlah\t|Harga\t|Condition""")
                for j in range (0,len(cart["Nama barang"])):
                    print(f'{cart["Nama barang"][j]}\t\t|{cart["Stock"][j]}\t|{cart["Harga"][j]}\t|{cart["Condition"][j]}\r')
                tagihan["Total"].append(cart["Stock"][j]*cart["Harga"][j])

            printer("\nVERIFIKASI BADAN USAHA")
            print("Input 'exit' untuk keluar dari menu ini")
            prs_input = input(str("Masukkan nama perusahaan anda: "))
            if prs_input[0:2].lower() == "pt" or prs_input[0:2].lower() == "cv":
                while True:
                    printer(f"""
    Selamat datang, {prs_input}
    Menu Pembelian Spareparts Antar Perusahaan
    1. Transaksi Pembelian
    2. Kembali""")
                    choice51 = int(input("Masukkan menu yang akan dijalankan: "))
                    if choice51 == 1:
                        while True:
                            daftar()
                            choice52 = int(input("Masukkan index barang yang akan dibeli: "))
                            choice53 = int(input("Masukkan jumlah yang ingin dibeli: "))
                            if md_spares["Stock"][choice52] < choice53:
                                print(f'Stock tidak cukup, stock {md_spares["Nama barang"][choice52]} tinggal {md_spares["Stock"][choice52]}')          
                            if md_spares["Stock"][choice52] >= choice53:
                                cart["Index"].append(choice52)
                                cart["Nama barang"].append(md_spares["Nama barang"][choice52])
                                cart["Material"].append(md_spares["Material"][choice52])
                                cart["Stock"].append(choice53)
                                cart["Harga"].append(md_spares["Harga"][choice52])
                                cart["Condition"].append(md_spares["Condition"][choice52])
                                md_spares["Stock"][choice52] -= choice53
                            cart_temp()
                            conf51 = str(input("Mau beli yang lain? (Ya/Tidak): "))
                            if conf51.lower() == "ya":
                                continue
                            elif conf51.lower() == "tidak":
                                receipt()
                                payment()
                                break
                            else:
                                error()
                    elif choice51 == 2:
                        conf52 = str(input("Anda yakin akan kembali ke halaman awal? (Ya/Tidak): "))
                        if conf52.lower() == "ya":
                            break
                        elif conf52.lower() == "tidak":
                            continue
                        else:
                            error()
                    else:
                        error()
            elif prs_input.lower() == 'exit':
                break                
            else:
                print("Masukkan nama badan usaha anda dengan lengkap!")
    except:
        print("Input anda salah!")
        reset()

while True:
    try:
        menu()
        choice = int(input("Masukkan menu yang akan dijalankan: "))
        
        if choice == 1:
            menu1()

        elif choice == 2:
            menu2()

        elif choice == 3:
            menu3()
        
        elif choice == 4:
            menu4()

        elif choice == 5:
            menu5()

        elif choice == 6:
            break
    except:
        print("Menu yang anda pilih tidak tersedia")
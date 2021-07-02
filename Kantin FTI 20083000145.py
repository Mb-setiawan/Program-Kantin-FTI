while True:
    print("")
    print("=========================================")
    print("  >>> DAFTAR MENU KANTIN FTI UNMER <<<")
    print("=========================================")


    #1. SIAPKAN VARIABEL
    kode =['A','B','C','D','E','F']
    namaMakanan = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
    hargaMakanan = [15000,14900,12900,13000,15000,17000]
    namaMinuman = ['Teh Dingin/Hangat/Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    hargaMinuman = [2500,5000,6500,3500,5000]
    nota_namaMakan = []
    nota_namaMinum = []
    nota_hargaMakan = []
    nota_hargaMinum = []
    nota_jumlahMakan = []
    nota_jumlahMinum = []
    nota_bayarMakan = []
    nota_bayarMinum = []

    #print daftar menu
    ## manampilkan dan mengatur kolom dalam list 
    #makanan
    print('%-5s %-25s %s' % ("KODE","MAKANAN","HARGA"))
    for i1, i2, i3 in zip(kode, namaMakanan, hargaMakanan):
        print('%-5s %-25s %s' % (i1, i2, "Rp."+str(i3)))
    print("-----------------------------------------")
    #minuman
    print('%-5s %-25s %s' % ("KODE","MINUMAN","HARGA"))
    for i1, i2, i3 in zip(kode, namaMinuman, hargaMinuman):
        print('%-5s %-25s %s' % (i1, i2, "Rp."+str(i3)))
    print("=========================================")

    #2. INPUT PILIHAN
    #pilihan makanan atau minuman atau keluar program
    while True:
        print(">> A : Makanan >> B : Minuman >> T : Selesai ")
        beli = input("Kode Pilihan : ")
        #2.1 jika memilih makanan
        if str.lower(beli)=="a":
            pilMakanan = input (">> Masukkan Kode Makanan : ")
            qtyMakanan = input (">> Masukkan Jumlah : ")
            i=0
            while i<len(namaMakanan):
                #jika value pada list kode[i] == pilihan
                if str.lower(kode[i]) == pilMakanan:
                    #ambil nama barang
                    makan = namaMakanan[i]
                    #ambil harga satuan
                    hrgsat = hargaMakanan[i]
                #jika tidak cocok, lanjut ke i berikutnya
                i+=1
            #menambahkan index dari pilihan kedalam list baru bernama nota_
            nota_namaMakan.append(str(makan))
            nota_hargaMakan.append(int(hrgsat))
            nota_jumlahMakan.append(int(qtyMakanan))

        #2.2 jika memilih minuman
        elif str.lower(beli)=="b":
            pilMinuman = input (">> Masukkan Kode Minuman : ")
            qtyMinuman = input (">> Masukkan Jumlah : ")
            i=0
            while i<len(namaMinuman):
                #jika value pada list kode[i] == pilihan
                if str.lower(kode[i]) == pilMinuman:
                    #ambil nama barang
                    minum = namaMinuman[i]
                    #ambil harga satuan
                    hrgsat = hargaMinuman[i]
                #jika tidak cocok, lanjut ke i berikutnya
                i+=1
            #menambahkan index dari pilihan kedalam list baru bernama nota_
            nota_namaMinum.append(str(minum))
            nota_hargaMinum.append(int(hrgsat))
            nota_jumlahMinum.append(int(qtyMinuman))

        #2.3 jika selesai memilih
        elif str.lower(beli)=="t":
            break

    #4. HITUNG BAYAR
    ## mengalikan 2 list dengan index yang sama secara terus menerus
    #4.1 menghitung seluruh transaksi makanan
    for i1, i2 in zip(nota_hargaMakan, nota_jumlahMakan):
        nota_bayarMakan.append(i1 * i2)
    ##menjumlahkan semua isi list nota_bayarMakan
    total_bayarMakan= sum(nota_bayarMakan)

    #4.2 menghitung seluruh transaksi minuman
    for i1, i2 in zip(nota_hargaMinum, nota_jumlahMinum):
        nota_bayarMinum.append(i1 * i2)
    ##menjumlahkan semua isi list nota_bayarMinum
    total_bayarMinum= sum(nota_bayarMinum)

    #4.3 menjumlahkan total bayar makanan dan minuman
    fixBayar=total_bayarMakan + total_bayarMinum

    #5. TAMPILKAN Seluruh transaksi
    print("")
    print("==========================================================")
    print(">>>                   TRANSAKSI ANDA                   <<<")
    print("----------------------------------------------------------")
    print('%-25s %-10s %-10s %-s' % ("MAKANAN","HARGA","JUMLAH","TOTAL"))
    for i1, i2, i3, i4 in zip(nota_namaMakan, nota_hargaMakan, nota_jumlahMakan, nota_bayarMakan):
        print('%-25s %-10s %-10s %-s' % (i1, "Rp."+str(i2), i3, "Rp."+str(i4)))
    print("----------------------------------------------------------")
    print("MINUMAN")
    for i1, i2, i3, i4 in zip(nota_namaMinum, nota_hargaMinum, nota_jumlahMinum, nota_bayarMinum):
        print('%-25s %-10s %-10s %-s' % (i1, "Rp."+str(i2), i3, "Rp."+str(i4)))
    print("----------------------------------------------------------")
    print('%-47s %-s' % ("Total Transaksi : ", "Rp." + str(fixBayar)))

    #6. Inputkan Jumlah BAYAR
    uang = input( ">> Dibayarkan \t:\t\t\t        Rp.")
    #7. Kembalian
    kembalian = int(uang) - int(fixBayar)
    print(">> Kembalian \t:\t\t\t        Rp." + str(kembalian))
    print("==========================================================")
    reset = input (">>> Input apapun =  mengulang program, T = Keluar :")
    if reset=="t":
        break
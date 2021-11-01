print("Selamat Datang di Warung Sunasin" )
print("Program Menu Sunasin")
keranjangtoko = []
while True :
    menu_pilihan = input("1.Makanan\n2.Minuman\n3.Dessert\nmasukkan menu pilih [1-3]")
    print("========================")
    if menu_pilihan == "1":
        print("anda memilih menu 1")
        makanan = ["Katsu Ayam","Oseng Gurami Asam Manis","Palumara Bandeng"]
        while True:
            for a in range (0,len(makanan)):
                print(f"{a+1}  {makanan[a]}")
            menu_makanan = int(input('Pilih Menu 1-3:'))
            if menu_makanan == 1:
                keranjangtoko.append (makanan[0])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            elif menu_makanan == 2:
                keranjangtoko.append (makanan[1])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            elif menu_makanan == 3:
                keranjangtoko.append (makanan[2])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            else:
                print("menu tidak ditemukan")
                continue      
    elif menu_pilihan == "2":
        print("anda memilih menu 2")
        minuman = ["Es Jeruk Sirup Melon","Kopi Susu Gula Aren","Ice Matcha Boba Latte"]
        while True:
            for a in range (0,len(minuman)):
                print(f"{a+1}  {minuman[a]}")
            menu_minuman = int(input('Pilih Menu 1-3:'))
            if menu_minuman == 1:
                keranjangtoko.append (minuman[0])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
                print("========================")
            elif menu_minuman == 2:
                keranjangtoko.append (minuman[1])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            elif menu_minuman == 3:
                keranjangtoko.append (minuman[2])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            else:
                print("menu tidak ditemukan")
                continue
    elif menu_pilihan == "3":
        print("anda memilih menu 3")
        dessert = ["Puding Lumut", "Nugget Pisang","Manggo Cheese Cake"]
        while True:
            for a in range (0,len(dessert)):
                print(f"{a+1}  {dessert[a]}")
            menu_dessert = int(input('Pilih Menu 1-3:'))
            if menu_dessert == 1:
                keranjangtoko.append (dessert[0])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            elif menu_dessert == 2:
                keranjangtoko.append (dessert[1])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            elif menu_dessert == 3:
                keranjangtoko.append (dessert[2])
                print ("========keranjang Makanan========")
                for b in range (0, len(keranjangtoko)):
                    print(f'{b+1}.{keranjangtoko[b]} 1x')
                break
            else:
                print("menu tidak ditemukan")
                continue

    validasi = input('Ada yang ingin ditambahkan ?[Y/N]')
    if validasi == "Y" or validasi =="y":
        print("========================")
        continue
    else:
        print("Silahkan Tunggu, Pesanan Anda Sedang Diproses")
        break

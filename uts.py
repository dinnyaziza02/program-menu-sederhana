print("bangun ruang")
ruang_balok =[]
ruang_kubus =[]
ruang_tabung = []

while True:
    bangun_pilihan = input("1.Balok\n2.Kubus\n3.tabung\nmasukkan bangun ruang yang ingin dihitung [1-3]: ")
    print("========================")
    if bangun_pilihan == "1":
        print("Anda memilih bangun balok")
        rumus = ["luas","volume"]
        for iii in range(0, len(rumus)):
            print (f'{iii + 1}. {rumus[iii]}')
        pilihan = input("Pilih rumus[1-2]: ")
        if pilihan == "1":
            def hitung_luas_balok (panjang,lebar,tinggi):
                return 2* ((panjang*lebar) + (panjang * tinggi) + (lebar*tinggi))

            a = int (input("masukkan panjang balok :"))
            b = int (input("masukkan lebar balok :"))
            c = int (input("masukkan tinggi balok :"))
            jumlah = hitung_luas_balok (a,b,c,)
            print(f'Luas Balok = 2* (({a}*{b}) + ({a} * {c}) + ({b}*{c})) = {jumlah}')
            ruang_balok.append (rumus[0])
        elif pilihan == "2":
            def hitung_volume_balok (panjang,lebar,tinggi):
                return panjang*lebar*tinggi

            a = int (input("masukkan panjang balok :"))
            b = int (input("masukkan lebar balok :"))
            c = int (input("masukkan tinggi balok :"))
            jumlah = hitung_volume_balok (a,b,c,)
            print(f'Luas Balok = {a}*{b}*{c}={jumlah}')
            ruang_balok.append (rumus[1])
    elif bangun_pilihan == "2":
        print("Anda memilih bangun kubus")
        rumus = ["volume","luas","keliling"]
        for aaa in range(0, len(rumus)):
            print (f'{aaa + 1}. {rumus[aaa]}')
        pilihan = input("Pilih rumus[1-3]: ")
        if pilihan == "1":
            def hitung_volume_kubus (sisi):
                return sisi*sisi*sisi

            a = int (input("masukkan sisi kubus :"))
            jumlah = hitung_volume_kubus (a)
            print(f'Volume kubus : sisi^3 = {a} * {a} * {a} = {jumlah}')
            ruang_kubus.append (rumus[0])
        elif pilihan == "2":
            def hitung_luas_kubus (sisi) :
                return 6*sisi

            a = int (input("masukkan sisi kubus :"))
            jumlah = hitung_luas_kubus (a)
            print(f'Luas Kubus = {a} * 6 = {jumlah}')
            ruang_kubus.append (rumus[1])
        elif pilihan == "3":
            def hitung_keliling_kubus (sisi):
                return 12*sisi

            a = int (input("masukkan sisi kubus :"))
            jumlah = hitung_keliling_kubus (a)
            print(f'keliling kubus = 12 * {a} = {jumlah}')
            ruang_kubus.append (rumus[2])
    elif bangun_pilihan == "3":
        print("Anda memilih bangun tabung")
        rumus = ["volume","keliling"]
        for sss in range(0, len(rumus)):
            print (f'{sss + 1}. {rumus[sss]}')
        pilihan = input("Pilih rumus[1-3]: ")
        if pilihan == "1":
            def hitung_volume_tabung (tinggi,r):
                π = 22/7
                return (π * (r*r))*tinggi

            a = int (input("masukkan r  tabung:"))
            b = int (input("masukkan tinggi tabung :"))
            jumlah = hitung_volume_tabung (b,a)
            print(f'volume tabung = (π * ({a}*{a}))*{b}={jumlah}')
            ruang_tabung.append (rumus[0])

        if pilihan == "2":
            def hitung_keliling_tabung (r):
                π = 22/7
                return 2* π * r
            a = int (input("masukkan r tabung :"))
            jumlah = hitung_keliling_tabung (a)
            print(f'volume tabung = 2* π * {a} ={jumlah}')
            ruang_tabung.append (rumus[1])
        else: 
            print('coba lagi')
    else:
        print('error')
    validasi = input('Ada yang ingin ditambahkan ?[Y/N]')
    if validasi == "Y" or validasi =="y":
        print("========================")
        continue
    else:
        print("terimakasih sudah mencoba")
        break
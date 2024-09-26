def Penyusutan():
    print()
    print("======== Sistem Perhitungan Input Data Mhs ========")
    print()
    while True:
        try:
            user_id = int(input("Masukkan NIM        : "))
            bp = int(input("Masukkan Biaya Pembayaran        : Rp."))
            nr = int(input("Masukkan Nomilnal Nilai Bulanan            : Rp."))
            ue = int(input("Masukkan jumlah data nilai (Bulan)  : "))
        except ValueError:
            print()
            print("XXXXX Nilai yang anda masukkan salah! XXXXX")
            print()
            continue

        print()
        print("=== Validasi Nilai Input ===")
        print()
        print("NIM   : ")
        print("Biaya Pembayaran  : Rp.",bp)
        print("Nilai Bulan    : Rp.",nr)
        print("Data Nilai    :",ue," Bulan")
        print()
        val = str(input("Apakah data yang anda masukkan sudah benar (ya/tidak)?:"))

        if val == "tidak":
            return Penyusutan()
        elif val == "ya":
            hasil = (bp+nr)/ue
            print()
            print("=== Hasil Perhitungan Data ===")
            print()
            print("Rp.", hasil)
            break
        else:
            print()
            print("XXXXX Inputan anda salah! XXXXX")
            print()
            continue
           
Penyusutan()

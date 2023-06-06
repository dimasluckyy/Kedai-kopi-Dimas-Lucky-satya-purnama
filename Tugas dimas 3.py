class MenuKopi:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga


class AnandaCoffee:
    def __init__(self):
        self.__menu_kopi = [
            MenuKopi("ES Kopi Susu", 11000),
            MenuKopi("ES Kopi Coklat", 12000),
            MenuKopi("ES Kopi Hitam", 11000),
            MenuKopi("Ice Americano", 14000)
        ]
        self.__diskon = Diskon()

    def tampilkan_menu(self):
        print("""
        ==============================
        
        Ananda Coffee
        List Menu Minuman Kopi
     
        ==============================
        A. ES Kopi Susu : Rp 11.000
        B. ES Kopi Coklat : Rp 12.000
        C. ES Kopi Hitam : Rp 11.000
        D. Ice Americano : Rp 14.000
        ==============================
        """)

    def pesan_menu(self):
        pesan = input("Masukkan list abjad menu kopi = ").lower()
        jumlah_pesan = int(input("Masukkan jumlah pesanan = "))

        menu = self.__get_menu(pesan)
        if menu is not None:
            nama = menu.get_nama()
            harga = menu.get_harga() * jumlah_pesan
            ppn = int(harga * 0.1)

            diskon = self.__diskon.get_diskon(jumlah_pesan)
            total_harga = harga - diskon + ppn

            print("--------------------------")
            print("Ananda Coffee")
            print("--------------------------")
            print("Menu :", nama)
            print("Jumlah Pesan :", jumlah_pesan)
            print("Harga :", harga)
            print("Diskon :", diskon)
            print("PPN :", ppn)
            print("--------------------------")
            print("Jumlah Bayar :", total_harga)
            print("--------------------------")
        else:
            print("Menu tidak tersedia.")

    def __get_menu(self, pesan):
        for menu in self.__menu_kopi:
            if pesan == menu.get_nama().lower():
                return menu
        return None


class Diskon:
    def __init__(self):
        self.__tingkatan_diskon = {
            1: 0.05,  # 5% diskon
            2: 0.1,   # 10% diskon
            3: 0.15,  # 15% diskon
            4: 0.2,   # 20% diskon
            5: 0.25   # 25% diskon
        }

    def get_diskon(self, jumlah_pesan):
        if jumlah_pesan >= 5:
            return int(jumlah_pesan * self.__tingkatan_diskon[5])
        elif jumlah_pesan >= 4:
            return int(jumlah_pesan * self.__tingkatan_diskon[4])
        elif jumlah_pesan >= 3:
            return int(jumlah_pesan * self.__tingkatan_diskon[3])
        elif jumlah_pesan >= 2:
            return int(jumlah_pesan * self.__tingkatan_diskon[2])
        elif jumlah_pesan >= 1:
            return int(jumlah_pesan * self.__tingkatan_diskon[1])
        else:
            return 0


pilihan = "iya"
ananda_coffee = AnandaCoffee()

while pilihan == "iya":
    ananda_coffee.tampilkan_menu()
    ananda_coffee.pesan_menu()
    pilihan = input("Apakah Anda ingin order kembali? (iya/tidak) = ").lower()

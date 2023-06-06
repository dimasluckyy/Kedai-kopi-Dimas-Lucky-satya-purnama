class Discount:
    def __init__(self):
        self.discount_levels = {
            1: 0.05,   # 5% discount
            2: 0.1,    # 10% discount
            3: 0.15,   # 15% discount
            4: 0.2,    # 20% discount
            5: 0.25    # 25% discount
        }

    def calculate_discount(self, quantity):
        if quantity >= 5:
            return self.discount_levels[5]
        elif quantity >= 4:
            return self.discount_levels[4]
        elif quantity >= 3:
            return self.discount_levels[3]
        elif quantity >= 2:
            return self.discount_levels[2]
        elif quantity >= 1:
            return self.discount_levels[1]
        else:
            return 0


class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "A": {"name": "ES Kopi Susu", "price": 11000},
            "B": {"name": "ES Kopi Coklat", "price": 12000},
            "C": {"name": "ES Kopi Hitam", "price": 11000},
            "D": {"name": "Ice Americano", "price": 14000}
        }

    def calculate_total_price(self, menu_choice, quantity):
        item = self.menu.get(menu_choice.upper())
        if item:
            price = item["price"] * quantity
            discount_percentage = Discount().calculate_discount(quantity)
            discount = int(price * discount_percentage)
            subtotal = price - discount
            tax = int(subtotal * 0.1)
            total_price = subtotal + tax
            return item["name"], price, discount, tax, total_price
        else:
            return "-", "-", "-", "-", "-"

    def display_menu(self):
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

    def display_order(self, menu_choice, quantity, name, price, discount, tax, total_price):
        print("--------------------------")
        print("Ananda Coffee")
        print("--------------------------")
        print("Menu:", name)
        print("Jumlah Pesan:", quantity)
        print("Harga:", price)
        print("Diskon:", discount)
        print("PPN:", tax)
        print("--------------------------")
        print("Jumlah Bayar:", total_price)
        print("--------------------------")


def main():
    coffee_menu = CoffeeMenu()
    choice = "Y"
    while choice == "Y":
        coffee_menu.display_menu()
        menu_choice = input("Masukkan list abjad menu kopi: ")
        quantity = int(input("Masukkan jumlah pesanan: "))
        name, price, discount, tax, total_price = coffee_menu.calculate_total_price(menu_choice, quantity)
        coffee_menu.display_order(menu_choice, quantity, name, price, discount, tax, total_price)
        choice = input("Apakah Anda ingin order kembali? (Y/N): ")


if __name__ == "__main__":
    main()

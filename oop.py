# class Laptop:
class Laptop: 
    # method & constructor & object
    def __init__(self, merk, tipe, harga):
        self.merk = merk
        self.tipe = tipe
        self.harga = harga
    # method
    def turnOn(self):
        print("Laptop menyala")
# instansiasi objek
my_laptop = Laptop("Asus", "Zenbook", 15000000)
print(my_laptop.merk, my_laptop.tipe, my_laptop.harga)
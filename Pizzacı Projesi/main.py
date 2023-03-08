import csv
from datetime import datetime

print("\nMERHABA BURGAZ PİZZAYA HOŞGELDİNİZ !!!!!\n")

# Menu.txt dosyasını oluşturur ve içine yazar
with open("Menu.txt", "w") as file:
    file.write(
        "* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik Pizza: **içinde; sadece sos olan pizza.**\n2: Margarita Pizza: **İçinde; sos ve özel eritilmiş peynirimiz olan pizza.**\n3: Türk Pizza: **İçinde; sos, eritilmiş peynir, sucuk, közlenmiş biber olan pizza.**\n4: Dominos Pizza: **İçinde; sos, eritilmiş peynir, közlenmiş biber olan pizza.**\n\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")


# Üst sınıf pizzayı oluşturur
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Alt sınıf oluştur “KlasikPizza”, “MargaritaPizza”, “TürkPizza” ve “DominosPizza”
class KlasikPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Klasik Pizza", 30.0)


class MargaritaPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Margarita Pizza", 37.0)


class TurkPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Türk Pizza", 50.0)


class DominosPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Dominos Pizza", 45.0)


# Üst sınıf “Decorator” sınıfını oluşturur ve miras aldırır
class Decorator(Pizza):
    def __init__(self, icindeki):
        self.icindeki = icindeki

    def get_cost(self):
        return self.icindeki.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.icindeki.get_description() + ' ' + Pizza.get_description(self)


# Sos sınıflarının tanımı
class Zeytin(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.cost = 8.0
        self.description = "Zeytin"

    def get_cost(self):
        return self.icindeki.get_cost() + self.cost

    def get_description(self):
        return self.icindeki.get_description() + ' ' + self.description

class Mantarlar(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.cost = 12.0
        self.description = "Mantarlar"

    def get_cost(self):
        return self.icindeki.get_cost() + self.cost

    def get_description(self):
        return self.icindeki.get_description() + ' ' + self.description


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.cost = 15.0
        self.description = "Keçi Peyniri"

    def get_cost(self):
        return self.icindeki.get_cost() + self.cost

    def get_description(self):
        return self.icindeki.get_description() + ' ' + self.description


class Et(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.cost = 25.0
        self.description = "Et"

    def get_cost(self):
        return self.icindeki.get_cost() + self.cost

    def get_description(self):
        return self.icindeki.get_description() + ' ' + self.description


class Sogan(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.cost = 6.0
        self.description = "Soğan"

    def get_cost(self):
        return self.icindeki.get_cost() + self.cost

    def get_description(self):
        return self.icindeki.get_description() + ' ' + self.description


class Misir(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.cost = 7.0
        self.description = "Mısır"

    def get_cost(self):
        return self.icindeki.get_cost() + self.cost

    def get_description(self):
        return self.icindeki.get_description() + ' ' + self.description


def main():
    menu = open("Menu.txt", "r")
    print(menu.read())
    menu.close()

    # pizza seçimi
    pizza_type = int(input("Pizza tabanı seçin (1-4): "))
    while pizza_type not in range(1, 5):
        pizza_type = int(input("Lütfen geçerli bir pizza seçimi yapın (1-4): "))

    # pizza nesnesini oluşturma
    if pizza_type == 1:
        pizza = KlasikPizza()
    elif pizza_type == 2:
        pizza = MargaritaPizza()
    elif pizza_type == 3:
        pizza = TurkPizza()
    else:
        pizza = DominosPizza()

    # sos seçimi ve sos nesnelerini oluşturma
    soslar = []
    sos_cesidleri = int(input("Sos seçin (11-16) çıkış için 0: "))
    while sos_cesidleri != 0:
        if sos_cesidleri not in range(11, 17):
            sos_cesidleri = int(input("Lütfen geçerli bir sos seçimi yapın (11-16) çıkış için 0: "))
            continue
        if sos_cesidleri == 11:
            sos = Zeytin(pizza)
        elif sos_cesidleri == 12:
            sos = Mantarlar(pizza)
        elif sos_cesidleri == 13:
            sos = KeciPeyniri(pizza)
        elif sos_cesidleri == 14:
            sos = Et(pizza)
        elif sos_cesidleri == 15:
            sos = Sogan(pizza)
        else:
            sos = Misir(pizza)
        soslar.append(sos)
        sos_cesidleri = int(input("Başka sos eklemek için sos seçin (11-16) çıkış için 0: "))

    # toplam tutar hesaplama, burada sosları bir liste haline alıp liste ile döndüyor
    total_cost = pizza.get_cost()
    description = pizza.get_description()
    for sos in soslar:
        total_cost += sos.get_cost()
        description += " " + sos.get_description()

    # sipariş bilgileri alma
    name = input("İsim: ")
    Tc_kimlik = input("TC Kimlik Numarası: ")
    Kredi_karti_numarasi = input("Kredi Kartı Numarası: ")
    Kredi_karti_sifresi = input("Kredi Kartı Şifresi: ")

    # sipariş bilgileri veritabanına ekleme
    siparis_tarihi = datetime.now()
    siparis_tarihi_str = siparis_tarihi.strftime('%d/%m/%Y %H:%M:%S')
    with open("Orders_Database.csv", mode="a") as kisi_bilgileri:
        kisi_bilgileri_yaz = csv.writer(kisi_bilgileri, delimiter="-")
        kisi_bilgileri_yaz.writerow(
            [name, Tc_kimlik, Kredi_karti_numarasi, description, total_cost, siparis_tarihi_str, Kredi_karti_sifresi])

    print("\nSiparişiniz başarıyla alınmıştır, Afiyet Olsun ! ")
    print(f"Seçilen Pizza: {description}")
    print(f"Toplam Tutar: {total_cost:.2f} TL")


main()
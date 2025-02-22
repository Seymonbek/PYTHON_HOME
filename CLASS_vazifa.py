# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda
# ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni
# chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.


class User:
    def __init__(self,ism,familiya,t_yil,f_ismi = None,email = None,parol = None,tel = None):
        self.ism = ism
        self.f_ismi = f_ismi
        self.email = email
        self.parol = parol
        self.tel = tel
        self.t_yil = t_yil
        self.familiya = familiya

    def get_age(self, yil):
        return f"{self.ism} {self.familiya} {yil - self.t_yil}-yoshda"

    def get_info(self):
        info = (f"Mening ismim {self.ism} familiyam {self.familiya}.\n"
              f"{self.t_yil}-yilda tug'ilganman.\n")
        if self.email:
            info += f"email: {self.email}"
        if self.parol:
            info += f"parol: {self.parol}"
        if self.f_ismi:
            info += f"Foydalanuvchi ismim: {self.f_ismi}"
        if self.tel:
            info += f"Tel raqamim: {self.tel}"
        return info

talaba1 = User("Ali","Valiyev",2000,email="Alivaliyev@gamil.com\n",tel="+998996661122\n",f_ismi="A_Valiyev\n")
talaba2 = User("Olim","Olimov",1995)

print(talaba1.get_info())
print(talaba1.get_age(2025))
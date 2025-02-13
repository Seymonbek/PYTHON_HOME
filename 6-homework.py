# 1. "user_data" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor(first_name, last_name, age).
# Input orqalik ism, familiya va yoshni kiritamiz. va bu qiymatlarni "user_data" funksiyasini chaqirib
# argumentlariga beramiz. "user_data" funksiyasi bu(first_name, last_name, age) o'zgaruvchilarni qiymatini
#
# Ism: Alisher
# Familiya: Olimov
# Yosh: 27
#
# ko'rinishiga print qilib bersin.

# 2. "find_max" funksiyasini elon qilasizlar. Funksiyani 3 ta parametri bor(a, b, c).
# Input orqalik 3 ta son kiritamiz. va bu sonlarni "find_max" funksiyasi chaqirib argumentlariga beramiz.
# "find_max" funksiyasini bu(a, b, c) o'zgaruvchilardan eng kattasini topib print qiladi.
#
# Eng katta son - A = 10 yoki Eng katta son - A va B = 10 yoki Eng katta son - A va B va C = 10

# 3. "find_letter_count" funksiyasini elon qilasizlar. Funksiyani 2 ta parametri bor(word, letter).
# Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi bolgan so'zimizni kiritamiz.
# va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
# "find_letter_count" funksiyasi bu(word, letter) o'garuvchilardan foydalanib "word" da "letter" nechi martda
# qatnashganini print qilsin.
# "Programing" so'zida "r" dan 2 ta.

# 4. "list_sum" funksiyasi elon qilasizlar. Funksiyani 1 ta pametrni bor(myList).
# "myList" funksiyasini chaqirib unda argumentini berasizlar.
# uni ichida esa myList elementlarini yig'indisini print qilasizlar.
# Listning elementlar yig'indisi = 32


# def user_data(first_name, last_name, age):
#
#     print(f"Ismi: {first_name}\n"
#           f"Familiyasi: {last_name}\n"
#           f"Yoshi: {age}")
#
# first_name = input("Ismingizni kiriting: ")
# last_name = input("Familiyangizni kiriting: ")
# age = input("Yoshingizni kiriting: ")
#
# user_data(first_name,last_name,age)

# def find_max(a,b,c):
#     max_e = max(a,b,c)
#     print(f"Eng katta son {max_e}")
# a=int(input("Birinchi sonni kiriting: "))
# b=int(input("Ikkinchi sonni kiriting: "))
# c=int(input("Uchinchi sonni kiriting: "))
#
# find_max(a,b,c)

# def find_letter_count(word,letter):
#     count = word.count(letter)
#     print(f"{word} so'zida {letter} dan {count} ta.")
#
# word = input("So'zni kiriting: ")
# letter = input("Qaysi harfni hisoblamoqchisiz: ")
#
# find_letter_count(word,letter)

# def list_sum(Mylist):
#     total = sum(Mylist)
#     print(f"Ro'yxatdagi elementlar yig'indisi {total}.")
#
# Mylist = [5,7,8,12]
# list_sum(Mylist)
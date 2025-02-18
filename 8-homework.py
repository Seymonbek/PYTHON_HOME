# 1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha guruhlaydigan str_counter(strs)funksiya yozing,
# bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
# M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}
#
#
# 2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning
# elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan
# merge_list(l1,l2) funksiya yarating.
# M: list_1 = ["a", "b", "c"]
#    list_2 = [1, 2, 3]
#    merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}
#
#
# 3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish
# imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
# M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}
#
#
# 4. Raqamlar ro'yxatini oladigan va ro'yxatdagi har bir raqamning takrorlanish sonini o'z ichiga
# olgan dict qaytaradigan counter_dict(nums) nomli funksiya yozing.
# M: counter_dict([2,1,1,1) -> {2:1, 1:3} Chunki listda 1ta 2 va 3ta 1bor.
#
#
# 5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
# o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
# max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }) -> {"Zafar":80, "Nodir":76}


# 1-misol
# def str_counter(strs):
#    counter = {}
#    for s in strs:
#       length = len(s)
#       if length in counter:
#          counter[length].append(s)
#       else:
#          counter[length] = [s]
#    return counter
# result = str_counter(['shaftoli', 'olma', 'nok', 'banan'])
# print(result)


# 2-misol
# def merge_list(l1,l2):
#    result = {}
#    for i in range(len(l1)):
#       result[l1[i]] = l2[i]
#    return result
#
# list_l1 = ['a', 'b', 'c']
# list_l2 = [1,2,3]
# print(merge_list(list_l1,list_l2))


# 3-misol
# contacts = {
#    "Ali":"+998991656511",
#    "Vali":"+998942356565"
# }
# def add_contact(contacts,name,phone):
#    if name in contacts:
#       print("Bu kontakt allaqachon mavjud!")
#    else:
#       contacts[name] = phone
#       print(f"{name} kontaktga qo'shildi.")
#
# def update_contact(contacts,name,new_phone):
#    if name in contacts:
#       contacts[name] = new_phone
#       print(f"{name}ning kontakti yangilandi.")
#    else:
#       print("Bunday kontakt mavjud emas.")
#
# def del_contact(contacts,name):
#    if name in contacts:
#       del contacts[name]
#       print(f"{name} kontaktdan o'chirildi.")
#    else:
#       print("Bunday kontakt topilmadi.")
#
# def search_contact(contacts,name):
#    if name.titl in contacts:
#       print(f"{name} : {contacts[name]}")
#    else:
#       print("Bunday kontakt topilmadi.")
#
# add_contact(contacts,"hasan","+998993151515")
# search_contact(contacts,"Ali")


# 4-misol
# def counter_dic(nums):
#    count = {}
#    for num in nums:
#       if num in count:
#          count[num] += 1
#       else:
#          count[num] = 1
#
#    return count
# nums = [1,2,3,2,2,1,3]
# print(counter_dic(nums))


# 5-misol
# def max_ball_students(talabalar):
#    max1, max2 = 0,0
#    max1_student = ''
#    max2_student = ''
#    for ism,ball in talabalar.items():
#       if ball > max1:
#          max2,max2_student = max1,max1_student
#          max1,max1_student = ball,ism
#       elif ball > max2:
#          max2,max2_student = ball,ism
#    return {max1_student:max1,max2_student:max2}
#
# talabalar = {
#       "Akmal": 56,
#       "Ali":78,
#       "Vali":90,
#       "Hasan":86,
#       "Husan":95
#    }
#
# print(max_ball_students(talabalar))
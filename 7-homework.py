# 5. daraja(a, b) - bu funksiya a ni b darajasini print qilsin.
#
# 6. daraja4(a, b, c, d) - bu funksiya a ni b, c va d chi darajasini print qilsin.
#
# 7. digit_count_and_sum(word) - bu funksiya "word" ni ichidagi raqamni aniqlab ularni yig'indisini va
# nechtaligini print qilsin.
#
# 8. add_right(a, b) - bu funksiya a sonini o'ng tomoniga b sonini birlashtirib qoysin va print qilsin.
#
# 9. add_left(a, b) - bu funksiya a sonini chap tomoniga b sonini birlashtirib qoysin va print qilsin.
#
# 10. work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga ko'paytirib
# qiymatini o'zgartiradi va listni print qilsin.
#
# 11. big_sales(sales) funksiyasini yarating.
# sales bu dictionary:
# {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
#
# qaysi oyda eng ko'p sotuv bolgan bo'lganini return qilsin.
#
# 12. min_max(numbers, max_num, min_num) max_num numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlang,
# min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang
#
# 13. expensiveProduct(products) - funksiyadagi products - list.
# Unga products sifatida [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ] shunaqa qiymat beriladi.
# Eng qimmat telefon nomini print qilib bersin bu funksiya.





# def daraja(a,b):
#     c = a**b
#     return c
#
# print(daraja(2,3))

# def daraja4(a,b,c,d):
#     x = a**b
#     y = a**c
#     z = a**d
#     return x,y,z
#
# print(daraja4(2,2,3,4))

# def digit_count_and_sum(word):
#     S=0
#     K=0
#     for son in word:
#         if son.isdigit():
#             S+=int(son)
#             K+=1
#     print(f"Raqamlar yig'indisi: {S}")
#     print(f"Raqamlar soni: {K}")
#
# digit_count_and_sum("jhgsdjakoieru9283yuwejoirghifuweqoi2984uiweoq3289u4ie")

# def add_right(a, b):
#     natija = str(a)+str(b)
#     return int(natija)
# natija = add_right(21564,32564)
# print(natija)

# def add_left(a, b):
#     natija = str(b)+str(a)
#     return int(natija)
# natija = add_left(21564,32564)
# print(natija)

# def work_with_list(a):
#     kichik_son = min(a)
#     for i in range(len(a)):
#         a[i] *= kichik_son
#     print(a)
#
# a = [3,5,2,8]
# work_with_list(a)

# def big_sales(sales):
#     max_oy = ""
#     max_narx = 0
#     for oy,narx in sales.items():
#         if narx>max_narx:
#             max_narx = narx
#             max_oy = oy
#     return max_oy
# malumot = {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
# natija = big_sales(malumot)
# print(natija)

# def min_max(numbers, max_num, min_num):
#     min_son = min(numbers)
#     max_son = max(numbers)
#
#     if min_son == min_num:
#     print(f"{min_num} funksiyadagi eng kichik son: ")
#     else:
#     print(f"")
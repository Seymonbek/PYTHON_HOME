# while True:
#     rang = input('Svetafor qaysi rangda? ').lower()
#     if rang in['qizil', 'sariq', 'yashil']:
#         print("Raxmat, to'g'ri keldi.")
#     else:
#         print("Bu xato rang, qaytadan urinib ko'ring")

# import random
#
# def sontop(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
#         elif taxmin>tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
#         else:
#             break
#     print(f"Tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")
#     return  taxminlar
#
# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha bo'lgan son o'ylang va istalgan tugmani bosing. Men topaman. ")
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         if quyi != yuqori:
#             taxmin = random.randint(quyi,yuqori)
#         else:
#             taxmin = quyi
#         javob = input(f"Siz {taxmin} sonini o'yladingiz:\n to'g'ri(t),"
#                       f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-) ni bosing >>>".lower())
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {taxminlar} ta taxmin bilan topdim!")
#     return taxminlar
#
# def play(x=10):
#     yana =True
#     while yana:
#         taxminlar_user = sontop(x)
#         taxminlar_pc = sontop_pc(x)
#
#         if taxminlar_pc>taxminlar_user:
#             print(f"Tabriklaymiz siz yutdingiz.")
#         elif taxminlar_user>taxminlar_pc:
#             print(f"Men yutdim.")
#         else:
#             print("Durrang")
#         yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): "))
# print(play())

# dostlar = []
# while True:
#     ism = input("DO'STLARINGIZNI ISMINI KIRITING: ")
#     if ism.lower() == "stop":
#         break
#     dostlar.append(ism)
#
# print("\nDo'stlaringiz ro'yxati: ")
#
# for dost in dostlar:
#     print(f"{dost}")


# kurs = 12600  # 1 USD = 12,600 UZS
# while True:
#     valuta = input("So'mni kiriting (yoki 'exit' deb yozing): ")
#     if valuta.lower() == "exit":
#         print("Dastur tugatildi.")
#         break
#     if valuta.isdigit():
#         uzs = int(valuta)
#         usd = uzs / kurs
#         print(f"{uzs} so'm = {usd:.2f} USD")
#     else:
#         print("Iltimos, to'g'ri raqam kiriting!")

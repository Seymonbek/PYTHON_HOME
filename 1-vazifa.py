# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for pochta in pochtalar:
#     if '@' in pochta:
#         print("Manzilingiz tog'ri")
#     else:
#         print("Manzilingiz noto'g'ri!")

# parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# # for parol in parollar:
# #     if len(parol) < 8:
# #         print(f'parol "{parol}" juda qisqa.')
# #     elif parol.isalnum():
# #         print(f'parol "{parol}" kuchsiz.')
# #     else:
# #         print(f'"{parol}" kuchli parol')

# darajalar = [20,22, 19, 24, 25, 23, 21]
# # s = 0
# for daraja in darajalar:
#     # s+=daraja
#     # ortacha = s/len(darajalar)
#     # print(ortacha)
#     if daraja >= 22:
#         print("Iliq kun.")
#     else:
#         print("Salqin kun.")

# taomlar =  ["Osh", "Shashlik", "Manti","Lag’mon" ]
# buyurtma = input("Nima yeyishni hohlaysiz.")
# for taom in taomlar:
#     if taom.lower() == buyurtma.lower():
#         print("Buyurtmangiz qabul qilindi")
#         break
#     else:
#         print("Kechirasiz, bunday taom yo'q")
#     break

# F_yoshlari = [16, 21, 17, 30, 25]
# for yosh in F_yoshlari:
#     if yosh > 18:
#         print("Xush kelibsiz.")
#     else:
#         print("Yosh chegarasi yetmagan.")

# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for xabar in xabarlar:
#     if xabar == "Batareya past":
#         print("Telefoningizni quvvatlang")

# fayllar = [ "kitob.jpg", "kok jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
# musiqalar = []
# rasmlar = []
# for fayl in fayllar:
#     if fayl.find(".jpg") != -1:
#         rasmlar.append(fayl)
#     elif fayl.find(".mp3") != -1:
#         musiqalar.append(fayl)
# print("Rasmlar: ",rasmlar)
# print("Musiqalar: ",musiqalar)
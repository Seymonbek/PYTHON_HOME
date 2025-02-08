# davlatlar = {
#     'AQSH' : 'Washington',
#     'Italiya':'Rim',
#     'MALAYZIYA':'Kuala-Lumpur',
#     'O\'ZBEKISTON':'Toshkent',
#     'QIRG\'IZISTON':'Bishkek',
#     'QOZOG\'ISTON':'Nursulton',
#     'ROSSIYA':'Moskva',
#     'SINGAPUR':'Singapur',
#     'TOJIKISTON':'Dushanbe'
# }
# print("Davlat nomlari: ")
# for davlat in sorted(davlatlar):
#     print(davlat.title())
# print("\nPoytaxt nomlari: ")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# davlatlar = {
#     'AQSH' : 'Washington',
#     'Italiya':'Rim',
#     'MALAYZIYA':'Kuala-Lumpur',
#     'O\'ZBEKISTON':'Toshkent',
#     'QIRG\'IZISTON':'Bishkek',
#     'QOZOG\'ISTON':'Nursulton',
#     'ROSSIYA':'Moskva',
#     'SINGAPUR':'Singapur',
#     'TOJIKISTON':'Dushanbe'
# }
# davlat = input("Qaysi davlatning poytaxtini bilishni xoxlaysiz? ")
# if davlat.upper() in davlatlar:
#     print(f"{davlat.upper()} ning poytaxti {davlatlar[davlat.upper()]}")

# menu = {
#     "Palov": 30000,
#     "Manti": 25000,
#     "Shashlik": 20000,
#     "Lag'mon": 35000,
#     "Somsa": 15000,
#     "Osh": 18000,
#     "Norin": 40000,
#     "Sho'rva": 30000,
#     "Barak": 28000,
#     "Kebab": 32000
# }
# print("Iltimos buyurtma qilmoqchi bo'lgan uchta taomingizni kiriting: ")
# buyurtmalar = []
# for i in range(1, 4):
#     taom = input(f"{i}-taomni kiriting: ").strip()
#     buyurtmalar.append(taom.title())
# print("\nBuyurtmalaringiz holati: ")
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"{taom}: {menu[taom]} so'm")
#     else:
#         print(f"{taom}: Bizda bunday taom yo'q")
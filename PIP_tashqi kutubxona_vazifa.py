# import datetime as dt
#
# hozir = dt.datetime.now()
# print(hozir)
#
# # sanani ajratib olish
# print(hozir.date())
#
# # vaqtni ajratib olish
# print(hozir.time())
#
# # soatni ajratib olish
# print(hozir.hour)
#
# # minutni ajratib olish
# print(hozir.minute)
#
# # sekundni ajratib olish
# print(hozir.second)
#
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
#
# ertaga = dt.date(2021, 3, 10)
# print(f"Ertangi sana: {ertaga}")
#
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
#
# vaqtKeyin = dt.time(23,45,00)
#
# bugun = dt.date.today()
# ramazon = dt.date(2024, 4, 10)
# farq = ramazon-bugun
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")
#
# hozir = dt.datetime.now()
# futbol = dt.datetime(2023, 3, 10, 23, 45, 00)
# farq= futbol-hozir
# sekundlar = farq.seconds
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
# print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
# print(f"Futbol boshlanishiga {minutlar} minut qoldi")
# print(f"Futbol boshlanishiga {soatlar} soat qoldi")
#
# # vaqtni millisekundsiz chiqaramiz
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")
#
# # sanani kun-oy-yil koʻrinishida chiqaramiz
# sana = hozir.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")
#
# # sanani kun/oy/yil koʻrinishida chiqaramiz
# sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
# print(sana_vaqt)

# from uzwords import words
# andoza = "^т...р$"
#
# matches = []
# for word in words:
#     if re.match(andoza,word):
#         matches.append(word)
# print(matches)
#
# matn = """Maqolalar  2023-yilning 20-martiga qadar jonibekdev@gmail.com elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
#
# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)
#
# # Kuchli parolni tekshirish
# # Quyidagi andoza ham ihateregex.io sahifasidan olindi
# andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# msg = "Yangi parol kiriting"
# msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
# msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '
#
# while True:
#     password = input(msg)
#     if re.match(andoza,password):
#         print("Maxfiy so'z qabul qilindi")
#         break
#     else:
#         print("Maxfiy so'z talabga javob bermadi")

# from googletrans import Translator
# tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
# tarjima = tarjimon.translate(matn_uz)
# print(tarjima.text)

# import requests
# from pprint import pprint
#
# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)

# import requests
# from pprint import pprint as print
#
# API_KEY = ''
#
# currency='USD'
# url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
# response = requests.get(url)
# kurs = response.json()['conversion_rate']
# print(f"1 dollar kursi {kurs} so'mga teng")

# import requests
# from bs4 import BeautifulSoup
#
# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
#
#
# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
# print(news[0].text) # eng birinchi yangilikni konsolga chiqaramiz

# import requests
#
# from bs4 import BeautifulSoup
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
#
# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title")
# matn = ""
# for n in news:
#     matn += n.text
#
# # kerakmas so'zlar
# stopwords = ["учун", "бўйича", "лекин", "билан", "ва", "бор", "ҳам", "хил", "йил"]
# # bulutni yaratamiz
# wordcloud = WordCloud(width=1000, height=1000,
#                       background_color='white',
#                       stopwords=stopwords,
#                       min_font_size=20).generate(matn)
#
# # plot the WordCloud image
# plt.figure(figsize=(8, 8), facecolor=None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad=0)
# plt.show()

# import cv2
#
# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#
# while True:
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#         roi_gray = gray[y:y+w, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
#
#     cv2.imshow('frame', frame)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
# # copyright Tim Ruscia aka techwithtim
# # code from https://github.com/techwithtim/OpenCV-Tutorials

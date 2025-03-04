# 1
import json
data = {
    "Model":"Malibu",
    "Rang":"Qora",
    "Yil":2020,
    "Narx":40000
}

data_json = json.dumps(data)
print(data_json)

with open("data.json","w") as file:
    json.dump(data,file,indent=3)


# 2
import json
talaba_json = {
    "Ism":"Hasan",
    "Familiya":"Husanov",
    "Tyil":2020
}
Talaba_json = json.dumps(talaba_json)
print(Talaba_json)

with open("Talaba.json","w") as file:
    json.dump(talaba_json,file,indent=3)


# 3
with open('pi_million_digits.txt') as file:
    pi = file.read()

def check_num():
    t_yil = input("Tug'ilgan sanangiz: ")
    ishora = True
    while ishora:
        if not t_yil in pi:
            ishora = False
            print("Sizning tug'ilgan sanangiz bu raqamlar ichida yo'q! ")

        else:
            print("Sizning tug'ilgan kuniningiz bor! ")

            import pickle
            with open("info.dat","wb") as fayl:
                pickle.dump(t_yil,fayl)
            break
check_num()
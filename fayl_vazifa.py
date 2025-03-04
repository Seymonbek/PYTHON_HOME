import pickle
with open("pi_million_digits.txt") as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace(' ','')

birthday = "05062006"
print(birthday in pi)

pi = float(pi)
with open("pi_million_digits.txt", "wb") as file:
    pickle.dump(pi,file)
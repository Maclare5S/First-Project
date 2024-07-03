import random

cara = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
long = int(input("Introduce la longitud de tu contrasena: "))
con = ("")

for i in range(long):
    con += random.choice(cara)

print(con)

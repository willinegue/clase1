import random

signos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingrese la longitud de la contraseña: "))

contrasena = ""
for i in range(longitud):
    contrasena += random.choice(signos)
print(contrasena)

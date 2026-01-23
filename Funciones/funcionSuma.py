def saber_mayor_edad(age):
    if age >= 18:
        return "Usuario MAYOR de edad!!!"
    elif age < 18:
        return "Usuario MENOR de edad!!!"
    else:
        return  "Usuario extraño!!!"
n = int(input("Ingrese edad del USUARIO: "))
print(saber_mayor_edad(n))
    
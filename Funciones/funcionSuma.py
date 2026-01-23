def saber_mayor_edad(age):
    if age >= 18:
        return "Usuario MAYOR de edad!!!"
    elif age < 18:
        return "Usuario MENOR de edad!!!"
    else:
        return  "Usuario extraño!!!"
n = int(input("Ingrese edad del USUARIO: "))
def sumar_10_a_tu_edad(age):
    operacion = age + 10
    return operacion
print(saber_mayor_edad(n))
print(sumar_10_a_tu_edad(n))
    
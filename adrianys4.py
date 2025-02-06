#Pide un numero al usuario
a1 = float(input("dime un numero:"))
b2 = float(input("dime otro numero"))
c3 = float(input("dime otro numero"))

#determina el mayor de los tres numeros
if a1 >= b2 and a1 >= c3:
    mayor = a1
elif b2 >= a1 and b2 >= c3:
    mayor = b2
else:
    mayor = c3
    # determinaren menor de los tres numeros
if a1 <= b2 and a1 <= c3:
    menor = a1
elif b2 <= a1 and b2 <= c3:
    menor = b2
else: 
    menor = c3
        # imprimir los resultados 
print(f" el mayor de los tres numeros es :{mayor} ")
print(f" el menor de los tres numeros es :{menor} ")
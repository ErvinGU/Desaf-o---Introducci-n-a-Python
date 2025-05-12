import math as m


#calcular la rentabilidad
#𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

P = float(input("Ingrese el valor de la suscripción : "))
U = float(input("Ingrese la cantidad de usuarios normales : "))
GT = float(input("Ingrese los gastos totales : "))

if P < 0 or U < 0 or GT < 0:
    print("Advertencia: Se han ingresado valores negativos, lo cual podría impedir un buen funcionamiento del programa.")

utilidades = P * U - GT

print(f"Resumen utilidades : {utilidades:.2f}")

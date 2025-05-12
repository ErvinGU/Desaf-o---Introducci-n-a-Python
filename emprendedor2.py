import math as m


#calcular la rentabilidad Recargo 50%
#𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

P = float(input("Ingrese el valor de la suscripción : "))
Unormal = float(input("Ingrese la cantidad de usuarios normales : "))
Upremium = float(input("Ingrese la cantidad de usuarios premium : "))
GT = float(input("Ingrese los gastos totales : "))

if P < 0 or Unormal < 0 or Upremium < 0 or GT < 0:
    print("Advertencia: Se han ingresado valores negativos, lo cual podría impedir un buen funcionamiento del programa.")

utilidades = (P * Unormal) + (P + Upremium) - GT

print(f"Resumen utilidades : {utilidades:.2f}")

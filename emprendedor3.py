import math as m


#calcular la rentabilidad Recargo 50%
#𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

P = float(input("Ingrese el valor de la suscripción : "))
U = float(input("Ingrese la cantidad de usuarios normales : "))
GT = float(input("Ingrese los gastos totales : "))
Uanterior = float(input("Ingrese las utilidades del año anterior : "))


if P < 0 or Uanterior < 0 < 0 or GT < 0:
    print("Advertencia: Se han ingresado valores negativos, lo cual podría impedir un buen funcionamiento del programa.")

Uactual = P * U - GT
print(f"Resumen utilidades  actuales : {Uactual:.2f}")

if Uanterior == 0:
    print("No se puede calcular la razón, ya que las utilidades del año anterior son 0.")

else:
    razon = Uactual / Uanterior
    print(f"La razón entre las utilidades actuales y las del año anterior es : {razon:.2f}")


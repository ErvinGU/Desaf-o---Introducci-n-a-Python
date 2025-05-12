import math as m


#Calcular velocidad de escape
#formula : √ 2*G*r

g = float(input("ingrese constante de g [m/s²] : "))
r = float(input("ingrese el radio en kilometros [Km] : ")) #se multiplicará por 1000 para transformar a metros

ve = (m.sqrt(2 * g * (r * 1000)))

print(f"La velocidad de Escape es : {ve:.1f} [m/s]")


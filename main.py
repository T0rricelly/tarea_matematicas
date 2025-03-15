import math
import matplotlib.pyplot as plt

def main():
    # Datos 
    a = int(input("Ingrese el valor del lado a: "))
    b = int(input("Ingrese el valor del lado b: "))
    c = int(input("Ingrese el valor del lado c: "))
    # validacion
    if a + b <= c or b + c <= a or a + c <= b:
        print("No es un triangulo valido")
    else:
        print("Es un triangulo")
        
    Anguloa= math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
    Angulob= math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
    Anguloc= 180-(Anguloa+Angulob)

    if Anguloa==90 or Angulob==90 or Anguloc==90:
        print(f"su triangulo tiene un angulo de 90°\es un triangulo rectangulo\nAngulo A--> {Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C--> {Anguloc}°")
    elif Anguloa>90 or Angulob>90 or Anguloc>90:
        print(f"Su triangulo tiene un angulo mayor a 90°\nes un triangulo obtusangulo\nAngulo A--> {Anguloa}°\nAngulo B-->{Angulob}°\nAngulo C-->{Anguloc}°")
    else:
        print(f"Su triangulo no tiene angulos mayores o iguales a 90°\es un angulo acutangulo\nAngulo A-->{Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C-->{Anguloc}°")

    if a ==b == c:
        print("es un triangulo equilatero")
    elif a  ==b or a ==c or b == c : 
        print("es un triangulo isosceles")
    else: 
        print("es un triangulo escaleno ")

main()

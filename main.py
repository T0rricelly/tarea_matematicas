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
        # Caracterizacion del triangulo
        Anguloa= math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
        Angulob= math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
        Anguloc= 180-(Anguloa+Angulob)
        # Validacion de angulos
        if Anguloa==90 or Angulob==90 or Anguloc==90:
            print(f"su triangulo tiene un angulo de 90°\nes un triangulo rectangulo\nAngulo A--> {Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C--> {Anguloc}°")
        elif Anguloa>90 or Angulob>90 or Anguloc>90:
            print(f"Su triangulo tiene un angulo mayor a 90°\nes un triangulo obtusangulo\nAngulo A--> {Anguloa}°\nAngulo B-->{Angulob}°\nAngulo C-->{Anguloc}°")
        else:
            print(f"Su triangulo no tiene angulos mayores o iguales a 90°\nes un angulo acutangulo\nAngulo A-->{Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C-->{Anguloc}°")
        # Validacion de lados
        if a == b == c:
            tipo = "Equilatero"
            print("es un triangulo equilatero")
        elif a  == b or a == c or b == c : 
            tipo = "Isosceles"
            print("es un triangulo isosceles")
        else: 
            tipo = "Escaleno"
            print("es un triangulo escaleno ")
            
        # Graficar el codigo
        
        # Coordenadas de (A)
        Ax = 0
        Ay = 0

        # Coordenadas de (B)
        Bx = c
        By = 0

        # Coordenadas de (C)
        Cx = (b**2 + c**2 - a**2) / (2 * c)
        Cy = math.sqrt(b**2 - Cx**2)

        # Puntos del triángulo
        puntos = [[Ax, Ay], [Bx, By], [Cx, Cy], [Ax, Ay]]

        # Desempaqueta las coordenadas x, y para graficar
        x, y = zip(*puntos)
        
        # Resultado
        # x = (0, 3, 0, 0)
        # y = (0, 0, 4, 0)
        
        # Etiquetas para los vértices
        
        plt.text(Ax, Ay, 'A', fontsize=12, ha='right', va='bottom')  
        plt.text(Bx, By, 'B', fontsize=12, ha='left', va='bottom')    
        plt.text(Cx, Cy, 'C', fontsize=12, ha='left', va='bottom')   
        
        # Configuracion de la grafica
        plt.title(f"Triangulo {tipo}")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.grid(True)
        plt.plot(x, y, marker='o')
        plt.fill(x, y, 'lightblue')
        plt.show()
    
main()

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

quadrado = a**2
triangulo = a*b / 2
trapezio = (a+b) * c / 2

print(f"Area do quadrado: {quadrado:.4f}")
print(f"Area do triangulo: {triangulo:.4f}")
print(f"Area do trapezio: {trapezio:.4f}")
numero = int(input("Ingrese un número: "))

a, b = 0, 1

print("Serie Fibonacci:")
for _ in range(numero):
    print(a, end=" ")
    a, b= b, a + b
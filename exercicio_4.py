import math

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def calcular_seno_taylor(x):
    seno_taylor = 0
    for i in range(5):
        termo = ((-1) ** i) * (x ** (2 * i + 1)) / fatorial(2 * i + 1)
        seno_taylor += termo
    return seno_taylor

def main():
    while True:
        try:
            x = float(input("Informe o valor de x (em radianos, no 1º quadrante, ou seja, entre 0 e π/2): "))
            if x < 0 or x > math.pi / 2:
                print("O valor de x deve estar no intervalo [0, π/2].")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    seno_taylor = calcular_seno_taylor(x)
    seno_math = math.sin(x)

    print(f"\nValor calculado pelo método de Taylor: {seno_taylor:.10f}")
    print(f"Valor calculado pela função math.sin: {seno_math:.10f}")

if __name__ == "__main__":
    main()

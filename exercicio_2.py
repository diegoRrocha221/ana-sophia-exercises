def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        try:
            celsius = float(input("Informe a temperatura em graus Celsius: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()

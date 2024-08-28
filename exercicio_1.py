def get_float_input(prompt, min_value=None, max_value=None, decimals=2):
    while True:
        try:
            user_input = input(prompt)
            value = round(float(user_input), decimals)
            if min_value is not None and value < min_value:
                print(f"O valor deve ser maior ou igual a {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"O valor deve ser menor ou igual a {max_value}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def main():
    print("Bem-vindo ao calculador de preços de terrenos!")

    largura = get_float_input("Informe a largura do terreno (em metros): ", min_value=0.1, decimals=1)
    comprimento = get_float_input("Informe o comprimento do terreno (em metros): ", min_value=0.1, decimals=1)
    preco_metro_quadrado = get_float_input("Informe o valor do metro quadrado do terreno (em reais): ", min_value=0.01, decimals=2)

    area = round(largura * comprimento, 2)
    preco_terreno = round(area * preco_metro_quadrado, 2)

    print(f"\nÁrea do terreno: {area:.2f} m²")
    print(f"Preço do terreno: R$ {preco_terreno:.2f}")

if __name__ == "__main__":
    main()

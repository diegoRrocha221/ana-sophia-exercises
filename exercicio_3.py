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

def calcular_pagamento(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    salario_com_bonus = salario_bruto * 1.10
    return round(salario_com_bonus, 2)

def main():
    print("Calculadora de Pagamento de Funcionário\n")

    valor_hora = get_float_input("Informe o valor da hora de trabalho (em reais): ", min_value=0.01, decimals=2)
    horas_trabalhadas = get_float_input("Informe o número de horas trabalhadas no mês: ", min_value=0.1, decimals=2)

    pagamento = calcular_pagamento(valor_hora, horas_trabalhadas)

    print(f"\nO valor a ser pago ao funcionário, incluindo 10% de bônus, é: R$ {pagamento:.2f}")

if __name__ == "__main__":
    main()

import requests


def converter_moeda(valor, moeda_origem, moeda_destino):
    """
    converte um valor de uma moeda para outra usando a api ExchangeRate-API

    Args:
        valor (float): O valor a ser convertido.
        moeda_origem (str): A moeda de origem (ex: 'USD').
        moeda_destino (str): A moeda de destino (ex: 'BRL').

    Returns:
        float: O valor convertido, ou uma mensagem de erro caso algo falhe
    """
    url = f"https://v6.exchangerate-api.com/v6/SUA_CHAVE_API/latest/{moeda_origem}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção se o status HTTP for um erro.
        
        data = response.json()
        taxa_cambio = data["conversion_rates"].get(moeda_destino)

        if taxa_cambio:
            return valor * taxa_cambio
        else:
            return f"Moeda de destino '{moeda_destino}' não encontrada."
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API: {e}"

# Interface
if __name__ == "__main__":
    print("=== Conversor de Moeda ===")
    
    try:
        valor = float(input("Digite o valor a ser convertido: "))
        moeda_origem = input("Digite a moeda de origem (ex: USD): ").upper()
        moeda_destino = input("Digite a moeda de destino (ex: BRL): ").upper()

        resultado = converter_moeda(valor, moeda_origem, moeda_destino)

        if isinstance(resultado, float):
            print(f"{valor:.2f} {moeda_origem} é igual a {resultado:.2f} {moeda_destino}")
        else:
            print(resultado)
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido para o valor a ser convertido.")

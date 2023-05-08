import os
import json
from lib_cotacao_moeda_sqn import avaliar_dollar


def lambda_handler(event, context):
    
    # Obtendo a moeda base (BRL) para cotacao do dolar.
    base_currency = event['base_currency']
    
    # Obtendo a API key do ExchangeRate via variavel de ambiente.
    api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
    
    # Executando a lib de cotacao.
    dollar_rate = avaliar_dollar(base_currency, api_key)

    # Retornando a cotacao do dolar.
    return {
        "statusCode": 200,
        "body": json.dumps({
            "dollar_rate": dollar_rate
        }),
        "headers": {
            "Content-Type": "application/json"
        }
    }

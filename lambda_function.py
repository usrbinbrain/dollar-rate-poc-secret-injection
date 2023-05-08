import os
import json
from lib_cotacao_moeda_sqn import avaliar_dollar
import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "poc/dollar-rate/apikeyy"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    return get_secret_value_response['SecretString']

def lambda_handler(event, context):
    
    # Obtendo a moeda base (BRL) para cotacao do dolar.
    base_currency = event['base_currency']
    
    # Obtendo a API key do ExchangeRate via variavel de ambiente.
    #api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
    api_key = get_secret()
    
    
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

# dollar-rate-poc-secret-injection

**Este projeto Python é uma Prova de Conceito (PoC) para demonstrar a possibilidade de um ataque de injeção de pacote em uma função AWS Lambda.**

A função lambda principal está no arquivo `lambda_function.py`, Ela importa a biblioteca maliciosa e usa a função `avaliar_dollar` para obter a taxa de câmbio do dólar para a moeda base fornecida no evento de entrada, a função lambda retorna um objeto JSON com a moeda base e a taxa de câmbio do dólar.

O projeto contém uma biblioteca maliciosa disfarçada como uma biblioteca legítima que obtém a taxa de câmbio do dólar para uma moeda base usando a [API do ExchangeRate](https://www.exchangerate-api.com/), a biblioteca maliciosa está contida no arquivo `lib_cotacao_moeda_sqn/__init__.py`.

O código malicioso dentro da biblioteca `lib_cotacao_moeda_sqn` coleta variáveis de ambiente filtradas por palavras-chave e as envia para um canal do Slack sem o conhecimento do usuário.
 
**O objetivo desta PoC é demonstrar a importância de garantir a segurança das bibliotecas utilizadas em projetos e estar ciente dos possíveis riscos de injeção de código malicioso.**

## Exemplo de evento válido esperado pela função Lambda.

A função Lambda `lambda_handler` espera receber um evento no formato a seguir:

```json
{
  "base_currency": "BRL"
}
```

- `base_currency`: A moeda base para a qual deseja-se obter a taxa de câmbio do dólar. Neste exemplo, estamos usando o Real Brasileiro (BRL).

## Exemplo de retorno da função Lambda.

A função Lambda `lambda_handler` retorna a avaliação do dolar no seguinte formato.

```json
{
  "statusCode": 200,
  "body": "{\"dollar_rate\": 4.9857}",
  "headers": {
    "Content-Type": "application/json"
  }
}
```

## Características do projeto

O projeto obtem a chave da [API do ExchangeRate](https://www.exchangerate-api.com/) por meio da variavel de ambiente **`EXCHANGE_RATE_API_KEY`**.

A estrutura de arquivos do projeto pode ser observadas abaixo.

```
dollar-rate-poc-secret-injection/
│
├── lib_cotacao_moeda_sqn/
│   ├── __init__.py
│
├── lambda_function.py
│
└── README.md
```

- `lib_cotacao_moeda_sqn/`: Diretório que contém a biblioteca maliciosa que simula uma biblioteca de cotação de moedas.
- `lib_cotacao_moeda_sqn/__init__.py`: Arquivo que contém o código malicioso e a implementação da função `avaliar_dollar`.
- `lambda_function.py`: Arquivo com a função principal (lambda handler) que utiliza a função `avaliar_dollar` para obter a taxa de câmbio do dólar para a moeda base informada.

## Diagrama do POC.

<p align="center">
  <img alt="Dollar-rate" src="https://i.imgur.com/4KsiFNG.png" title="Dollar-rate" width="75%">
</p>

  1 - A função handler executa a lib maliciosa para obter avaliação atualizada.

  2 - O código arbitrário carrega as variavei de ambiente.

  3 - O código arbitrário exfiltra os dados capturados.

  4 - A lib maliciosa autentica na API e obtem a avaliação atualizada.

---

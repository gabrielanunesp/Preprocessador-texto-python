# Projeto Prático: Pré-processador de Texto em Python

Este projeto é um exemplo prático de pré-processamento básico de textos usando Python, uma etapa fundamental para trabalhar com dados textuais em projetos de Inteligência Artificial, Machine Learning e análise de dados.

## Como o projeto funciona

O código realiza as seguintes operações em um texto de entrada:

1. **Remoção de URLs** — elimina links como `https://exemplo.com` para evitar ruído nos dados.  
2. **Remoção de pontuação** — retira caracteres especiais como vírgulas, pontos e exclamações.  
3. **Remoção de números** — elimina dígitos que podem atrapalhar análises específicas.  
4. **Conversão para minúsculas** — padroniza o texto para facilitar o processamento.  
5. **Remoção de espaços extras** — ajusta o espaçamento, deixando apenas um espaço entre as palavras.  
6. **Tokenização** — separa o texto em uma lista de palavras individuais (tokens).

## Autor

Gabriela Nunes  
Estudante de Engenharia de Software e entusiasta em Inteligência Artificial e Desenvolvimento.


## Exemplo de saída

```plaintext
Texto original:

Olá! Este é um exemplo de texto para pré-processamento. 
Visite https://exemplo.com para mais informações! O número é 1234.

Texto limpo:

olá este é um exemplo de texto para préprocessamento visite para mais informações o número é

Tokens:

['olá', 'este', 'é', 'um', 'exemplo', 'de', 'texto', 'para', 'préprocessamento', 'visite', 'para', 'mais', 'informações', 'o', 'número', 'é']

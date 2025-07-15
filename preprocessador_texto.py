import re
import string

def limpar_texto(texto):
    # Remove URLs
    texto = re.sub(r'http\S+', '', texto)
    # Remove pontuação
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    # Remove números
    texto = re.sub(r'\d+', '', texto)
    # Remove espaços extras e deixa tudo em minúsculo
    texto = texto.lower().strip()
    texto = re.sub(r'\s+', ' ', texto)
    return texto

def tokenizar(texto):
    # Divide o texto em palavras (tokens)
    return texto.split()

if __name__ == "__main__":
    texto_exemplo = """
    Olá! Este é um exemplo de texto para pré-processamento. 
    Visite https://exemplo.com para mais informações! O número é 1234.
    """

    print("Texto original:")
    print(texto_exemplo)

    texto_limpo = limpar_texto(texto_exemplo)
    print("\nTexto limpo:")
    print(texto_limpo)

    tokens = tokenizar(texto_limpo)
    print("\nTokens:")
    print(tokens)

import string
import secrets

# Aqui criamos o conjunto completo de caracteres que podem ser usados na senha.
# O módulo "string" já traz grupos prontos:
# - ascii_lowercase: letras minúsculas
# - ascii_uppercase: letras maiúsculas
# - digits: números de 0 a 9
# - punctuation: símbolos especiais
ALFABETO = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)

def gerar_senha(tamanho: int) -> str:
    """
    Gera uma senha aleatória com o tamanho especificado.

    Parâmetro:
        tamanho (int): Quantidade de caracteres da senha.

    Retorno:
        str: Uma string contendo a nova senha gerada.

    Observação:
        Usamos 'secrets.choice' porque ele é mais seguro para gerar senhas,
        diferente de 'random.choice', que não é recomendado para segurança.
    """
    return ''.join(secrets.choice(ALFABETO) for _ in range(tamanho))


# Este bloco garante que o código abaixo só será executado
# quando o arquivo for rodado diretamente (ex: python gerador.py)
# e não quando for importado por outro módulo.
if __name__ == "__main__":
    # Aqui apenas chamamos a função e mostramos uma senha de 12 caracteres.
    print(gerar_senha(12))

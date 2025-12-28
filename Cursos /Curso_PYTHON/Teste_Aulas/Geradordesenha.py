import secrets
import string

def gerar_senha(tamanho=450):
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser pelo menos 4")

    senha = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    alfabeto = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    senha += [secrets.choice(alfabeto) for _ in range(tamanho - 4)]
    secrets.SystemRandom().shuffle(senha)

    return ''.join(senha)

if __name__ == "__main__":
    print("Senha gerada:", gerar_senha())

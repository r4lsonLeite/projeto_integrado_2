import datetime

import user


class Diagnosis():
    def __init__(self, user: user, date_app: datetime, score_first: str, level: int, answers: str):
       
        self.user = user
        self.date_app = date_app
        self.score_first = score_first
        self.level = level
        self.answers
        
        # teste
if __name__ == "__main__":
    print("--- 1. Criando o Usuário ---")
    usuario = user("Ana Souza", "ana@email.com")
    print(f"Usuário criado: {usuario}")

    print("\n--- 2. Criando o Diagnóstico ---")
    # Simulando dados vindos de um formulário
    respostas_form = {"pergunta1": "sim", "pergunta2": "não", "dor": "frequente"}
    
    diag = Diagnosis(
        user=usuario,
        date_app=datetime.now(),
        score_first="85/100",
        level=4, # Nível alto
        answers=respostas_form
    )
    print("Diagnóstico gerado com sucesso.")

    print("\n--- 3. Verificando os Dados (Teste de Leitura) ---")
    # Aqui testamos a NAVEGAÇÃO entre objetos (Diagnosis -> User)
    print(f"Paciente: {diag.user.name}")  # Acessando atributo do objeto User dentro de Diagnosis
    print(f"Data: {diag.date_app}")
    print(f"Nível: {diag.level}")
    
    print("\n--- 4. Testando Lógica de Negócio ---")
    resultado = diag.verificar_risco()
    print(f"Resultado da análise: {resultado}")
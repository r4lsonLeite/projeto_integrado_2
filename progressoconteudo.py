from datetime import datetime

from user import User

class Progconteudo():
    def __init__ (self, prog: int, user: User, conteudo: str, status: bool, ultimoacesso: datetime, percentual:int ):
        self.prog = prog
        self.user = user
        self.conteudo = conteudo    
        self.status = status
        self.ultimoacesso = ultimoacesso
        self.percentual = percentual
        
        
from datetime import datetime
from user import User
from progressoconteudo import Progconteudo

# 1. Primeiro você precisa ter um User criado
# (Preencha com os dados que sua classe User pede)
usuario_teste = User(id=1, nome="Carlos", email="carlos@teste.com") 

# 2. Pegar a data e hora de agora
agora = datetime.now()

# 3. Criar o Progresso ligando tudo
novo_progresso = Progconteudo(
    prog=101,
    user=usuario_teste,      # Passa o objeto usuário inteiro aqui
    conteudo="Aula de Python",
    status=True,
    ultimoacesso=agora,      # Passa a data gerada acima
    percentual=25
)

print(f"O usuário {novo_progresso.user.nome} completou {novo_progresso.percentual}%")
class Conteudo():
    
    def __init__(self, titulo, descricao, categoria, url, carga_horaria, visibilidade):
        self.titulo = titulo 
        self.descrição = descricao 
        self.categoria = categoria
        self.url = url 
        self.carga_horaria = carga_horaria
        self.visibilidade = visibilidade
        
        
        # Criando uma instância (um objeto) da classe Conteudo
meu_curso = Conteudo(
    titulo="Fundamentos",
    descricao="Curso introdutório",
    categoria="vendas",
    url="https://www.google.com/",
    carga_horaria=40,
    visibilidade="Publico"
)

# Acessando os dados
print(f"Curso: {meu_curso.titulo}")
print(f"Carga Horária: {meu_curso.carga_horaria} horas")
# Empreenda Mais Elas — Plataforma de Apoio ao Empreendedorismo Feminino

> **Protótipo de Alta Fidelidade & Estrutura de Classes MVP** > Disciplina: Design de Interfaces e Experiência de Usuário / Projeto Integrado III [ADS0038]  
> Professor: Luís Fabrício de Freitas Souza (fabricio.freitas@ufca.edu.br)  
> Polo: Lavras da Mangabeira — UFCA  

---

## 📋 Contextualização do Projeto

### Qual é o problema que a solução resolve?
O projeto enfrenta barreiras críticas que impedem o crescimento e a sustentabilidade de micro-negócios liderados por mulheres, especialmente no cenário regional e informal. Essas barreiras incluem a falta de inclusão digital, a ausência de capacitação em gestão e finanças de forma acessível, e o isolamento comercial que dificulta a conexão com parceiros estratégicos e novos canais de venda.

### Qual é o objetivo do sistema?
O objetivo principal é ampliar o potencial do empreendedorismo feminino local. A plataforma atua reduzindo as barreiras de entrada no mercado por meio de conteúdos educacionais acessíveis, linguagem clara e acolhedora, suporte contínuo, mentorias especializadas e uma vitrine digital para escoamento da produção, unificando todo o ecossistema de apoio em um ambiente integrado.

### Como o sistema funciona (Visão Geral)?
O fluxo do sistema foi desenhado para acompanhar a jornada da empreendedora desde o primeiro acesso:
1. **Cadastro e Login Simples:** Entrada rápida e descomplicada no ecossistema.
2. **Diagnóstico de Perfil:** Um questionário dinâmico mapeia o estágio atual do negócio (se na Fase de Ideia ou com Negócio Ativo).
3. **Trilhas Personalizadas:** O sistema gera automaticamente uma rota de aprendizado baseada no diagnóstico (ex: *Alfabetização Digital* para iniciantes ou *Cursos Avançados* para aceleração).
4. **Mentorias e Rede de Conexão:** Espaço para agendamento e realização de encontros individuais com especialistas (como voluntários do SEBRAE e instituições parceiras).
5. **Marketplace Comunitário:** Uma vitrine onde as usuárias podem expor, anunciar e vender seus produtos ou serviços diretamente aos consumidores.
6. **Painéis Gerenciais:** Interfaces para controle de métricas das empreendedoras e monitoramento global de impacto social para os administradores.

---

## 🎨 Design de Interfaces & Decisões de Desenvolvimento

O protótipo de alta fidelidade desenvolvido no Figma foi estruturado sobre os pilares fundamentais da Experiência do Usuário (UX), priorizando a usabilidade, acessibilidade e redução da carga cognitiva.

### Identidade Visual e Psicologia das Cores
* **Primary (Vermelho Terracota — `#AB332A`):** Utilizada estritamente em botões de ação principal (*Call to Action*), links ativos e estados selecionados. Garante foco visual e induz o avanço da usuária no fluxo sem poluição gráfica.
* **Secondary (Marrom Suave — `#58413E`):** Tonalidade orgânica aplicada a textos de apoio, descrições e ícones secundários, gerando um ambiente visual acolhedor e menos agressivo que o cinza convencional.
* **Text Dark (Quase Preto — `#191C1D`):** Usada em todos os títulos para garantir contraste máximo e leitura limpa.
* **Brand Highlight (Roxo — `#7A4C8F`):** Utilizada para tags de status importantes (ex: mentoria confirmada) e elementos do rodapé, criando pontos de diferenciação elegantes na interface.

### Tipografia e Hierarquia Visual
* **Títulos Grandes e Médios:** Utilizam a fonte serifada **Playfair Display (Bold, 32px e 22px)**. A escolha confere autoridade, elegância e demarcação estrutural nítida entre as seções das páginas.
* **Corpo, Rótulos e Inputs:** Utilizam a fonte sem serifa **Plus Jakarta Sans (Regular/SemiBold, 14px e 16px)**. Projetada especificamente para alta legibilidade em ambientes digitais, facilitando a absorção das informações por usuárias de todos os níveis de alfabetização tecnológica.

### Práticas de UX Aplicadas no Figma
* **Componentização e Auto Layout:** Toda a interface utiliza propriedades avançadas de Auto Layout (simulando o comportamento de caixas do CSS Flexbox), garantindo paddings e espaçamentos consistentes de `12px` e `24px`.
* **Inputs Estilo Radio Cards:** Na tela de Diagnóstico, as opções são botões horizontais amplos e fáceis de clicar (com feedback visual de borda ativada de `2px` em `#AB332A`), otimizando a experiência em dispositivos móveis.
* **Redução de Fricção:** O Dashboard organiza dados complexos de vendas, progresso de cursos e reuniões em cards resumidos e diretos na primeira tela, evitando cliques desnecessários.

---

## 🌍 [Componente Extensionista] Importância da Experiência do Usuário (UX)

Um bom design de interface vai muito além da estética: ele dita o sucesso ou o fracasso de um sistema de software quando inserido na sociedade. No ecossistema de soluções reais, sistemas excessivamente técnicos, poluídos e confusos acabam excluindo justamente as pessoas que mais necessitam da tecnologia, gerando frustração e abandono da ferramenta.

Para a plataforma **Empreenda Mais Elas**, aplicar os princípios de UX e acessibilidade significa construir uma ponte de inclusão. Ao desenhar uma interface com tipografia legível, fluxo sem fricção e cores com alto contraste, reduzimos o medo da tecnologia que muitas mulheres micro-empreendedoras enfrentam ao tentar digitalizar seus negócios. Uma boa experiência transforma uma ferramenta complexa de gerenciamento em um ambiente amigável e acolhedor. Quando o software respeita o tempo, a clareza visual e as necessidades reais do usuário final, a curva de adoção cresce, promovendo autonomia econômica, dignidade e impacto social palpável dentro das comunidades atendidas.

---

## 🛠️ Tecnologias Utilizadas

* **Design de Interface (Figma):** Prototipagem de alta fidelidade das jornadas de Dashboard, Diagnóstico, Trilhas, Mentorias, Marketplace, Painel Comercial e Painel Administrativo.
* **Backend & Modelagem (Python):** Estrutura de classes isoladas para o Modelo de Visão Mínima (MVP).
* **Ferramentas de Engenharia:** Visual Studio Code (IDE), Discord (Comunicação Síncrona do Time) e GitHub (Controle de Versão e Repositório).

---

## 🧩 Classes Principais Implementadas (MVP)

Cada classe foca em uma responsabilidade simples e usa métodos curtos para manipular seu estado de forma modular (uma classe por arquivo):

* `AgendaMentora` (`agendamentora.py`): Controla disponibilidade da mentora (`reservar`, `liberar`) e mantém vínculo com usuário e data/hora.
* `Mentoria` (`mentoria.py`): Ciclo de vida de uma sessão (`iniciar`, `concluir`, `cancelar`) baseado no agendamento aprovado.
* `AvaliacaoMentoria` (`avaliacaomentoria.py`): Guarda nota/comentário e permite ajustes com `atualizar_nota`.
* `Produto` (`produto.py`): Representa oferta cadastrada pela usuária e permite `aplicar_desconto` e mudança de status.
* `Anuncio` (`anuncio.py`): Publicação de um produto, com `publicar` e `pausar` para controlar exposição na vitrine.
* `Pedido` (`pedido.py`): Agrega itens, atualiza total automaticamente com `adicionar_item`/`recalcular_total` e rastreia status.
* `ItemPedido` (`itempedido.py`): Detalhe de item do pedido e cálculo de total por item (`calcular_total`).
* `User` (`user.py`) e `Address` (`adress.py`): Cadastro de usuário e endereço, com `check_password`, `__str__` e `to_dict` para depuração.
* `Invoice`/`Payment` (`invoice.py`, `payment.py`): Geração de cobrança e confirmação de pagamento integradas.
* `Partner`/`PartnerOffer` (`partner.py`, `partneroffer.py`): Parceiros institucionais podem publicar serviços e gerenciar ofertas.
* `Notification` (`notification.py`): Envio de alertas de status com controle de entrega.
* `EventMetric` (`eventmetric.py`): Registro de interações e eventos para alimentar as métricas do sistema.
* `Conteudo`, `Diagnosis`, `Progconteudo`, `Trilha`, `Trilhaitem`: Suporte à modelagem de dados educacionais, diagnóstico inicial e estrutura de trilhas de conhecimento.

---

## 🚀 Como Executar e Testar a Aplicação

### Visualizando o Protótipo no Figma
O link completo contendo o mapa de telas, fluxogramas de alta fidelidade e interações pode ser acessado em:  
👉 `https://www.figma.com/design/TsSz5tbHcWjJsypyS8JXYW/Empreenda--Elas?node-id=0-1&t=FBjxLNrLPSOWI8MQ-1`

### Executando os Testes de Classes Locais
Para testar rapidamente os comportamentos, validações e a serialização `to_dict` das entidades principais do MVP, abra um terminal na raiz do projeto e execute o comando Python abaixo:

```bash
python - <<'PY'
from pedido import Pedido
from itempedido import ItemPedido

pedido = Pedido(pedido_id=1, usuario_id=10, endereco_entrega='Rua A, 123')
item = ItemPedido(item_id=1, pedido_id=None, produto_id=7, quantidade=2, preco_unitario=50)
pedido.adicionar_item(item)
print("Valor Total Calculado pelo MVP:", pedido.valor_total)
print("Dicionário Serializado para API (to_dict):")
print(pedido.to_dict())
PY

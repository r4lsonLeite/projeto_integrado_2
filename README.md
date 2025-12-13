# Projeto integrado 2

## Visão geral (MVP EP1)

Implementação das classes principais pedidas no Entregável Parcial 1: `AgendaMentora`, `Mentoria`, `AvaliacaoMentoria`, `Produto`, `Anuncio`, `Pedido` e `ItemPedido`. Cada classe foca em uma responsabilidade simples e usa métodos curtos para manipular seu estado.

## Classes principais (EP1)

- `AgendaMentora` (`agendamentora.py`): controla disponibilidade da mentora (`reservar`, `liberar`) e mantém vínculo com usuário e data/hora.
- `Mentoria` (`mentoria.py`): ciclo de vida de uma sessão (`iniciar`, `concluir`, `cancelar`) baseado no agendamento aprovado.
- `AvaliacaoMentoria` (`avaliacaomentoria.py`): guarda nota/comentário e permite ajustes com `atualizar_nota`.
- `Produto` (`produto.py`): representa oferta cadastrada pelo usuário e permite `aplicar_desconto` e mudança de status.
- `Anuncio` (`anuncio.py`): publicação de um produto, com `publicar` e `pausar` para controlar exposição.
- `Pedido` (`pedido.py`): agrega itens, atualiza total automaticamente com `adicionar_item`/`recalcular_total` e rastreia status.
- `ItemPedido` (`itempedido.py`): detalhe de item do pedido e cálculo de total por item (`calcular_total`).
- `User` (`user.py`) e `Address` (`adress.py`): cadastro de usuário e endereço, com `check_password`, `__str__` e `to_dict` para depuração.
- `Invoice`/`Payment` (`invoice.py`, `payment.py`): geração de cobrança e confirmação de pagamento integradas.
- `Partner`/`PartnerOffer` (`partner.py`, `partneroffer.py`): parceiros podem publicar serviços e ativar/desativar ofertas.
- `Notification` (`notification.py`): envio simples com controle de status.
- `EventMetric` (`eventmetric.py`): registro de evento para métricas.
- `Conteudo`, `Diagnosis`, `Progconteudo`, `Trilha`, `Trilhaitem`: suporte a conteúdos, diagnóstico inicial, progresso e organização de trilhas.

## Processos e escolhas de software

- Orientação a objetos simples: cada classe encapsula atributos do diagrama e expõe poucos métodos coesos.
- Métodos `to_dict` para facilitar serialização/depuração rápida durante o MVP.
- Validações leves: checagem de disponibilidade (agenda), estados do ciclo de vida (mentoria/pedido/anúncio) e faixas de desconto (produto).
- Estrutura modular: uma classe por arquivo para manter o código fácil de localizar e estender nas próximas entregas.


## Possíveis usos da nossa solução

Imaginamos a plataforma como um hub de mentoria e produtos educacionais para mulheres. Exemplos de aplicação no mundo real:

- Pequenas consultorias podem cadastrar mentorias, publicar anúncios e receber pedidos em um fluxo único.
- Mentores independentes controlam agenda e avaliações para construir reputação e organizar horários.
- Lojas de cursos ou materiais digitais aplicam descontos, geram anúncios e montam pedidos rapidamente, com métricas futuras para entender engajamento.

## Como testar rapidamente

Abra um shell na raiz do projeto e instancie as classes em Python para verificar os métodos principais, por exemplo:

```bash
python - <<'PY'
from pedido import Pedido
from itempedido import ItemPedido

pedido = Pedido(pedido_id=1, usuario_id=10, endereco_entrega='Rua A, 123')
item = ItemPedido(item_id=1, pedido_id=None, produto_id=7, quantidade=2, preco_unitario=50)
pedido.adicionar_item(item)
print(pedido.valor_total)
print(pedido.to_dict())
PY
```

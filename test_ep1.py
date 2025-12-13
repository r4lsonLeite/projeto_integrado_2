from agendamentora import AgendaMentora
from mentoria import Mentoria
from avaliacaomentoria import AvaliacaoMentoria
from produto import Produto
from anuncio import Anuncio
from pedido import Pedido
from itempedido import ItemPedido


def run_basic_assertions() -> None:
    agenda = AgendaMentora(agenda_id=1, mentora_id=10, data_hora="2025-12-12T10:00:00")
    assert agenda.disponivel is True
    assert agenda.reservar(usuario_id=20) is True
    assert agenda.disponivel is False
    assert agenda.liberar() is True
    print("AgendaMentora: reserva e liberação ok")

    mentoria = Mentoria(mentoria_id=1, agendamento_id=agenda.agenda_id)
    assert mentoria.iniciar() is True
    assert mentoria.status == 'em_andamento'
    assert mentoria.concluir() is True
    assert mentoria.status == 'concluida'
    print("Mentoria: iniciar e concluir ok")

    avaliacao = AvaliacaoMentoria(avaliacao_id=1, mentoria_id=mentoria.mentoria_id, nota=4.5, comentario="Boa")
    assert avaliacao.nota == 4.5
    assert avaliacao.atualizar_nota(5.0, "Excelente") is True
    assert avaliacao.nota == 5.0
    print("AvaliacaoMentoria: atualização de nota ok")

    produto = Produto(produto_id=1, usuario_id=30, titulo="Curso", descricao="Python", valor=100.0, categoria="curso")
    assert produto.aplicar_desconto(10) is True
    assert round(produto.valor, 2) == 90.0
    print("Produto: desconto aplicado ok")

    anuncio = Anuncio(anuncio_id=1, produto_id=produto.produto_id)
    assert anuncio.publicar(data_publicacao="2025-12-12") is True
    assert anuncio.status_anuncio == 'publicado'
    assert anuncio.pausar() is True
    print("Anuncio: publicar e pausar ok")

    pedido = Pedido(pedido_id=1, usuario_id=40, endereco_entrega="Rua A, 123")
    item = ItemPedido(item_id=1, pedido_id=None, produto_id=produto.produto_id, quantidade=2, preco_unitario=45.0)
    assert pedido.adicionar_item(item) is True
    assert round(pedido.valor_total, 2) == 90.0
    assert pedido.to_dict()['itens'][0]['total'] == 90.0
    print("Pedido/ItemPedido: cálculo e serialização ok")


if __name__ == "__main__":
    run_basic_assertions()
    print("Todos os testes básicos do passaram.")

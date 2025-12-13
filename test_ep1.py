from agendamentora import AgendaMentora
from mentoria import Mentoria
from avaliacaomentoria import AvaliacaoMentoria
from produto import Produto
from anuncio import Anuncio
from pedido import Pedido
from itempedido import ItemPedido
from projeto_integrado_2.adress import Address
from projeto_integrado_2.conteudo import Conteudo
from projeto_integrado_2.diagnosis import Diagnosis
from projeto_integrado_2.eventmetric import EventMetric
from projeto_integrado_2.invoice import Invoice
from projeto_integrado_2.notification import Notification
from projeto_integrado_2.partner import Partner
from projeto_integrado_2.partneroffer import PartnerOffer
from projeto_integrado_2.payment import Payment
from projeto_integrado_2.progressoconteudo import Progconteudo
from projeto_integrado_2.trilha import Trilha
from projeto_integrado_2.trilhaItem import Trilhaitem
from projeto_integrado_2.user import User


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

    user = User(name='Ana', adress='Rua B', phone=119999999, email='ana@test.com', date_register='2025-01-01', password='123', status=True)
    assert user.check_password('123') is True
    assert user.check_password('321') is False

    addr = Address(user=user, street='Rua B', city='Sao Paulo', country='BR', zip_code=12345)
    assert 'Sao Paulo' in str(addr)
    assert addr.to_dict()['country'] == 'BR'

    invoice = Invoice(invoice_id=1, order_id=9, amount=100.0, due_date='2025-12-31', client_id=7, status='pending', issue_date='2025-12-01')
    assert invoice.generate_charge() is True
    assert invoice.status == 'awaiting_payment'

    payment = Payment(payment_id=1, invoice_id=invoice.invoice_id, amount=100.0, gateway_type='pix', transaction_gateway='abc', status='pending', payment_date=None)
    assert payment.process_and_confirm(confirmation_date='2025-12-02', invoice_object=invoice) is True
    assert payment.status == 'confirmed'
    assert invoice.status == 'paid'

    partner = Partner(partner_id=1, name='Org X', partner_type='school', contact='contato')
    assert partner.publish_service('Mentoria', 'Descricao') is True

    offer = PartnerOffer(offer_id=1, partner_id=partner.partner_id, title='Bolsa', description='Desc', criteria_json='{}', enrollment_url='http://test.com')
    assert offer.is_active is True
    assert offer.toggle_activation() is False
    assert offer.toggle_activation() is True

    notification = Notification(notification_id=1, user_id=user.name, channel='email', content='Olá', send_date='2025-12-01', send_status='pending')
    assert notification.send_notification() is True

    event = EventMetric(event_id=1, user_id=1, event_type='login', reference_id='abc', event_date='2025-12-12')
    assert event.record_event() is True

    conteudo = Conteudo(titulo='Curso', descricao='Intro', categoria='edu', url='http://conteudo', carga_horaria=10)
    assert conteudo.to_dict()['titulo'] == 'Curso'

    diag = Diagnosis(user=user, date_app='2025-12-12', score_first=8.5, level='avancado', answers=['a'])
    assert 'score' in diag.resumo()

    prog = Progconteudo(user=user, conteudo=conteudo, status='em_andamento', ultimoacesso='2025-12-12', percentual=10)
    assert prog.marcar_progresso(50) is True
    assert prog.percentual == 50

    trilha = Trilha(user=user, tipo='aprendizado', status='ativa', date_creat='2025-12-01')
    assert trilha.atualizar_status('concluida') is True
    assert trilha.status == 'concluida'

    trilhaitem = Trilhaitem(trilha=trilha, conteudo=conteudo, ordem=1, obrigatorio=True)
    assert trilhaitem.ordem == 1
    
if __name__ == "__main__":
    run_basic_assertions()
    print("Todos os testes básicos do passaram.")

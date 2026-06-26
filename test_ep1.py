from app import create_app
from app.models.agenda import AgendaMentora
from app.models.apoio import Address, EventMetric, Notification
from app.models.avaliacao import AvaliacaoMentoria
from app.models.diagnostico import Diagnostico
from app.models.financeiro import Invoice, Payment
from app.models.marketplace import Anuncio
from app.models.parcerias import Partner, PartnerOffer
from app.models.pedido import ItemPedido, Pedido
from app.models.produto import Produto
from app.models.progresso import ProgressoConteudo
from app.models.trilha import Conteudo, Trilha, TrilhaItem
from app.models.user import User
from app.models.mentoria import Mentoria


def run_basic_assertions() -> None:
    app = create_app()
    assert app is not None

    agenda = AgendaMentora(agenda_id=1, mentora_id=10, data_hora="2025-12-12T10:00:00")
    assert agenda.disponivel is True
    assert agenda.reservar(usuario_id=20) is True
    assert agenda.disponivel is False
    assert agenda.liberar() is True
    print("AgendaMentora: reserva e liberação ok")

    mentoria = Mentoria(usuario_id=20, mentora="Mentora A", data_hora="2025-12-12T10:00:00", tema="Vendas", mentoria_id=1)
    mentoria.atualizar_status('concluida')
    assert mentoria.status == 'concluida'
    print("Mentoria: atualização de status ok")

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
    item = ItemPedido(produto_id=produto.produto_id, quantidade=2, preco_unitario=45.0)
    pedido.adicionar_item(item)
    assert round(pedido.valor_total, 2) == 90.0
    assert pedido.to_dict()['itens'][0]['total'] == 90.0
    print("Pedido/ItemPedido: cálculo e serialização ok")

    user = User(nome='Ana', email='ana@test.com', senha_hash='pbkdf2:sha256:1000000$teste$98c5d6d7f8940a4f16f0d9c58a1f4e11c7bd6340732f641663a5540c2fdd03f0', telefone='119999999', endereco='Rua B', user_id=1)
    user.senha_hash = __import__('werkzeug.security').security.generate_password_hash('123')
    assert user.check_password('123') is True
    assert user.check_password('321') is False

    addr = Address(user_id=user.user_id, street='Rua B', city='Sao Paulo', country='BR', zip_code='12345')
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

    notification = Notification(notification_id=1, user_id=user.user_id, channel='email', content='Olá', send_date='2025-12-01', send_status='pending')
    assert notification.send_notification() is True

    event = EventMetric(event_id=1, user_id=1, event_type='login', reference_id='abc', event_date='2025-12-12')
    assert event.record_event() is True

    conteudo = Conteudo(conteudo_id=1, titulo='Curso', descricao='Intro', categoria='edu', url='http://conteudo', carga_horaria=10)
    assert conteudo.to_dict()['titulo'] == 'Curso'

    diag = Diagnostico(user_id=user.user_id, date_app='2025-12-12', score_first=8.5, level='avancado', answers=['a'])
    assert 'score' in diag.resumo()

    prog = ProgressoConteudo(user_id=user.user_id, conteudo_id=conteudo.conteudo_id, status='em_andamento', percentual=10, ultimo_acesso='2025-12-12')
    assert prog.marcar_progresso(50) is True
    assert prog.percentual == 50

    trilha = Trilha(usuario_id=user.user_id, tipo='aprendizado', status='ativa', trilha_id=1, criado_em='2025-12-01')
    trilha.status = 'concluida'
    assert trilha.status == 'concluida'

    trilhaitem = TrilhaItem(conteudo=conteudo, ordem=1, obrigatorio=True)
    trilha.adicionar_item(trilhaitem)
    assert trilha.itens[0].ordem == 1
    
if __name__ == "__main__":
    run_basic_assertions()
    print("Todos os testes básicos do passaram.")

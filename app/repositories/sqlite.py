from app.extensions import db
from app.models.agenda import AgendaMentora
from app.models.apoio import Address, EventMetric, Notification
from app.models.avaliacao import AvaliacaoMentoria
from app.models.diagnostico import Diagnostico
from app.models.financeiro import Invoice, Payment
from app.models.marketplace import Anuncio
from app.models.mentoria import Mentoria
from app.models.parcerias import Partner, PartnerOffer
from app.models.pedido import ItemPedido, Pedido
from app.models.produto import Produto
from app.models.progresso import ProgressoConteudo
from app.models.trilha import Conteudo, Trilha, TrilhaItem
from app.models.user import User
from app.persistence_models import AddressModel, AnnouncementModel, ContentModel, ContentProgressModel, DiagnosisModel, EventMetricModel, InvoiceModel, MentorAgendaModel, MentoriaModel, MentoriaReviewModel, NotificationModel, OrderItemModel, OrderModel, PartnerModel, PartnerOfferModel, PaymentModel, ProductModel, TrailItemModel, TrailModel, UserModel


class UserRepository:
    def create(self, user: User) -> User:
        row = UserModel(nome=user.nome, email=user.email, senha_hash=user.senha_hash, telefone=user.telefone, endereco=user.endereco, papel=user.papel, ativo=user.ativo, criado_em=user.criado_em)
        db.session.add(row)
        db.session.commit()
        user.user_id = row.id
        return user

    def list_all(self) -> list[User]:
        return [self._to_domain(row) for row in UserModel.query.order_by(UserModel.id).all()]

    def get_by_id(self, entity_id: int) -> User | None:
        row = db.session.get(UserModel, entity_id)
        return self._to_domain(row) if row else None

    def get_by_email(self, email: str) -> User | None:
        row = UserModel.query.filter_by(email=email).first()
        return self._to_domain(row) if row else None

    @staticmethod
    def _to_domain(row: UserModel) -> User:
        return User(nome=row.nome, email=row.email, senha_hash=row.senha_hash, telefone=row.telefone, endereco=row.endereco, papel=row.papel, ativo=row.ativo, user_id=row.id, criado_em=row.criado_em)


class ProductRepository:
    def create(self, product: Produto) -> Produto:
        row = ProductModel(usuario_id=product.usuario_id, titulo=product.titulo, descricao=product.descricao, valor=product.valor, categoria=product.categoria, status=product.status)
        db.session.add(row)
        db.session.commit()
        product.produto_id = row.id
        return product

    def list_all(self) -> list[Produto]:
        return [self._to_domain(row) for row in ProductModel.query.order_by(ProductModel.id).all()]

    def get_by_id(self, entity_id: int) -> Produto | None:
        row = db.session.get(ProductModel, entity_id)
        return self._to_domain(row) if row else None

    @staticmethod
    def _to_domain(row: ProductModel) -> Produto:
        return Produto(usuario_id=row.usuario_id, titulo=row.titulo, descricao=row.descricao, valor=row.valor, categoria=row.categoria, status=row.status, produto_id=row.id)


class OrderRepository:
    def create(self, order: Pedido) -> Pedido:
        row = OrderModel(usuario_id=order.usuario_id, endereco_entrega=order.endereco_entrega, status=order.status, data_criacao=order.data_criacao, valor_total=order.valor_total)
        db.session.add(row)
        db.session.flush()
        for item in order.itens:
            db.session.add(OrderItemModel(pedido_id=row.id, produto_id=item.produto_id, quantidade=item.quantidade, preco_unitario=item.preco_unitario))
        db.session.commit()
        order.pedido_id = row.id
        return order

    def list_all(self) -> list[Pedido]:
        return [self._to_domain(row) for row in OrderModel.query.order_by(OrderModel.id).all()]

    def get_by_id(self, entity_id: int) -> Pedido | None:
        row = db.session.get(OrderModel, entity_id)
        return self._to_domain(row) if row else None

    @staticmethod
    def _to_domain(row: OrderModel) -> Pedido:
        itens = [ItemPedido(produto_id=item.produto_id, quantidade=item.quantidade, preco_unitario=item.preco_unitario) for item in row.itens]
        return Pedido(usuario_id=row.usuario_id, endereco_entrega=row.endereco_entrega, status=row.status, pedido_id=row.id, data_criacao=row.data_criacao, itens=itens, valor_total=row.valor_total)


class MentoriaRepository:
    def create(self, mentoria: Mentoria) -> Mentoria:
        row = MentoriaModel(usuario_id=mentoria.usuario_id, mentora=mentoria.mentora, data_hora=mentoria.data_hora, tema=mentoria.tema, observacoes=mentoria.observacoes, status=mentoria.status, criado_em=mentoria.criado_em)
        db.session.add(row)
        db.session.commit()
        mentoria.mentoria_id = row.id
        return mentoria

    def list_all(self) -> list[Mentoria]:
        return [self._to_domain(row) for row in MentoriaModel.query.order_by(MentoriaModel.id).all()]

    def get_by_id(self, entity_id: int) -> Mentoria | None:
        row = db.session.get(MentoriaModel, entity_id)
        return self._to_domain(row) if row else None

    @staticmethod
    def _to_domain(row: MentoriaModel) -> Mentoria:
        return Mentoria(usuario_id=row.usuario_id, mentora=row.mentora, data_hora=row.data_hora, tema=row.tema, observacoes=row.observacoes, status=row.status, mentoria_id=row.id, criado_em=row.criado_em)


class ConteudoRepository:
    def seed_defaults(self) -> None:
        if ContentModel.query.count() > 0:
            return
        db.session.add_all([
            ContentModel(id=1, titulo="Alfabetização Digital", descricao="Primeiros passos no digital", categoria="formacao", url="https://exemplo.com/alfabetizacao", carga_horaria=8),
            ContentModel(id=2, titulo="Precificação", descricao="Como precificar produtos e serviços", categoria="gestao", url="https://exemplo.com/precificacao", carga_horaria=6),
            ContentModel(id=3, titulo="Marketing para Redes Sociais", descricao="Estratégias básicas de divulgação", categoria="marketing", url="https://exemplo.com/marketing", carga_horaria=10),
        ])
        db.session.commit()

    def list_all(self) -> list[Conteudo]:
        return [self._to_domain(row) for row in ContentModel.query.order_by(ContentModel.id).all()]

    def get_by_id(self, conteudo_id: int) -> Conteudo | None:
        row = db.session.get(ContentModel, conteudo_id)
        return self._to_domain(row) if row else None

    @staticmethod
    def _to_domain(row: ContentModel) -> Conteudo:
        return Conteudo(conteudo_id=row.id, titulo=row.titulo, descricao=row.descricao, categoria=row.categoria, url=row.url, carga_horaria=row.carga_horaria)


class TrilhaRepository:
    def create(self, trilha: Trilha) -> Trilha:
        row = TrailModel(usuario_id=trilha.usuario_id, tipo=trilha.tipo, status=trilha.status, criado_em=trilha.criado_em)
        db.session.add(row)
        db.session.flush()
        for item in trilha.itens:
            db.session.add(TrailItemModel(trilha_id=row.id, conteudo_id=item.conteudo.conteudo_id, ordem=item.ordem, obrigatorio=item.obrigatorio))
        db.session.commit()
        trilha.trilha_id = row.id
        return trilha

    def list_all(self) -> list[Trilha]:
        return [self._to_domain(row) for row in TrailModel.query.order_by(TrailModel.id).all()]

    def get_by_id(self, entity_id: int) -> Trilha | None:
        row = db.session.get(TrailModel, entity_id)
        return self._to_domain(row) if row else None

    @staticmethod
    def _to_domain(row: TrailModel) -> Trilha:
        itens = [TrilhaItem(ordem=item.ordem, obrigatorio=item.obrigatorio, conteudo=ConteudoRepository._to_domain(item.conteudo)) for item in sorted(row.itens, key=lambda current_item: current_item.ordem)]
        return Trilha(usuario_id=row.usuario_id, tipo=row.tipo, status=row.status, trilha_id=row.id, criado_em=row.criado_em, itens=itens)


class AnnouncementRepository:
    def create(self, anuncio: Anuncio) -> Anuncio:
        row = AnnouncementModel(produto_id=anuncio.produto_id, status_anuncio=anuncio.status_anuncio, data_publicacao=anuncio.data_publicacao)
        db.session.add(row)
        db.session.commit()
        anuncio.anuncio_id = row.id
        return anuncio

    def list_all(self) -> list[Anuncio]:
        return [Anuncio(produto_id=row.produto_id, status_anuncio=row.status_anuncio, data_publicacao=row.data_publicacao, anuncio_id=row.id) for row in AnnouncementModel.query.order_by(AnnouncementModel.id).all()]

    def get_by_id(self, entity_id: int) -> Anuncio | None:
        row = db.session.get(AnnouncementModel, entity_id)
        return Anuncio(produto_id=row.produto_id, status_anuncio=row.status_anuncio, data_publicacao=row.data_publicacao, anuncio_id=row.id) if row else None

    def update(self, anuncio_id: int, updates: dict) -> Anuncio | None:
        row = db.session.get(AnnouncementModel, anuncio_id)
        if not row:
            return None
        if 'status_anuncio' in updates:
            row.status_anuncio = updates['status_anuncio']
        if 'data_publicacao' in updates:
            row.data_publicacao = updates['data_publicacao']
        db.session.commit()
        return Anuncio(produto_id=row.produto_id, status_anuncio=row.status_anuncio, data_publicacao=row.data_publicacao, anuncio_id=row.id)

    def delete(self, anuncio_id: int) -> bool:
        row = db.session.get(AnnouncementModel, anuncio_id)
        if not row:
            return False
        db.session.delete(row)
        db.session.commit()
        return True


class MentorAgendaRepository:
    def create(self, agenda: AgendaMentora) -> AgendaMentora:
        row = MentorAgendaModel(mentora_id=agenda.mentora_id, data_hora=agenda.data_hora, usuario_id=agenda.usuario_id, disponivel=agenda.disponivel)
        db.session.add(row)
        db.session.commit()
        agenda.agenda_id = row.id
        return agenda

    def list_all(self) -> list[AgendaMentora]:
        return [AgendaMentora(mentora_id=row.mentora_id, data_hora=row.data_hora, usuario_id=row.usuario_id, disponivel=row.disponivel, agenda_id=row.id) for row in MentorAgendaModel.query.order_by(MentorAgendaModel.id).all()]

    def get_by_id(self, entity_id: int) -> AgendaMentora | None:
        row = db.session.get(MentorAgendaModel, entity_id)
        return AgendaMentora(mentora_id=row.mentora_id, data_hora=row.data_hora, usuario_id=row.usuario_id, disponivel=row.disponivel, agenda_id=row.id) if row else None


class MentoriaReviewRepository:
    def create(self, avaliacao: AvaliacaoMentoria) -> AvaliacaoMentoria:
        row = MentoriaReviewModel(mentoria_id=avaliacao.mentoria_id, nota=avaliacao.nota, comentario=avaliacao.comentario, data_avaliacao=avaliacao.data_avaliacao)
        db.session.add(row)
        db.session.commit()
        avaliacao.avaliacao_id = row.id
        return avaliacao

    def list_all(self) -> list[AvaliacaoMentoria]:
        return [AvaliacaoMentoria(mentoria_id=row.mentoria_id, nota=row.nota, comentario=row.comentario, data_avaliacao=row.data_avaliacao, avaliacao_id=row.id) for row in MentoriaReviewModel.query.order_by(MentoriaReviewModel.id).all()]

    def get_by_id(self, entity_id: int) -> AvaliacaoMentoria | None:
        row = db.session.get(MentoriaReviewModel, entity_id)
        return AvaliacaoMentoria(mentoria_id=row.mentoria_id, nota=row.nota, comentario=row.comentario, data_avaliacao=row.data_avaliacao, avaliacao_id=row.id) if row else None


class AddressRepository:
    def create(self, address: Address) -> Address:
        row = AddressModel(user_id=address.user_id, street=address.street, city=address.city, country=address.country, zip_code=address.zip_code)
        db.session.add(row)
        db.session.commit()
        address.address_id = row.id
        return address

    def list_all(self) -> list[Address]:
        return [Address(user_id=row.user_id, street=row.street, city=row.city, country=row.country, zip_code=row.zip_code, address_id=row.id) for row in AddressModel.query.order_by(AddressModel.id).all()]

    def get_by_id(self, entity_id: int) -> Address | None:
        row = db.session.get(AddressModel, entity_id)
        return Address(user_id=row.user_id, street=row.street, city=row.city, country=row.country, zip_code=row.zip_code, address_id=row.id) if row else None


class EventMetricRepository:
    def create(self, metric: EventMetric) -> EventMetric:
        row = EventMetricModel(user_id=metric.user_id, event_type=metric.event_type, reference_id=metric.reference_id, event_date=metric.event_date)
        db.session.add(row)
        db.session.commit()
        metric.event_id = row.id
        return metric

    def list_all(self) -> list[EventMetric]:
        return [EventMetric(user_id=row.user_id, event_type=row.event_type, reference_id=row.reference_id, event_date=row.event_date, event_id=row.id) for row in EventMetricModel.query.order_by(EventMetricModel.id).all()]

    def get_by_id(self, entity_id: int) -> EventMetric | None:
        row = db.session.get(EventMetricModel, entity_id)
        return EventMetric(user_id=row.user_id, event_type=row.event_type, reference_id=row.reference_id, event_date=row.event_date, event_id=row.id) if row else None


class NotificationRepository:
    def create(self, notification: Notification) -> Notification:
        row = NotificationModel(user_id=notification.user_id, channel=notification.channel, content=notification.content, send_status=notification.send_status, send_date=notification.send_date)
        db.session.add(row)
        db.session.commit()
        notification.notification_id = row.id
        return notification

    def list_all(self) -> list[Notification]:
        return [Notification(user_id=row.user_id, channel=row.channel, content=row.content, send_status=row.send_status, send_date=row.send_date, notification_id=row.id) for row in NotificationModel.query.order_by(NotificationModel.id).all()]

    def get_by_id(self, entity_id: int) -> Notification | None:
        row = db.session.get(NotificationModel, entity_id)
        return Notification(user_id=row.user_id, channel=row.channel, content=row.content, send_status=row.send_status, send_date=row.send_date, notification_id=row.id) if row else None


class PartnerRepository:
    def create(self, partner: Partner) -> Partner:
        row = PartnerModel(name=partner.name, partner_type=partner.partner_type, contact=partner.contact)
        db.session.add(row)
        db.session.commit()
        partner.partner_id = row.id
        return partner

    def list_all(self) -> list[Partner]:
        return [Partner(name=row.name, partner_type=row.partner_type, contact=row.contact, partner_id=row.id) for row in PartnerModel.query.order_by(PartnerModel.id).all()]

    def get_by_id(self, entity_id: int) -> Partner | None:
        row = db.session.get(PartnerModel, entity_id)
        return Partner(name=row.name, partner_type=row.partner_type, contact=row.contact, partner_id=row.id) if row else None

    def update(self, partner_id: int, updates: dict) -> Partner | None:
        row = db.session.get(PartnerModel, partner_id)
        if not row:
            return None
        if 'name' in updates:
            row.name = updates['name']
        if 'partner_type' in updates:
            row.partner_type = updates['partner_type']
        if 'contact' in updates:
            row.contact = updates['contact']
        db.session.commit()
        return Partner(name=row.name, partner_type=row.partner_type, contact=row.contact, partner_id=row.id)

    def delete(self, partner_id: int) -> bool:
        row = db.session.get(PartnerModel, partner_id)
        if not row:
            return False
        db.session.delete(row)
        db.session.commit()
        return True


class PartnerOfferRepository:
    def create(self, offer: PartnerOffer) -> PartnerOffer:
        row = PartnerOfferModel(partner_id=offer.partner_id, title=offer.title, description=offer.description, criteria_json=offer.criteria_json, enrollment_url=offer.enrollment_url, is_active=offer.is_active)
        db.session.add(row)
        db.session.commit()
        offer.offer_id = row.id
        return offer

    def list_all(self) -> list[PartnerOffer]:
        return [PartnerOffer(partner_id=row.partner_id, title=row.title, description=row.description, criteria_json=row.criteria_json, enrollment_url=row.enrollment_url, is_active=row.is_active, offer_id=row.id) for row in PartnerOfferModel.query.order_by(PartnerOfferModel.id).all()]

    def get_by_id(self, entity_id: int) -> PartnerOffer | None:
        row = db.session.get(PartnerOfferModel, entity_id)
        return PartnerOffer(partner_id=row.partner_id, title=row.title, description=row.description, criteria_json=row.criteria_json, enrollment_url=row.enrollment_url, is_active=row.is_active, offer_id=row.id) if row else None

    def update(self, offer_id: int, updates: dict) -> PartnerOffer | None:
        row = db.session.get(PartnerOfferModel, offer_id)
        if not row:
            return None
        if 'title' in updates:
            row.title = updates['title']
        if 'description' in updates:
            row.description = updates['description']
        if 'is_active' in updates:
            row.is_active = updates['is_active']
        db.session.commit()
        return PartnerOffer(partner_id=row.partner_id, title=row.title, description=row.description, criteria_json=row.criteria_json, enrollment_url=row.enrollment_url, is_active=row.is_active, offer_id=row.id)

    def delete(self, offer_id: int) -> bool:
        row = db.session.get(PartnerOfferModel, offer_id)
        if not row:
            return False
        db.session.delete(row)
        db.session.commit()
        return True


class InvoiceRepository:
    def create(self, invoice: Invoice) -> Invoice:
        row = InvoiceModel(order_id=invoice.order_id, amount=invoice.amount, due_date=invoice.due_date, client_id=invoice.client_id, status=invoice.status, issue_date=invoice.issue_date)
        db.session.add(row)
        db.session.commit()
        invoice.invoice_id = row.id
        return invoice

    def list_all(self) -> list[Invoice]:
        return [Invoice(order_id=row.order_id, amount=row.amount, due_date=row.due_date, client_id=row.client_id, status=row.status, issue_date=row.issue_date, invoice_id=row.id) for row in InvoiceModel.query.order_by(InvoiceModel.id).all()]

    def get_by_id(self, entity_id: int) -> Invoice | None:
        row = db.session.get(InvoiceModel, entity_id)
        return Invoice(order_id=row.order_id, amount=row.amount, due_date=row.due_date, client_id=row.client_id, status=row.status, issue_date=row.issue_date, invoice_id=row.id) if row else None

    def update_status(self, invoice_id: int, status: str) -> None:
        row = db.session.get(InvoiceModel, invoice_id)
        if row:
            row.status = status
            db.session.commit()


class PaymentRepository:
    def create(self, payment: Payment) -> Payment:
        row = PaymentModel(invoice_id=payment.invoice_id, amount=payment.amount, gateway_type=payment.gateway_type, transaction_gateway=payment.transaction_gateway, status=payment.status, payment_date=payment.payment_date)
        db.session.add(row)
        db.session.commit()
        payment.payment_id = row.id
        return payment

    def list_all(self) -> list[Payment]:
        return [Payment(invoice_id=row.invoice_id, amount=row.amount, gateway_type=row.gateway_type, transaction_gateway=row.transaction_gateway, status=row.status, payment_date=row.payment_date, payment_id=row.id) for row in PaymentModel.query.order_by(PaymentModel.id).all()]

    def get_by_id(self, entity_id: int) -> Payment | None:
        row = db.session.get(PaymentModel, entity_id)
        return Payment(invoice_id=row.invoice_id, amount=row.amount, gateway_type=row.gateway_type, transaction_gateway=row.transaction_gateway, status=row.status, payment_date=row.payment_date, payment_id=row.id) if row else None


class ContentProgressRepository:
    def create(self, progress: ProgressoConteudo) -> ProgressoConteudo:
        row = ContentProgressModel(user_id=progress.user_id, conteudo_id=progress.conteudo_id, status=progress.status, percentual=progress.percentual, ultimo_acesso=progress.ultimo_acesso)
        db.session.add(row)
        db.session.commit()
        progress.progresso_id = row.id
        return progress

    def list_all(self) -> list[ProgressoConteudo]:
        return [ProgressoConteudo(user_id=row.user_id, conteudo_id=row.conteudo_id, status=row.status, percentual=row.percentual, ultimo_acesso=row.ultimo_acesso, progresso_id=row.id) for row in ContentProgressModel.query.order_by(ContentProgressModel.id).all()]

    def get_by_id(self, entity_id: int) -> ProgressoConteudo | None:
        row = db.session.get(ContentProgressModel, entity_id)
        return ProgressoConteudo(user_id=row.user_id, conteudo_id=row.conteudo_id, status=row.status, percentual=row.percentual, ultimo_acesso=row.ultimo_acesso, progresso_id=row.id) if row else None


class DiagnosisRepository:
    def create(self, diagnosis: Diagnostico) -> Diagnostico:
        row = DiagnosisModel(user_id=diagnosis.user_id, score_first=diagnosis.score_first, level=diagnosis.level, answers=diagnosis.answers, date_app=diagnosis.date_app)
        db.session.add(row)
        db.session.commit()
        diagnosis.diagnostico_id = row.id
        return diagnosis

    def list_all(self) -> list[Diagnostico]:
        return [Diagnostico(user_id=row.user_id, score_first=row.score_first, level=row.level, answers=row.answers, date_app=row.date_app, diagnostico_id=row.id) for row in DiagnosisModel.query.order_by(DiagnosisModel.id).all()]

    def get_by_id(self, entity_id: int) -> Diagnostico | None:
        row = db.session.get(DiagnosisModel, entity_id)
        return Diagnostico(user_id=row.user_id, score_first=row.score_first, level=row.level, answers=row.answers, date_app=row.date_app, diagnostico_id=row.id) if row else None